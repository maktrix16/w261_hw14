import sys
import ast
import json
from pyspark import SparkContext

def matchIndex(pagerank_file, indices_file, output_file):
    
    #page rank result
    result = sc.textFile(pagerank_file)
    result = result.map(lambda x: (ast.literal_eval(x)[0],ast.literal_eval(x)[1])) #.keyBy(lambda r: r[0])

    #indices file
    result2 = sc.textFile(indices_file) \
        .map(lambda x: (int(x.split("\t")[1]),x.split("\t")[0])) \
        
    #larger version "s3n://ucb-mids-mls-networks/wikipedia/indices.txt"
    #smaller version of index file->  sampleWikiIndex

    #join and sort
    joinedResult = result.join(result2).map(lambda (x,y): (y[1],y[0])).sortBy(lambda (k,v): -v) \
        .collect() #.saveAsTextFile(output_file)
    
    #write result
    with open(output_file,"w") as f:
        for line in joinedResult:
            f.write(str(line[0]) + "\t" + str(line[1]) + "\n")

if __name__ == "__main__":
    
    # two arguments
    #  1. page rank result in tuple format
    #  2. index file path
    
    if len(sys.argv) < 3:
        print >> sys.stderr, "Usage: nodename_score <pagerank_file> <indices_file> <output_file>"
        exit(-1)

    [pagerank_file, indices_file, output_file] = sys.argv[1:4]
    
    sc = SparkContext(appName="MatchNameWithIndex")
    matchIndex(pagerank_file , indices_file, output_file)    
    sc.stop()