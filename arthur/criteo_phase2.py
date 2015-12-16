#!/usr/bin/env python
import sys
from pyspark import SparkContext
import numpy as np
from math import log
from math import exp
import hashlib
from collections import defaultdict
from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.linalg import SparseVector
from pyspark.mllib.evaluation import BinaryClassificationMetrics
from pyspark.mllib.classification import LogisticRegressionWithSGD
import csv
import ast
import json
import time

def hashFunction(numBuckets, rawFeats, printMapping=False):
    """Calculate a feature dictionary for an observation's features based on hashing.

    Note:
        Use printMapping=True for debug purposes and to better understand how the hashing works.

    Args:
        numBuckets (int): Number of buckets to use as features.
        rawFeats (list of (int, str)): A list of features for an observation.  Represented as
            (featureID, value) tuples.
        printMapping (bool, optional): If true, the mappings of featureString to index will be
            printed.

    Returns:
        dict of int to float:  The keys will be integers which represent the buckets that the
            features have been hashed to.  The value for a given key will contain the count of the
            (featureID, value) tuples that have hashed to that key.
    """
    mapping = {}
    for ind, category in rawFeats:
        featureString = category + str(ind)
        mapping[featureString] = int(int(hashlib.md5(featureString).hexdigest(), 16) % numBuckets)
    if(printMapping): print mapping
    sparseFeatures = defaultdict(float)
    for bucket in mapping.values():
        sparseFeatures[bucket] += 1.0
    
    return dict(sparseFeatures)


def parseHashPoint(point, numBuckets):
    """Create a LabeledPoint for this observation using hashing.

    Args:
        point (str): A comma separated string where the first value is the label and the rest are
            features.
        numBuckets: The number of buckets to hash to.

    Returns:
        LabeledPoint: A LabeledPoint with a label (0.0 or 1.0) and a SparseVector of hashed
            features.
    """
    values = [x for x in point.split(",")]
    num_features = len(values) - 1
    x = []
    for i in range(num_features):
        x.append((i, values[i+1]))
    features = SparseVector(numBuckets,hashFunction(numBuckets, x, False))
        
    return LabeledPoint(values[0], features)


def getP(x, w, intercept):
    """Calculate the probability for an observation given a set of weights and intercept.

    Note:
        We'll bound our raw prediction between 20 and -20 for numerical purposes.

    Args:
        x (SparseVector): A vector with values of 1.0 for features that exist in this
            observation and 0.0 otherwise.
        w (DenseVector): A vector of weights (betas) for the model.
        intercept (float): The model's intercept.

    Returns:
        float: A probability between 0 and 1.
    """
    rawPrediction = x.dot(w) + intercept

    # Bound the raw prediction value
    rawPrediction = min(rawPrediction, 20)
    rawPrediction = max(rawPrediction, -20)
    
    return 1.0/(1 + exp(-1.0*rawPrediction))


def computeLogLoss(p, y):
    """Calculates the value of log loss for a given probability and label.

    Note:
        log(0) is undefined, so when p is 0 we need to add a small value (epsilon) to it
        and when p is 1 we need to subtract a small value (epsilon) from it.

    Args:
        p (float): A probabilty between 0 and 1.
        y (int): A label.  Takes on the values 0 and 1.

    Returns:
        float: The log loss value.
    """
    epsilon = 10e-12
    p = np.maximum(epsilon, p)
    p = np.minimum(1-epsilon, p)
    logLoss = y*np.log(p) + (1 - y)*np.log(1 - p)
    logLoss = logLoss * -1.0
    
    return logLoss


def evaluateResults(model, data):
    """Calculates the log loss and AUC for the data given the model.

    Args:
        model (LogisticRegressionModel): A trained logistic regression model.
        data (RDD of LabeledPoint): Labels and features for each observation.

    Returns:
        float: Log loss for the data.
    """
    predictionWithLabel = (data.map(lambda x: (getP(x.features, model.weights, model.intercept), x.label)))
    logLoss     = (predictionWithLabel
                   .map(lambda x: computeLogLoss(x[0], x[1]))
                   .reduce(lambda a, b: a + b)
                  )/predictionWithLabel.count()
    metrics = BinaryClassificationMetrics(predictionWithLabel)
    auc = metrics.areaUnderROC
    
    return logLoss, auc


