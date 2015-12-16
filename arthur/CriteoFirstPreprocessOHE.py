import sys
import ast
import json
from pyspark import SparkContext
from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.linalg import SparseVector


#Compile a tuple of categorical feature and its value
def parsePointForCategoricalOnly(point):
    """Converts a comma separated string into a list of (featureID, value) tuples ONLY IF value is not an integer. 
    Note:
        featureIDs should start at 0 and increase to the number of features - 1.

    Args:
        point (str): A comma separated string where the first value is the label and the rest
            are features.

    Returns:
        list: A list of (featureID, value) tuples.
        [(1, "cat"), (1,"dog"), ... ]
    """
    values = [x for x in point.split("\t")]
    num_features = len(values)
    x = []
    
    #get only 14th feature and after
    index = 0
    for i in range(14, num_features):
            x.append((index, values[i]))
            index +=1
    return x

#create one-hot-encoder dictionary given a raw input
def createOneHotDict(categoricalDataOnly):
    """Creates a one-hot-encoder dictionary based on the input data.

    Args:
        inputData  NOW RDD of tuple of all of the features -- OLD  (RDD of lists of (int, str)): An RDD of observations where each observation is
            made up of a list of (featureID, value) tuples.

    Returns:
        dict: A dictionary where the keys are (featureID, value) tuples and map to values that are
            unique integers.
            [((3, "cat"),4),((1, "dog"),1)] 
    """
    #get tuples for each 
    #inputData = rawData.map(parsePointForCategoricalOnly)
    #print parsedTrainFeat.take(1)
    
    #remove collectAsMap as creating dictionay would not work well with large datasets!
    return (categoricalDataOnly
            .flatMap(lambda x: x) #everything here and below is to create a dictionary
            .distinct()
            .sortByKey()
            .zipWithIndex()      
           )
    #return (rawData
    #        .map(parsePointForCategoricalOnly) #get tuple of all of the features
    #        .flatMap(lambda x: x) #everything here and below is to create a dictionary
    #        .distinct()
    #        .sortByKey()
    #        .zipWithIndex()
    #        .collectAsMap()            
    #       )

def oneHotEncoding(rawFeats, OHEDict, numOHEFeats):
    """Produce a one-hot-encoding from a list of features and an OHE dictionary.

    Note:
        If a (featureID, value) tuple doesn't have a corresponding key in OHEDict it should be
        ignored.

    Args:
        rawFeats (list of (int, str)): The features corresponding to a single observation.  Each
            feature consists of a tuple of featureID and the feature's value. (e.g. sampleOne)
        OHEDict (now RDD for performance reason -- OLD (dict):   A mapping of (featureID, value) to unique integer.
        numOHEFeats (int): The total number of unique OHE features (combinations of featureID and
            value).

    Returns:
        SparseVector: A SparseVector of length numOHEFeats with indicies equal to the unique
            identifiers for the (featureID, value) combinations that occur in the observation and
            with values equal to 1.0.
    """
    #print >> sys.stderr, OHEDict    
    #format of OHEDict
    #((14, u'4a0593ee'), 0)
    
    featureArray = []
    for featTuple in rawFeats:
        
        if featTuple in OHEDict: #tuple is in the dict 
            featureArray.append(OHEDict[featTuple])
        else: #skip it
            pass
    
    #sort the indices
    featureArray.sort()
    
    #we are assuming no duplicates, thus occurrence of each feature is 1 (last parameter in SparseVector)
    return SparseVector(numOHEFeats, featureArray,[1] * len(featureArray))

#for each line of data return either sparse vector or raw data, given a dictionary
def parseOHEPoint(point, OHEDict, getRaw=False):
    """Obtain the label and feature vector for this raw observation.

    Note:
        You must use the function `oneHotEncoding` in this implementation or later portions
        of this lab may not function as expected.

    Args:
        point (str): A comma separated string where the first value is the label and the rest
            are features.
        OHEDict  it's now an RDD for performance reason --OLD -  (dict of (int, str) to int): Mapping of (featureID, value) to unique integer.
        getRaw: if false, return LabelPoint with SparseVector for categorical features. 
                if true, return "\t" delimited mixture of integer and categorical features 
                        withon categorical features having value of either 0 or 1 

    Returns:
        LabeledPoint: Contains the label for the observation and the one-hot-encoding of the
            raw features based on the provided OHE dictionary.
    """
    #numOHEFeats = len(OHEDict)
    numOHEFeats = OHEDict.count()
    #print >> sys.stderr, OHEDict

    values = [x for x in point.split("\t")]
    num_features = len(values)
    x = []
    
    #per Criteo Winner's Powerpoint we will treat only 14th feature and later as categorical
    for i in range(14, num_features):
        x.append((i, values[i]))
    features = oneHotEncoding(x, OHEDict, numOHEFeats)
    
    if getRaw: #must collect label and integer features in addition to the categorical ones
        rawDataArray = []
        
        #get label and integer features
        for i in range(0,13):
            rawDataArray.append(values[i])
        
        #now convert SparseVector features to 
        rawDataArray.extend([str(int(x)) for x in features.toArray().tolist()])
        return "\t".join(rawDataArray)
        
    else: 
        return LabeledPoint(values[0], features)


