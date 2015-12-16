#!/usr/bin/env python
import sys
from pyspark import SparkContext
from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.linalg import SparseVector
from pyspark.mllib.tree import GradientBoostedTrees, GradientBoostedTreesModel
from pyspark.mllib.util import MLUtils
from types import *

def parsePoint(point):
    ##exclude the first 13 features always as they are numerical
    return [(i,j)for i,j in enumerate(point.split(',')[14:])]

def createOneHotDict(inputData):
    sampleDistinctFeats = (inputData #.flatMap(filterNumbers)
                         .flatMap(lambda x: x)
                      .distinct())
    return (sampleDistinctFeats
                           .zipWithIndex()
                             .collectAsMap())  

# TODO: Replace <FILL IN> with appropriate code
def oneHotEncoding(rawFeats, OHEDict, numOHEFeats,first13):
    rawFeats=sorted(rawFeats)
    num=[]
    arr=[]
    for j,i in enumerate(first13):
        if i != '':
            num.append(j)
            arr.append(i)
    OHEFeats=[]
    for i in OHEDict.keys():
        if i in rawFeats:
            OHEFeats.append(i)
                  
    return SparseVector(26+13,sorted(num+\
                            [OHEDict[i]+13 for i in OHEFeats]),\
                        arr+[1.0 for i in range(len(OHEFeats))]) #[i for i in first13]+

def parseOHEPoint(point, OHEDict, numOHEFeats):
    featurelist=point.strip().split(',')
    return LabeledPoint(featurelist[0],oneHotEncoding([(i,j) for i,j in enumerate(featurelist[14:]) ],\
                                                      OHEDict, 26+13,[i for i in featurelist[1:14]]))

def maaro(z):
    if z[1]=='':
        return (-1,0)
    else:
        return(z,1)

#main GBDT function
def run_GBDT(input_file,output_file,iterations):
    dataRDD=sc.textFile(input_file).map(lambda x: x.replace('\t',','))
    #Now let us create labeled point from data
    dataRDDParsed=dataRDD.map(parsePoint).cache()
    featSet=dataRDDParsed.flatMap(lambda x: x).map(maaro).reduceByKey(lambda a,b: a+b).takeOrdered(26,lambda (k,v): -v)
    #reduceByKey(lambda x,y:x+y).takeOrdered(25,lambda (k,v):-v)
    #print featSet
    #OHEdict=createOneHotDict(dataRDDParsed,featSet)
    OHEdict={}
    for i,x in enumerate(featSet):
#         print i,x
        OHEdict[x[0]]=i
   
    #print oneHotEncoding(dataRDDParsed,OHEdict,numSampleOHEFeats,)
    #Now let us create a dictionary of points
#     weights=[.8,.1,.1]
#     seed=42
#     trainRDD,validateRDD,testRDD=dataRDD.randomSplit(weights,seed)
#     OHETrainData = trainRDD.map(lambda point: parseOHEPoint(point, OHEdict, 39))
    OHETrainData = dataRDD.map(lambda point: parseOHEPoint(point, OHEdict, 39))
#     print OHETrainData.take(1)
#     print OHETrainData.count()

    model = (GradientBoostedTrees.trainClassifier(OHETrainData, loss = 'logLoss', numIterations=2, 
             categoricalFeaturesInfo={}, learningRate = 0.1, maxDepth = 7, maxBins = 2))
    
    sc.parallelize([model.toDebugString()]).coalesce(1).saveAsTextFile(output_file)  
    
#Execute code    
if __name__== '__main__':
#     if len(sys.argv) < 3:
#         print >> sys.stderr, "Usage: page_rank <initialize sc ?> <input file> <output file> <damping factor> <number_of_iterations>"
#         exit(-1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    input_iterations =int(sys.argv[3])
    
    sc = SparkContext(appName="GBDT")
    run_GBDT(input_file,output_file,input_iterations)
    sc.stop()