def main_lr_model(input_train, input_val, input_test, output_file, splitData, hashData,  \
                  numHashBuckets, stepSizes, regParams, regType, includeIntercept):

    if splitData == 'True':
        splitData = True
    else:
        splitData = False
    if hashData == 'True':
        hashData = True
    else:
        hashData = False
    if regType == 'None':
        regType = None
    if includeIntercept == 'True':
        includeIntercept = True
    else:
        includeIntercept = False
      
    # get data from file, split if splitData = True, hash if hashData = True
    
    # read in train data
    # work with either ',' or '\t' separated data
    rawTrainData = (sc.textFile(input_train).map(lambda x: x.replace('\t', ',')))
    rawTrainData.cache()
    
    if input_val != 'None':
        rawValidationData = (sc.textFile(input_val).map(lambda x: x.replace('\t', ',')))
        rawValidationData.cache()
    
    if input_test != 'None':
        rawTestData = (sc.textFile(input_test).map(lambda x: x.replace('\t', ',')))
        rawTestData.cache()
    
    if splitData == True or input_val == 'None' or input_test == 'None':
        
        # split the raw data into training, validation, and test datasets
        weights = [.8, .1, .1]
        seed = 42

        rawTrainData, rawValidationData, rawTestData = rawTrainData.randomSplit(weights, seed)
        rawTrainData.cache()
        rawValidationData.cache()
        rawTestData.cache()

#     final_outputs=[]
    final_outputs=sc.emptyRDD()
    run_count = 0
        
    if hashData == True:
        for numHashBucket in numHashBuckets:

            # hash the data
            hashTrainData = rawTrainData.map(lambda point: parseHashPoint(point,numHashBucket))
            hashTrainData.cache()
            hashValidationData = rawValidationData.map(lambda point: parseHashPoint(point,numHashBucket))
            hashValidationData.cache()
            hashTestData = rawTestData.map(lambda point: parseHashPoint(point,numHashBucket))
            hashTestData.cache()

            for stepSize in stepSizes:
                for regParam in regParams:
        
                    # test hyperparameters: stepSize, regParam, regType, includeIntercept
                    # output: log loss and AUC for training, validation, and test datasets
                        
                    # build logistic regression model
                    model = (LogisticRegressionWithSGD
                                .train(hashTrainData, step = stepSize, regParam = regParam,  \
                                       regType=regType, intercept=includeIntercept))

                    # evaluate the model
                    logLossTrain, aucTrain = evaluateResults(model, hashTrainData)
                    logLossVal, aucVal = evaluateResults(model, hashValidationData)
                    logLossTest, aucTest = evaluateResults(model, hashTestData)
    
                    output_line = (stepSize, regParam, regType, includeIntercept, logLossTrain, 
                                   aucTrain,logLossVal, aucVal, logLossTest, aucTest)

                    run_count+=1               

                    output_rdd = sc.parallelize([(run_count,output_line)])
                    final_outputs = final_outputs.union(output_rdd)
                        
    else:
#         for j in range(stepSize_start, stepSize_end, stepSize_incr):
        for stepSize in stepSizes:
        
#             for k in range(0, regParam_iterations, 1):
#                 regParam = 1.0*regParam_start + 1.0*regParam_incr*k
            for regParam in regParams:
                        
                # test hyperparameters: stepSize, regParam, regType, includeIntercept
                # output: log loss and AUC for training, validation, and test datasets
                        
                # build logistic regression model
                model = (LogisticRegressionWithSGD
                            .train(hashTrainData, step = stepSize, regParam = regParam,  \
                                   regType=regType, intercept=includeIntercept))

                # evaluate the model
                logLossTrain, aucTrain = evaluateResults(model, hashTrainData)
                logLossVal, aucVal = evaluateResults(model, hashValidationData)
                logLossTest, aucTest = evaluateResults(model, hashTestData)
    
                #configure output
                output_line = (stepSize, regParam, regType, includeIntercept, logLossTrain, 
                               aucTrain,logLossVal, aucVal, logLossTest, aucTest)
                run_count+=1               
                output_rdd = sc.parallelize([(run_count,output_line)])
                final_outputs = final_outputs.union(output_rdd)

    #save output
    final_outputs.sortByKey(True).coalesce(1).saveAsTextFile(output_file)

    return


if __name__ == "__main__":
    
    #obtain data from json input
    sc = SparkContext(appName="criteo_phase2") 
    
    input_data = sc.textFile(sys.argv[1]).map(lambda line: json.loads(line)).collect()[0]
 
    if input_data["splitData"]=="True": input_data["splitData"]==True
    else: input_data["splitData"]=False
    
    if input_data["hashData"]=="True": input_data["hashData"]==True
    else: input_data["hashData"]=False
        
    if input_data["regType"]=="None": input_data["regType"]=None

    if input_data["includeIntercept"]=="True": input_data["includeIntercept"]==True
    else: input_data["includeIntercept"]=False    

    main_lr_model(input_data["input_train"], 
                  input_data["input_val"], 
                  input_data["input_test"], 
                  input_data["output_file"], 
                  input_data["splitData"], 
                  input_data["hashData"],
                  input_data["numHashBuckets"],
                  input_data["stepSize"],
                  input_data["regParam"],
                  input_data["regType"], 
                  input_data["includeIntercept"]
    )

    sc.stop()