def main_preprocessWithOHE(input_file, limit, output_file):
    
    #test on sample
    rawData = sc.textFile(input_file) #'dac_sample.txt'
    #rawData.cache() #cache since it will be used later to generate final preprocessed output
    
    categoricalDataOnly = rawData.map(parsePointForCategoricalOnly).flatMap(lambda x: x) # \get tuple of only categorical features
    categoricalDataOnly.cache()
    
    #create dictionary of all of the features
    #prelimOHEDict = categoricalDataOnly \
    #        .distinct() #\
            #.sortByKey() #\
            #.zipWithIndex()     
           
    #prelimOHEDict = createOneHotDict(rawData) 
    #print prelimOHEDict.take(1)
    #(14, u'4a0593ee')
   
    #apply OHE to each data based on dictionary created above
    #prelimOHETrainData = categoricalDataOnly.map(lambda point: parseOHEPoint(point, prelimOHEDict))
    
    #now get count of each features so we can prune them
    #featCounts = (prelimOHETrainData
    #          .flatMap(lambda lp: lp.features.indices)
    #          .map(lambda x: (x, 1))
    #          .reduceByKey(lambda x, y: x + y)).sortByKey()
    featCounts = (categoricalDataOnly
                .map(lambda x: (x,1))
                .reduceByKey(lambda x, y: x + y)).sortByKey()
    #print featCounts.take(30) 
    #format
    #[((14, u'1695330e'), 2), ((14, u'169f6798'), 5), ((14, u'16a99cfb'), 12)]
    
    #based on the count prune and create new dictionary
    prunedOHCDictionary = featCounts \
        .filter(lambda keyValue: keyValue[1] >= int(limit)) \
        .map(lambda x: "C" + str(x[0][0]) + "_" + str(x[0][1])) 
        
#    print prunedOHCDictionary.take(10)
#    return
    
              #.join(featCounts) #\
              #.filter(lambda keyValue: keyValue[1][1] >= int(limit)) \
              #.sortByKey() \
              #.map(lambda x: str(x[1][0][0]) + "_" + str(x[1][0][1]))  #.zipWithIndex().collectAsMap() #take(10)
    #prunedOHCDictionary = prelimOHEDict \
    #          .map(lambda x: (x[0],x[1])) \
    #          .join(featCounts) \
    #          .filter(lambda keyValue: keyValue[1][1] >= int(limit)) \
    #          .sortByKey() \
    #          .map(lambda x: str(x[1][0][0]) + "_" + str(x[1][0][1]))  #.zipWithIndex().collectAsMap() #take(10)
    #key, value =  prunedOHCDictionary.popitem()
    #print key
    #print value
    #print prunedOHCDictionary.take(1)
    prunedOHCDictionary.saveAsTextFile(output_file)

    #parse raw data again and create features
    #finalTrainData = rawData.map(lambda point: parseOHEPoint(point, prunedOHCDictionary, True))
    #OHETrainDataPruned.cache()
    #print OHETrainDataPruned.take(1)    
    
    #finalTrainData.saveAsTextFile(output_file)
    
if __name__ == "__main__":
    
    # two arguments
    #  1. input file
    #  2. limit
    #  3. output file
    
    if len(sys.argv) < 3:
        print >> sys.stderr, "Usage: input_file limit_for_frequency_of_features <output_file>"
        exit(-1)

    [input_file, limit, output_file] = sys.argv[1:4]
    
    sc = SparkContext(appName="PreprocessOHE")
    main_preprocessWithOHE(input_file, limit, output_file)    
    sc.stop()