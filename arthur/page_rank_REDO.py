#!/usr/bin/env python
import ast
import sys
import time
from pyspark import SparkContext


# Input:  (node, {adjacencies_list})
# Output: [nodes_list]
def get_nodes_REDO(line):
    main_node, adjacencies = line[0], line[1]
    adjacencies = ast.literal_eval(adjacencies)
    nodes = [(main_node, adjacencies)]
    for node in adjacencies.keys():
        nodes.append((node, None))
    return nodes


# Input:  {adjacencies_list} or None
# Output: {adjacencies_list} or None
def final_adjacencies(a, b):
    if a == None:
        if b == None:
            return None
        else:
            return b
    else:
        return a

    
# Input: (node, (adjacency_list, PageRank))
# Output: (node, contribution)
def get_contributions_REDO(main_node, (adjacencies, PageRank)):
    start_time_REDO = time.time()

    if adjacencies == None:
        output = [(main_node, 0)]
        output.append(('dangling_mass', PageRank))
        return output
    else:
        output = [(main_node, 0)]
        adjacencies = ast.literal_eval(str(adjacencies))
        num_adjacencies = len(adjacencies.keys())
        for node in adjacencies.keys(): 
            output.append((node, 1.0*PageRank / num_adjacencies))
        return output
    

# Input: (contributions, d, num_nodes, dangling_mass)
# Output: (new_PageRank)
def calc_pagerank_REDO(contributions, d, num_nodes, dangling_mass):
    PageRank =  1.0*(1.0-d)/num_nodes + \
                1.0*d*(dangling_mass/num_nodes + contributions)  
    return PageRank


def main_page_rank_REDO(input_file,output_file,partitions,d,iterations):

    #get graph from raw data into RDD
    graph = (sc.textFile(input_file, partitions)
             .map(lambda x: (x.split("\t")[0].encode('ascii','ignore'), x.split("\t")[1].encode('ascii','ignore')))
             .cache()
               )
    
    # get all main nodes with their adjacency lists and any adjacent nodes that are dangling nodes
    # Input:  [node, {adjacency_list}]
    # Output: [(node, {adjacency_list} or None)]
    complete_graph = (graph.flatMap(get_nodes_REDO)         
                           .reduceByKey(lambda a, b: final_adjacencies(a,b))        
                           .partitionBy(partitions)
                           .cache()
                     )

    num_nodes = complete_graph.count()  # should force evaluation
    
    # initialize all PageRanks to 1/num_nodes
    # Input: [(node, {adjacency_list} or None)]  
    # Output: [(node, 1/num_nodes)]
    PageRanks = complete_graph.map(lambda (node, adjacencies): (node, 1.0/num_nodes)).cache()    
    PageRanks.take(1)    # should force evaluation
    
    # iteratively calculate new PageRanks
    for i in range(iterations):
        start_time_c = time.time()        

        # join graph and latest page ranks
        joined_graph = (complete_graph
                        .join(PageRanks)
                        .cache()
                        )
        joined_graph.take(1)
        
        # calculate contributions of each node to its adjacencies
        # Input:  [(node, ({adjacencies_list}, PageRank))]
        # Output: [(node, sum of contributions)]

        contributions = (joined_graph
        .flatMap(lambda (node, (adjacencies, PageRank)): get_contributions_REDO(node, (adjacencies, PageRank)))
        .reduceByKey(lambda x, y: x + y)
        .cache()
                        )
        contributions.take(1)
  
        dangling_mass = contributions.lookup('dangling_mass')[0]
        
        # broadcast dangling node mass to all workers
        dangling_mass_br = sc.broadcast(dangling_mass)
        d_br = sc.broadcast(d)
        num_nodes_br = sc.broadcast(num_nodes)
        start_time = time.time()
        # calculate new PageRanks
        # Input:  [(node, sum of contributions)]
        # Output: [(node, PageRank)]
        PageRanks = (contributions
            .filter(lambda (x, y): x != 'dangling_mass')
            .mapValues(lambda contribs: calc_pagerank_REDO(contribs, d_br.value, num_nodes_br.value, dangling_mass_br.value)) 
                     )
        PageRanks.take(1) # forcing evaluation

        # check that PageRanks sum to 1
#         total = PageRanks.aggregate(0, (lambda acc, value: acc + value[1]), (lambda acc1, acc2: acc1 + acc2)) 
#         print >> sys.stdout, "***********************Total PageRank****************************************"
#         print >> sys.stdout, total
        
        print >> sys.stdout, "Iteration: " + str(i) + "  Time: " + str(time.time() - start_time)
        print >> sys.stdout, PageRanks.collect()
    PageRanks.saveAsTextFile(output_file)

if __name__ == "__main__":
    if len(sys.argv) < 5:
        print >> sys.stderr, "Usage: page_rank <initialize sc ?> <input file> <output file> <damping factor> <number_of_iterations>"
        exit(-1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    input_partitions = int(sys.argv[3])
    input_d = float(sys.argv[4])
    input_iterations =int(sys.argv[5])
    
    sc = SparkContext(appName="PageRank")
    main_page_rank_REDO(input_file,output_file,input_partitions,input_d,input_iterations)
    sc.stop()    
    
