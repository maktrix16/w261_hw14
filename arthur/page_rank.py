#!/usr/bin/env python
import ast
# import time
import sys
from pyspark import SparkContext

# start_time = time.time()

# Input:  (node, {adjacencies_list})
# Output: [nodes_list]
def get_nodes(line):
    main_node, adjacencies = line[0], line[1]
    adjacencies = ast.literal_eval(adjacencies)
    nodes = [main_node]
    for node in adjacencies.keys():
        nodes.append(node)
    return nodes

# Input:  (node, (adjacency_list, PageRank))
# Output: ('dangling_node', (adjacency_list, PageRank or 0))
def get_dangling_node_mass(main_node, (adjacencies, PageRank)):
    if adjacencies == None:
        return [('dangling_node', PageRank)]
    else:
        return [('dangling_node', 0)]

# Input:  (node, (adjacency_list, PageRank))
# Output: (node, (adjacency_list, PageRank))
def get_contributions(main_node, (adjacencies, PageRank)):
    if adjacencies == None:
        return [(main_node, (adjacencies, 0))]
    else:
        output = [(main_node, (adjacencies, 0))]
        adjacencies = ast.literal_eval(adjacencies)
        num_adjacencies = len(adjacencies.keys())
        for node in adjacencies.keys():
            output.append((node, (None, 1.0*PageRank / num_adjacencies)))
        return output

# Input:  (adjacency_list, PageRank)
# Output: (adjacency_list, PageRank)
def sum_contributions(a, b):
    if a[0] == None:
        if b[0] == None:
            return (None, a[1] + b[1])
        else:
            return (b[0], a[1] + b[1])
    else:
        return (a[0], a[1] + b[1])

    
# Input:  (adjacency_list, PageRank)
# Output: (adjacency_list, new_PageRank)
def calc_pagerank(adjacencies, PageRank, d, num_nodes, dangling_mass):
#     PageRank =  1.0*(1.0-d_br.value)/num_nodes_br.value + \
#                 1.0*d_br.value*(dangling_mass_br.value/num_nodes_br.value + PageRank)  

    PageRank =  1.0*(1.0-d)/num_nodes + \
                1.0*d*(dangling_mass/num_nodes + PageRank)  

    return (adjacencies, PageRank)


def main_page_rank(input_file,output_file,d,iterations):

    #get node and neighbor info from raw data into RDD
    data = (sc.textFile(input_file, 4)
             .map(lambda x: (x.split("\t")[0].encode('ascii','ignore'), x.split("\t")[1].encode('ascii','ignore')))
             .cache()
               )

    # get all main nodes with their adjacency lists and any adjacent nodes that are dangling nodes
    # Input:  [node, {adjacency_list}]
    # Output: [(node, {adjacency_list} or None)]
    unique_nodes = (data.map(lambda x: x).flatMap(get_nodes)         
                     .distinct()                     
                     .map(lambda x: (x, ''))         
                     .leftOuterJoin(data)       
                     .map(lambda (x, y): (x, y[1]))  
#                          .partitionBy(8)
#                          .persist()
                     .cache()
                   )

    num_nodes = unique_nodes.count()
#     num_nodes_br = sc.broadcast(num_nodes)

    # initialize all PageRanks to 1/num_nodes
    # Input: [(node, {adjacency_list} or None)]  
    # Output: [(node, ({adjacency_list}, 1/num_nodes))]
#     PageRanks = unique_nodes.flatMap(lambda (node, adjacencies): [(node, (adjacencies, 1.0/num_nodes_br.value))]).cache()
    PageRanks = unique_nodes.flatMap(lambda (node, adjacencies): [(node, (adjacencies, 1.0/num_nodes))]).cache()


    # iteratively calculate new PageRanks
#     iterations = 3
#     d = 0.85


    for i in range(iterations):
        # calculate dangling node mass
        # Input:  [(node, ({adjacencies_list}, PageRank))]
        # Output: [('dangling_node', (None, PageRank))]
        dangling_mass = (PageRanks
            .flatMap(lambda (node, (adjacencies, PageRank)): get_dangling_node_mass(node, (adjacencies, PageRank)))
            .aggregate(0, (lambda acc, value: acc + value[1]), (lambda acc1, acc2: acc1 + acc2))
                         )

        # calculate contributions of each node to its adjacencies
        # Input:  [(node, ({adjacencies_list}, PageRank))]
        # Output: [(node, ({adjacencies_list}, PageRank))]
        PageRanks = (PageRanks
            .flatMap(lambda (node, (adjacencies, PageRank)): get_contributions(node, (adjacencies, PageRank)))
            .reduceByKey(lambda a, b: sum_contributions(a, b))
            .cache()
                     )

        PageRanks.count() # this random action is needed to get the dangling node mass accumulator to run

        # broadcast parameters and dangling node mass to all workers
#         d_br = sc.broadcast(d)
#         num_nodes_br = sc.broadcast(num_nodes)
        dangling_mass_br = sc.broadcast(dangling_mass)

        # calculate new PageRanks
        # Input:  [(node, ({adjacencies_list}, PageRank))]
        # Output: [(node, ({adjacencies_list}, PageRank))]
#         PageRanks = (PageRanks.mapValues(lambda (adjacencies, PageRank): calc_pagerank(adjacencies, PageRank))     
#                      )

        PageRanks = (PageRanks.mapValues(lambda (adjacencies, PageRank): calc_pagerank(adjacencies, PageRank, d, num_nodes, dangling_mass_br.value)) 
                     )
        
#         # check that PageRanks sum to 1
#         total = PageRanks.aggregate(0, (lambda acc, value: acc + value[1][1]), (lambda acc1, acc2: acc1 + acc2))
#         print 'Sum of all new PageRanks for iteration %i = %f' %(i + 1, total)

#     elapsed_time = time.time() - start_time
#     print 'Total run-time was %f seconds.' %(elapsed_time)
    print 'Final PageRanks after %i iterations:' %(iterations)
#     print PageRanks.collect()

    PageRanks.saveAsTextFile(output_file)

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print >> sys.stderr, "Usage: page_rank <initialize sc ?> <input file> <output file> <damping factor> <number_of_iterations>"
        exit(-1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    input_d = float(sys.argv[3])
    input_iterations =int(sys.argv[4])
    
    sc = SparkContext(appName="PageRank")
    main_page_rank(input_file,output_file,input_d, input_iterations)
    sc.stop()