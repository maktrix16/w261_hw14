#!/usr/bin/env python
import sys
from pyspark import SparkContext
from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.linalg import SparseVector
from pyspark.mllib.util import MLUtils
from types import *
import hashlib
import math

#hash like 3 idiots!
def hashLike3Idiots(strToHash,numHashBuckets):
    return int(int(hashlib.md5(strToHash.encode('utf8')).hexdigest(), 16)%numHashBuckets)

def get_hashed_bins(point, numHashBuckets,frequentCategories):
    #input is a tuple
    #1st item is row label,2nd is sparse vector, 3rd item is a tuple (category index array, category value array)
    #[(u'0', 
    #(SparseVector(39, {0: 1.0, 1: 1.0, 2: 5.0, 3: 0.0, 4: 1382.0, 5: 4.0, 6: 15.0, 7: 2.0, 8: 181.0, 9: 1.0, 10: 2.0, 12: 2.0, 13: 1.0, 14: 1.0, 17: 1.0, 19: 1.0, 22: 1.0, 25: 1.0, 28: 1.0, 29: 1.0, 31: 1.0, 32: 1.0}), 
    #([39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 61, 62, 63, 64], [u'68fd1e64', u'80e26c9b', u'fb936136', u'7b4723c4', u'25c83c98', u'7e0ccccf', u'de7995b8', u'1f89b562', u'a73ee510', u'a8cd5504', u'b2cb9c98', u'37c9c164', u'2824a5f6', u'1adce6ef', u'8ba8b39a', u'891b62e7', u'e5ba7672', u'f54016b9', u'21ddcdc9', u'b1252a9d', u'07b5194c', u'3a171ecb', u'c5c50484', u'e8b83407', u'9727dd16'])))]
    
    feature = SparseVector.toArray(point[1][0])
    
    bin_num = {}
    
#NEW_RULES_HERE
    # Tree 0
    if (feature[0]<=0.0):
        if (feature[10]<=1.0):
            if (feature[12]<=2.0):
                if (feature[13]<=0.0):
                    if (feature[18]<=0.0):
                        if (feature[17]<=0.0):
                            if (feature[2]<=3.0):
                                bin_num[0] = 0
                            else:
                                bin_num[0] = 1
                        else:
                            if (feature[20]<=0.0):
                                bin_num[0] = 2
                            else:
                                bin_num[0] = 3
                    else:
                        if (feature[2]<=3.0):
                            if (feature[17]<=0.0):
                                bin_num[0] = 4
                            else:
                                bin_num[0] = 5
                        else:
                            if (feature[17]<=0.0):
                                bin_num[0] = 6
                            else:
                                bin_num[0] = 7
                else:
                    if (feature[8]<=36.0):
                        if (feature[6]<=2.0):
                            if (feature[17]<=0.0):
                                bin_num[0] = 8
                            else:
                                bin_num[0] = 9
                        else:
                            if (feature[5]<=15.0):
                                bin_num[0] = 10
                            else:
                                bin_num[0] = 11
                    else:
                        if (feature[17]<=0.0):
                            if (feature[3]<=2.0):
                                bin_num[0] = 12
                            else:
                                bin_num[0] = 13
                        else:
                            if (feature[20]<=0.0):
                                bin_num[0] = 14
                            else:
                                bin_num[0] = 15
            else:
                if (feature[7]<=7.0):
                    if (feature[13]<=0.0):
                        if (feature[18]<=0.0):
                            if (feature[5]<=15.0):
                                bin_num[0] = 16
                            else:
                                bin_num[0] = 17
                        else:
                            if (feature[5]<=15.0):
                                bin_num[0] = 18
                            else:
                                bin_num[0] = 19
                    else:
                        if (feature[17]<=0.0):
                            if (feature[8]<=36.0):
                                bin_num[0] = 20
                            else:
                                bin_num[0] = 21
                        else:
                            if (feature[8]<=36.0):
                                bin_num[0] = 22
                            else:
                                bin_num[0] = 23
                else:
                    if (feature[17]<=0.0):
                        if (feature[18]<=0.0):
                            if (feature[5]<=15.0):
                                bin_num[0] = 24
                            else:
                                bin_num[0] = 25
                        else:
                            if (feature[19]<=0.0):
                                bin_num[0] = 26
                            else:
                                bin_num[0] = 27
                    else:
                        if (feature[20]<=0.0):
                            if (feature[2]<=3.0):
                                bin_num[0] = 28
                            else:
                                bin_num[0] = 29
                        else:
                            if (feature[18]<=0.0):
                                bin_num[0] = 30
                            else:
                                bin_num[0] = 31
        else:
            if (feature[5]<=15.0):
                if (feature[2]<=3.0):
                    if (feature[37]<=0.0):
                        if (feature[17]<=0.0):
                            if (feature[12]<=2.0):
                                bin_num[0] = 32
                            else:
                                bin_num[0] = 33
                        else:
                            if (feature[12]<=2.0):
                                bin_num[0] = 34
                            else:
                                bin_num[0] = 35
                    else:
                        if (feature[27]<=0.0):
                            if (feature[17]<=0.0):
                                bin_num[0] = 36
                            else:
                                bin_num[0] = 37
                        else:
                            if (feature[28]<=0.0):
                                bin_num[0] = 38
                            else:
                                bin_num[0] = 39
                else:
                    if (feature[17]<=0.0):
                        if (feature[20]<=0.0):
                            if (feature[7]<=7.0):
                                bin_num[0] = 40
                            else:
                                bin_num[0] = 41
                        else:
                            if (feature[29]<=0.0):
                                bin_num[0] = 42
                            else:
                                bin_num[0] = 43
                    else:
                        if (feature[7]<=7.0):
                            if (feature[20]<=0.0):
                                bin_num[0] = 44
                            else:
                                bin_num[0] = 45
                        else:
                            if (feature[37]<=0.0):
                                bin_num[0] = 46
                            else:
                                bin_num[0] = 47
            else:
                if (feature[12]<=2.0):
                    if (feature[20]<=0.0):
                        if (feature[17]<=0.0):
                            if (feature[2]<=3.0):
                                bin_num[0] = 48
                            else:
                                bin_num[0] = 49
                        else:
                            if (feature[37]<=0.0):
                                bin_num[0] = 50
                            else:
                                bin_num[0] = 51
                    else:
                        if (feature[18]<=0.0):
                            if (feature[17]<=0.0):
                                bin_num[0] = 52
                            else:
                                bin_num[0] = 53
                        else:
                            if (feature[29]<=0.0):
                                bin_num[0] = 54
                            else:
                                bin_num[0] = 55
                else:
                    if (feature[2]<=3.0):
                        if (feature[20]<=0.0):
                            if (feature[26]<=0.0):
                                bin_num[0] = 56
                            else:
                                bin_num[0] = 57
                        else:
                            if (feature[18]<=0.0):
                                bin_num[0] = 58
                            else:
                                bin_num[0] = 59
                    else:
                        if (feature[7]<=7.0):
                            if (feature[37]<=0.0):
                                bin_num[0] = 60
                            else:
                                bin_num[0] = 61
                        else:
                            if (feature[37]<=0.0):
                                bin_num[0] = 62
                            else:
                                bin_num[0] = 63
    else:
        if (feature[5]<=15.0):
            if (feature[12]<=2.0):
                if (feature[3]<=2.0):
                    if (feature[10]<=1.0):
                        if (feature[20]<=0.0):
                            if (feature[29]<=0.0):
                                bin_num[0] = 64
                            else:
                                bin_num[0] = 65
                        else:
                            if (feature[18]<=0.0):
                                bin_num[0] = 66
                            else:
                                bin_num[0] = 67
                    else:
                        if (feature[37]<=0.0):
                            if (feature[29]<=0.0):
                                bin_num[0] = 68
                            else:
                                bin_num[0] = 69
                        else:
                            if (feature[27]<=0.0):
                                bin_num[0] = 70
                            else:
                                bin_num[0] = 71
                else:
                    if (feature[21]<=0.0):
                        if (feature[37]<=0.0):
                            if (feature[10]<=1.0):
                                bin_num[0] = 72
                            else:
                                bin_num[0] = 73
                        else:
                            if (feature[22]<=0.0):
                                bin_num[0] = 74
                            else:
                                bin_num[0] = 75
                    else:
                        if (feature[9]<=0.0):
                            if (feature[10]<=1.0):
                                bin_num[0] = 76
                            else:
                                bin_num[0] = 77
                        else:
                            if (feature[20]<=0.0):
                                bin_num[0] = 78
                            else:
                                bin_num[0] = 79
            else:
                if (feature[10]<=1.0):
                    if (feature[38]<=0.0):
                        if (feature[21]<=0.0):
                            if (feature[37]<=0.0):
                                bin_num[0] = 80
                            else:
                                bin_num[0] = 81
                        else:
                            if (feature[20]<=0.0):
                                bin_num[0] = 82
                            else:
                                bin_num[0] = 83
                    else:
                        if (feature[7]<=7.0):
                            if (feature[21]<=0.0):
                                bin_num[0] = 84
                            else:
                                bin_num[0] = 85
                        else:
                            if (feature[18]<=0.0):
                                bin_num[0] = 86
                            else:
                                bin_num[0] = 87
                else:
                    if (feature[37]<=0.0):
                        if (feature[21]<=0.0):
                            if (feature[29]<=0.0):
                                bin_num[0] = 88
                            else:
                                bin_num[0] = 89
                        else:
                            if (feature[26]<=0.0):
                                bin_num[0] = 90
                            else:
                                bin_num[0] = 91
                    else:
                        if (feature[21]<=0.0):
                            if (feature[29]<=0.0):
                                bin_num[0] = 92
                            else:
                                bin_num[0] = 93
                        else:
                            if (feature[26]<=0.0):
                                bin_num[0] = 94
                            else:
                                bin_num[0] = 95
        else:
            if (feature[10]<=1.0):
                if (feature[12]<=2.0):
                    if (feature[17]<=0.0):
                        if (feature[7]<=7.0):
                            if (feature[2]<=3.0):
                                bin_num[0] = 96
                            else:
                                bin_num[0] = 97
                        else:
                            if (feature[21]<=0.0):
                                bin_num[0] = 98
                            else:
                                bin_num[0] = 99
                    else:
                        if (feature[20]<=0.0):
                            if (feature[29]<=0.0):
                                bin_num[0] = 100
                            else:
                                bin_num[0] = 101
                        else:
                            if (feature[29]<=0.0):
                                bin_num[0] = 102
                            else:
                                bin_num[0] = 103
                else:
                    if (feature[2]<=3.0):
                        if (feature[20]<=0.0):
                            if (feature[21]<=0.0):
                                bin_num[0] = 104
                            else:
                                bin_num[0] = 105
                        else:
                            if (feature[7]<=7.0):
                                bin_num[0] = 106
                            else:
                                bin_num[0] = 107
                    else:
                        if (feature[21]<=0.0):
                            if (feature[37]<=0.0):
                                bin_num[0] = 108
                            else:
                                bin_num[0] = 109
                        else:
                            if (feature[26]<=0.0):
                                bin_num[0] = 110
                            else:
                                bin_num[0] = 111
            else:
                if (feature[2]<=3.0):
                    if (feature[37]<=0.0):
                        if (feature[12]<=2.0):
                            if (feature[29]<=0.0):
                                bin_num[0] = 112
                            else:
                                bin_num[0] = 113
                        else:
                            if (feature[20]<=0.0):
                                bin_num[0] = 114
                            else:
                                bin_num[0] = 115
                    else:
                        if (feature[27]<=0.0):
                            if (feature[12]<=2.0):
                                bin_num[0] = 116
                            else:
                                bin_num[0] = 117
                        else:
                            if (feature[12]<=2.0):
                                bin_num[0] = 118
                            else:
                                bin_num[0] = 119
                else:
                    if (feature[21]<=0.0):
                        if (feature[37]<=0.0):
                            if (feature[3]<=2.0):
                                bin_num[0] = 120
                            else:
                                bin_num[0] = 121
                        else:
                            if (feature[29]<=0.0):
                                bin_num[0] = 122
                            else:
                                bin_num[0] = 123
                    else:
                        if (feature[3]<=2.0):
                            if (feature[17]<=0.0):
                                bin_num[0] = 124
                            else:
                                bin_num[0] = 125
                        else:
                            if (feature[26]<=0.0):
                                bin_num[0] = 126
                            else:
                                bin_num[0] = 127
    # Tree 1
    if (feature[6]<=2.0):
        if (feature[2]<=3.0):
            if (feature[18]<=0.0):
                if (feature[20]<=0.0):
                    if (feature[7]<=7.0):
                        if (feature[23]<=0.0):
                            if (feature[35]<=0.0):
                                bin_num[1] = 0
                            else:
                                bin_num[1] = 1
                        else:
                            if (feature[25]<=0.0):
                                bin_num[1] = 2
                            else:
                                bin_num[1] = 3
                    else:
                        if (feature[4]<=2704.0):
                            if (feature[10]<=1.0):
                                bin_num[1] = 4
                            else:
                                bin_num[1] = 5
                        else:
                            if (feature[37]<=0.0):
                                bin_num[1] = 6
                            else:
                                bin_num[1] = 7
                else:
                    if (feature[35]<=0.0):
                        if (feature[7]<=7.0):
                            if (feature[23]<=0.0):
                                bin_num[1] = 8
                            else:
                                bin_num[1] = 9
                        else:
                            if (feature[12]<=2.0):
                                bin_num[1] = 10
                            else:
                                bin_num[1] = 11
                    else:
                        if (feature[28]<=0.0):
                            if (feature[4]<=2704.0):
                                bin_num[1] = 12
                            else:
                                bin_num[1] = 13
                        else:
                            if (feature[25]<=0.0):
                                bin_num[1] = 14
                            else:
                                bin_num[1] = 15
            else:
                if (feature[20]<=0.0):
                    if (feature[8]<=34.0):
                        if (feature[11]<=0.0):
                            if (feature[7]<=7.0):
                                bin_num[1] = 16
                            else:
                                bin_num[1] = 17
                        else:
                            if (feature[23]<=0.0):
                                bin_num[1] = 18
                            else:
                                bin_num[1] = 19
                    else:
                        if (feature[5]<=15.0):
                            if (feature[13]<=0.0):
                                bin_num[1] = 20
                            else:
                                bin_num[1] = 21
                        else:
                            if (feature[7]<=7.0):
                                bin_num[1] = 22
                            else:
                                bin_num[1] = 23
                else:
                    if (feature[26]<=0.0):
                        if (feature[19]<=0.0):
                            if (feature[24]<=0.0):
                                bin_num[1] = 24
                            else:
                                bin_num[1] = 25
                        else:
                            if (feature[34]<=0.0):
                                bin_num[1] = 26
                            else:
                                bin_num[1] = 27
                    else:
                        if (feature[13]<=0.0):
                            if (feature[7]<=7.0):
                                bin_num[1] = 28
                            else:
                                bin_num[1] = 29
                        else:
                            if (feature[8]<=34.0):
                                bin_num[1] = 30
                            else:
                                bin_num[1] = 31
        else:
            if (feature[18]<=0.0):
                if (feature[37]<=0.0):
                    if (feature[4]<=2704.0):
                        if (feature[13]<=0.0):
                            if (feature[25]<=0.0):
                                bin_num[1] = 32
                            else:
                                bin_num[1] = 33
                        else:
                            if (feature[34]<=0.0):
                                bin_num[1] = 34
                            else:
                                bin_num[1] = 35
                    else:
                        if (feature[25]<=0.0):
                            if (feature[23]<=0.0):
                                bin_num[1] = 36
                            else:
                                bin_num[1] = 37
                        else:
                            if (feature[20]<=0.0):
                                bin_num[1] = 38
                            else:
                                bin_num[1] = 39
                else:
                    if (feature[8]<=34.0):
                        if (feature[5]<=15.0):
                            if (feature[23]<=0.0):
                                bin_num[1] = 40
                            else:
                                bin_num[1] = 41
                        else:
                            if (feature[35]<=0.0):
                                bin_num[1] = 42
                            else:
                                bin_num[1] = 43
                    else:
                        if (feature[10]<=1.0):
                            if (feature[5]<=15.0):
                                bin_num[1] = 44
                            else:
                                bin_num[1] = 45
                        else:
                            if (feature[5]<=15.0):
                                bin_num[1] = 46
                            else:
                                bin_num[1] = 47
            else:
                if (feature[8]<=34.0):
                    if (feature[19]<=0.0):
                        if (feature[24]<=0.0):
                            if (feature[29]<=0.0):
                                bin_num[1] = 48
                            else:
                                bin_num[1] = 49
                        else:
                            if (feature[5]<=15.0):
                                bin_num[1] = 50
                            else:
                                bin_num[1] = 51
                    else:
                        if (feature[27]<=0.0):
                            if (feature[5]<=15.0):
                                bin_num[1] = 52
                            else:
                                bin_num[1] = 53
                        else:
                            if (feature[5]<=15.0):
                                bin_num[1] = 54
                            else:
                                bin_num[1] = 55
                else:
                    if (feature[5]<=15.0):
                        if (feature[24]<=0.0):
                            if (feature[19]<=0.0):
                                bin_num[1] = 56
                            else:
                                bin_num[1] = 57
                        else:
                            if (feature[27]<=0.0):
                                bin_num[1] = 58
                            else:
                                bin_num[1] = 59
                    else:
                        if (feature[27]<=0.0):
                            if (feature[29]<=0.0):
                                bin_num[1] = 60
                            else:
                                bin_num[1] = 61
                        else:
                            if (feature[22]<=0.0):
                                bin_num[1] = 62
                            else:
                                bin_num[1] = 63
    else:
        if (feature[25]<=0.0):
            if (feature[5]<=15.0):
                if (feature[35]<=0.0):
                    if (feature[20]<=0.0):
                        if (feature[23]<=0.0):
                            if (feature[17]<=0.0):
                                bin_num[1] = 64
                            else:
                                bin_num[1] = 65
                        else:
                            if (feature[11]<=0.0):
                                bin_num[1] = 66
                            else:
                                bin_num[1] = 67
                    else:
                        if (feature[29]<=0.0):
                            if (feature[18]<=0.0):
                                bin_num[1] = 68
                            else:
                                bin_num[1] = 69
                        else:
                            if (feature[34]<=0.0):
                                bin_num[1] = 70
                            else:
                                bin_num[1] = 71
                else:
                    if (feature[22]<=0.0):
                        if (feature[27]<=0.0):
                            if (feature[17]<=0.0):
                                bin_num[1] = 72
                            else:
                                bin_num[1] = 73
                        else:
                            if (feature[1]<=2.0):
                                bin_num[1] = 74
                            else:
                                bin_num[1] = 75
                    else:
                        if (feature[29]<=0.0):
                            if (feature[27]<=0.0):
                                bin_num[1] = 76
                            else:
                                bin_num[1] = 77
                        else:
                            if (feature[34]<=0.0):
                                bin_num[1] = 78
                            else:
                                bin_num[1] = 79
            else:
                if (feature[7]<=7.0):
                    if (feature[2]<=3.0):
                        if (feature[26]<=0.0):
                            if (feature[8]<=34.0):
                                bin_num[1] = 80
                            else:
                                bin_num[1] = 81
                        else:
                            if (feature[37]<=0.0):
                                bin_num[1] = 82
                            else:
                                bin_num[1] = 83
                    else:
                        if (feature[4]<=2704.0):
                            if (feature[27]<=0.0):
                                bin_num[1] = 84
                            else:
                                bin_num[1] = 85
                        else:
                            if (feature[29]<=0.0):
                                bin_num[1] = 86
                            else:
                                bin_num[1] = 87
                else:
                    if (feature[4]<=2704.0):
                        if (feature[29]<=0.0):
                            if (feature[27]<=0.0):
                                bin_num[1] = 88
                            else:
                                bin_num[1] = 89
                        else:
                            if (feature[20]<=0.0):
                                bin_num[1] = 90
                            else:
                                bin_num[1] = 91
                    else:
                        if (feature[26]<=0.0):
                            if (feature[20]<=0.0):
                                bin_num[1] = 92
                            else:
                                bin_num[1] = 93
                        else:
                            if (feature[2]<=3.0):
                                bin_num[1] = 94
                            else:
                                bin_num[1] = 95
        else:
            if (feature[35]<=0.0):
                if (feature[20]<=0.0):
                    if (feature[34]<=0.0):
                        if (feature[33]<=0.0):
                            if (feature[22]<=0.0):
                                bin_num[1] = 96
                            else:
                                bin_num[1] = 97
                        else:
                            if (feature[1]<=2.0):
                                bin_num[1] = 98
                            else:
                                bin_num[1] = 99
                    else:
                        if (feature[26]<=0.0):
                            if (feature[22]<=0.0):
                                bin_num[1] = 100
                            else:
                                bin_num[1] = 101
                        else:
                            if (feature[19]<=0.0):
                                bin_num[1] = 102
                            else:
                                bin_num[1] = 103
                else:
                    if (feature[29]<=0.0):
                        if (feature[19]<=0.0):
                            if (feature[24]<=0.0):
                                bin_num[1] = 104
                            else:
                                bin_num[1] = 105
                        else:
                            if (feature[27]<=0.0):
                                bin_num[1] = 106
                            else:
                                bin_num[1] = 107
                    else:
                        if (feature[34]<=0.0):
                            if (feature[2]<=3.0):
                                bin_num[1] = 108
                            else:
                                bin_num[1] = 109
                        else:
                            if (feature[5]<=15.0):
                                bin_num[1] = 110
                            else:
                                bin_num[1] = 111
            else:
                if (feature[7]<=7.0):
                    if (feature[28]<=0.0):
                        if (feature[2]<=3.0):
                            if (feature[23]<=0.0):
                                bin_num[1] = 112
                            else:
                                bin_num[1] = 113
                        else:
                            if (feature[20]<=0.0):
                                bin_num[1] = 114
                            else:
                                bin_num[1] = 115
                    else:
                        if (feature[20]<=0.0):
                            if (feature[33]<=0.0):
                                bin_num[1] = 116
                            else:
                                bin_num[1] = 117
                        else:
                            if (feature[23]<=0.0):
                                bin_num[1] = 118
                            else:
                                bin_num[1] = 119
                else:
                    if (feature[28]<=0.0):
                        if (feature[34]<=0.0):
                            if (feature[4]<=2704.0):
                                bin_num[1] = 120
                            else:
                                bin_num[1] = 121
                        else:
                            if (feature[29]<=0.0):
                                bin_num[1] = 122
                            else:
                                bin_num[1] = 123
                    else:
                        if (feature[20]<=0.0):
                            if (feature[4]<=2704.0):
                                bin_num[1] = 124
                            else:
                                bin_num[1] = 125
                        else:
                            if (feature[29]<=0.0):
                                bin_num[1] = 126
                            else:
                                bin_num[1] = 127
    # Tree 2
    if (feature[6]<=2.0):
        if (feature[2]<=3.0):
            if (feature[18]<=0.0):
                if (feature[20]<=0.0):
                    if (feature[37]<=0.0):
                        if (feature[25]<=0.0):
                            if (feature[23]<=0.0):
                                bin_num[2] = 0
                            else:
                                bin_num[2] = 1
                        else:
                            if (feature[8]<=35.0):
                                bin_num[2] = 2
                            else:
                                bin_num[2] = 3
                    else:
                        if (feature[8]<=35.0):
                            if (feature[5]<=15.0):
                                bin_num[2] = 4
                            else:
                                bin_num[2] = 5
                        else:
                            if (feature[10]<=1.0):
                                bin_num[2] = 6
                            else:
                                bin_num[2] = 7
                else:
                    if (feature[35]<=0.0):
                        if (feature[4]<=2589.0):
                            if (feature[10]<=1.0):
                                bin_num[2] = 8
                            else:
                                bin_num[2] = 9
                        else:
                            if (feature[25]<=0.0):
                                bin_num[2] = 10
                            else:
                                bin_num[2] = 11
                    else:
                        if (feature[23]<=0.0):
                            if (feature[8]<=35.0):
                                bin_num[2] = 12
                            else:
                                bin_num[2] = 13
                        else:
                            if (feature[25]<=0.0):
                                bin_num[2] = 14
                            else:
                                bin_num[2] = 15
            else:
                if (feature[7]<=7.0):
                    if (feature[20]<=0.0):
                        if (feature[13]<=0.0):
                            if (feature[29]<=0.0):
                                bin_num[2] = 16
                            else:
                                bin_num[2] = 17
                        else:
                            if (feature[8]<=35.0):
                                bin_num[2] = 18
                            else:
                                bin_num[2] = 19
                    else:
                        if (feature[29]<=0.0):
                            if (feature[19]<=0.0):
                                bin_num[2] = 20
                            else:
                                bin_num[2] = 21
                        else:
                            if (feature[34]<=0.0):
                                bin_num[2] = 22
                            else:
                                bin_num[2] = 23
                else:
                    if (feature[20]<=0.0):
                        if (feature[33]<=0.0):
                            if (feature[29]<=0.0):
                                bin_num[2] = 24
                            else:
                                bin_num[2] = 25
                        else:
                            if (feature[1]<=2.0):
                                bin_num[2] = 26
                            else:
                                bin_num[2] = 27
                    else:
                        if (feature[26]<=0.0):
                            if (feature[5]<=15.0):
                                bin_num[2] = 28
                            else:
                                bin_num[2] = 29
                        else:
                            if (feature[13]<=0.0):
                                bin_num[2] = 30
                            else:
                                bin_num[2] = 31
        else:
            if (feature[18]<=0.0):
                if (feature[20]<=0.0):
                    if (feature[35]<=0.0):
                        if (feature[37]<=0.0):
                            if (feature[25]<=0.0):
                                bin_num[2] = 32
                            else:
                                bin_num[2] = 33
                        else:
                            if (feature[8]<=35.0):
                                bin_num[2] = 34
                            else:
                                bin_num[2] = 35
                    else:
                        if (feature[28]<=0.0):
                            if (feature[37]<=0.0):
                                bin_num[2] = 36
                            else:
                                bin_num[2] = 37
                        else:
                            if (feature[37]<=0.0):
                                bin_num[2] = 38
                            else:
                                bin_num[2] = 39
                else:
                    if (feature[29]<=0.0):
                        if (feature[27]<=0.0):
                            if (feature[4]<=2589.0):
                                bin_num[2] = 40
                            else:
                                bin_num[2] = 41
                        else:
                            if (feature[21]<=0.0):
                                bin_num[2] = 42
                            else:
                                bin_num[2] = 43
                    else:
                        if (feature[23]<=0.0):
                            if (feature[35]<=0.0):
                                bin_num[2] = 44
                            else:
                                bin_num[2] = 45
                        else:
                            if (feature[34]<=0.0):
                                bin_num[2] = 46
                            else:
                                bin_num[2] = 47
            else:
                if (feature[8]<=35.0):
                    if (feature[19]<=0.0):
                        if (feature[24]<=0.0):
                            if (feature[29]<=0.0):
                                bin_num[2] = 48
                            else:
                                bin_num[2] = 49
                        else:
                            if (feature[0]<=0.0):
                                bin_num[2] = 50
                            else:
                                bin_num[2] = 51
                    else:
                        if (feature[27]<=0.0):
                            if (feature[29]<=0.0):
                                bin_num[2] = 52
                            else:
                                bin_num[2] = 53
                        else:
                            if (feature[22]<=0.0):
                                bin_num[2] = 54
                            else:
                                bin_num[2] = 55
                else:
                    if (feature[27]<=0.0):
                        if (feature[29]<=0.0):
                            if (feature[24]<=0.0):
                                bin_num[2] = 56
                            else:
                                bin_num[2] = 57
                        else:
                            if (feature[20]<=0.0):
                                bin_num[2] = 58
                            else:
                                bin_num[2] = 59
                    else:
                        if (feature[22]<=0.0):
                            if (feature[5]<=15.0):
                                bin_num[2] = 60
                            else:
                                bin_num[2] = 61
                        else:
                            if (feature[19]<=0.0):
                                bin_num[2] = 62
                            else:
                                bin_num[2] = 63
    else:
        if (feature[20]<=0.0):
            if (feature[27]<=0.0):
                if (feature[29]<=0.0):
                    if (feature[33]<=0.0):
                        if (feature[25]<=0.0):
                            if (feature[23]<=0.0):
                                bin_num[2] = 64
                            else:
                                bin_num[2] = 65
                        else:
                            if (feature[7]<=7.0):
                                bin_num[2] = 66
                            else:
                                bin_num[2] = 67
                    else:
                        if (feature[1]<=2.0):
                            if (feature[26]<=0.0):
                                bin_num[2] = 68
                            else:
                                bin_num[2] = 69
                        else:
                            if (feature[25]<=0.0):
                                bin_num[2] = 70
                            else:
                                bin_num[2] = 71
                else:
                    if (feature[22]<=0.0):
                        if (feature[0]<=0.0):
                            if (feature[18]<=0.0):
                                bin_num[2] = 72
                            else:
                                bin_num[2] = 73
                        else:
                            if (feature[17]<=0.0):
                                bin_num[2] = 74
                            else:
                                bin_num[2] = 75
                    else:
                        if (feature[34]<=0.0):
                            if (feature[18]<=0.0):
                                bin_num[2] = 76
                            else:
                                bin_num[2] = 77
                        else:
                            if (feature[21]<=0.0):
                                bin_num[2] = 78
                            else:
                                bin_num[2] = 79
            else:
                if (feature[28]<=0.0):
                    if (feature[1]<=2.0):
                        if (feature[18]<=0.0):
                            if (feature[19]<=0.0):
                                bin_num[2] = 80
                            else:
                                bin_num[2] = 81
                        else:
                            if (feature[22]<=0.0):
                                bin_num[2] = 82
                            else:
                                bin_num[2] = 83
                    else:
                        if (feature[21]<=0.0):
                            if (feature[22]<=0.0):
                                bin_num[2] = 84
                            else:
                                bin_num[2] = 85
                        else:
                            if (feature[33]<=0.0):
                                bin_num[2] = 86
                            else:
                                bin_num[2] = 87
                else:
                    if (feature[22]<=0.0):
                        if (feature[1]<=2.0):
                            if (feature[37]<=0.0):
                                bin_num[2] = 88
                            else:
                                bin_num[2] = 89
                        else:
                            if (feature[21]<=0.0):
                                bin_num[2] = 90
                            else:
                                bin_num[2] = 91
                    else:
                        if (feature[34]<=0.0):
                            if (feature[21]<=0.0):
                                bin_num[2] = 92
                            else:
                                bin_num[2] = 93
                        else:
                            if (feature[18]<=0.0):
                                bin_num[2] = 94
                            else:
                                bin_num[2] = 95
        else:
            if (feature[18]<=0.0):
                if (feature[35]<=0.0):
                    if (feature[17]<=0.0):
                        if (feature[29]<=0.0):
                            if (feature[23]<=0.0):
                                bin_num[2] = 96
                            else:
                                bin_num[2] = 97
                        else:
                            if (feature[2]<=3.0):
                                bin_num[2] = 98
                            else:
                                bin_num[2] = 99
                    else:
                        if (feature[29]<=0.0):
                            if (feature[19]<=0.0):
                                bin_num[2] = 100
                            else:
                                bin_num[2] = 101
                        else:
                            if (feature[34]<=0.0):
                                bin_num[2] = 102
                            else:
                                bin_num[2] = 103
                else:
                    if (feature[12]<=2.0):
                        if (feature[26]<=0.0):
                            if (feature[24]<=0.0):
                                bin_num[2] = 104
                            else:
                                bin_num[2] = 105
                        else:
                            if (feature[25]<=0.0):
                                bin_num[2] = 106
                            else:
                                bin_num[2] = 107
                    else:
                        if (feature[28]<=0.0):
                            if (feature[17]<=0.0):
                                bin_num[2] = 108
                            else:
                                bin_num[2] = 109
                        else:
                            if (feature[29]<=0.0):
                                bin_num[2] = 110
                            else:
                                bin_num[2] = 111
            else:
                if (feature[29]<=0.0):
                    if (feature[27]<=0.0):
                        if (feature[4]<=2589.0):
                            if (feature[23]<=0.0):
                                bin_num[2] = 112
                            else:
                                bin_num[2] = 113
                        else:
                            if (feature[7]<=7.0):
                                bin_num[2] = 114
                            else:
                                bin_num[2] = 115
                    else:
                        if (feature[19]<=0.0):
                            if (feature[24]<=0.0):
                                bin_num[2] = 116
                            else:
                                bin_num[2] = 117
                        else:
                            if (feature[21]<=0.0):
                                bin_num[2] = 118
                            else:
                                bin_num[2] = 119
                else:
                    if (feature[34]<=0.0):
                        if (feature[1]<=2.0):
                            if (feature[2]<=3.0):
                                bin_num[2] = 120
                            else:
                                bin_num[2] = 121
                        else:
                            if (feature[4]<=2589.0):
                                bin_num[2] = 122
                            else:
                                bin_num[2] = 123
                    else:
                        if (feature[21]<=0.0):
                            if (feature[11]<=0.0):
                                bin_num[2] = 124
                            else:
                                bin_num[2] = 125
                        else:
                            if (feature[19]<=0.0):
                                bin_num[2] = 126
                            else:
                                bin_num[2] = 127
    # Tree 3
    if (feature[6]<=2.0):
        if (feature[2]<=3.0):
            if (feature[7]<=7.0):
                if (feature[18]<=0.0):
                    if (feature[37]<=0.0):
                        if (feature[35]<=0.0):
                            if (feature[23]<=0.0):
                                bin_num[3] = 0
                            else:
                                bin_num[3] = 1
                        else:
                            if (feature[28]<=0.0):
                                bin_num[3] = 2
                            else:
                                bin_num[3] = 3
                    else:
                        if (feature[35]<=0.0):
                            if (feature[26]<=0.0):
                                bin_num[3] = 4
                            else:
                                bin_num[3] = 5
                        else:
                            if (feature[28]<=0.0):
                                bin_num[3] = 6
                            else:
                                bin_num[3] = 7
                else:
                    if (feature[13]<=0.0):
                        if (feature[5]<=15.0):
                            if (feature[24]<=0.0):
                                bin_num[3] = 8
                            else:
                                bin_num[3] = 9
                        else:
                            if (feature[8]<=34.0):
                                bin_num[3] = 10
                            else:
                                bin_num[3] = 11
                    else:
                        if (feature[8]<=34.0):
                            if (feature[11]<=0.0):
                                bin_num[3] = 12
                            else:
                                bin_num[3] = 13
                        else:
                            if (feature[5]<=15.0):
                                bin_num[3] = 14
                            else:
                                bin_num[3] = 15
            else:
                if (feature[4]<=2646.0):
                    if (feature[10]<=1.0):
                        if (feature[29]<=0.0):
                            if (feature[27]<=0.0):
                                bin_num[3] = 16
                            else:
                                bin_num[3] = 17
                        else:
                            if (feature[34]<=0.0):
                                bin_num[3] = 18
                            else:
                                bin_num[3] = 19
                    else:
                        if (feature[8]<=34.0):
                            if (feature[0]<=0.0):
                                bin_num[3] = 20
                            else:
                                bin_num[3] = 21
                        else:
                            if (feature[0]<=0.0):
                                bin_num[3] = 22
                            else:
                                bin_num[3] = 23
                else:
                    if (feature[5]<=15.0):
                        if (feature[12]<=2.0):
                            if (feature[18]<=0.0):
                                bin_num[3] = 24
                            else:
                                bin_num[3] = 25
                        else:
                            if (feature[26]<=0.0):
                                bin_num[3] = 26
                            else:
                                bin_num[3] = 27
                    else:
                        if (feature[8]<=34.0):
                            if (feature[18]<=0.0):
                                bin_num[3] = 28
                            else:
                                bin_num[3] = 29
                        else:
                            if (feature[10]<=1.0):
                                bin_num[3] = 30
                            else:
                                bin_num[3] = 31
        else:
            if (feature[8]<=34.0):
                if (feature[5]<=15.0):
                    if (feature[0]<=0.0):
                        if (feature[34]<=0.0):
                            if (feature[23]<=0.0):
                                bin_num[3] = 32
                            else:
                                bin_num[3] = 33
                        else:
                            if (feature[26]<=0.0):
                                bin_num[3] = 34
                            else:
                                bin_num[3] = 35
                    else:
                        if (feature[17]<=0.0):
                            if (feature[12]<=2.0):
                                bin_num[3] = 36
                            else:
                                bin_num[3] = 37
                        else:
                            if (feature[9]<=0.0):
                                bin_num[3] = 38
                            else:
                                bin_num[3] = 39
                else:
                    if (feature[29]<=0.0):
                        if (feature[27]<=0.0):
                            if (feature[18]<=0.0):
                                bin_num[3] = 40
                            else:
                                bin_num[3] = 41
                        else:
                            if (feature[22]<=0.0):
                                bin_num[3] = 42
                            else:
                                bin_num[3] = 43
                    else:
                        if (feature[20]<=0.0):
                            if (feature[22]<=0.0):
                                bin_num[3] = 44
                            else:
                                bin_num[3] = 45
                        else:
                            if (feature[1]<=3.0):
                                bin_num[3] = 46
                            else:
                                bin_num[3] = 47
            else:
                if (feature[5]<=15.0):
                    if (feature[4]<=2646.0):
                        if (feature[10]<=1.0):
                            if (feature[9]<=0.0):
                                bin_num[3] = 48
                            else:
                                bin_num[3] = 49
                        else:
                            if (feature[18]<=0.0):
                                bin_num[3] = 50
                            else:
                                bin_num[3] = 51
                    else:
                        if (feature[29]<=0.0):
                            if (feature[27]<=0.0):
                                bin_num[3] = 52
                            else:
                                bin_num[3] = 53
                        else:
                            if (feature[20]<=0.0):
                                bin_num[3] = 54
                            else:
                                bin_num[3] = 55
                else:
                    if (feature[20]<=0.0):
                        if (feature[18]<=0.0):
                            if (feature[37]<=0.0):
                                bin_num[3] = 56
                            else:
                                bin_num[3] = 57
                        else:
                            if (feature[24]<=0.0):
                                bin_num[3] = 58
                            else:
                                bin_num[3] = 59
                    else:
                        if (feature[29]<=0.0):
                            if (feature[27]<=0.0):
                                bin_num[3] = 60
                            else:
                                bin_num[3] = 61
                        else:
                            if (feature[1]<=3.0):
                                bin_num[3] = 62
                            else:
                                bin_num[3] = 63
    else:
        if (feature[35]<=0.0):
            if (feature[18]<=0.0):
                if (feature[20]<=0.0):
                    if (feature[27]<=0.0):
                        if (feature[29]<=0.0):
                            if (feature[4]<=2646.0):
                                bin_num[3] = 64
                            else:
                                bin_num[3] = 65
                        else:
                            if (feature[22]<=0.0):
                                bin_num[3] = 66
                            else:
                                bin_num[3] = 67
                    else:
                        if (feature[28]<=0.0):
                            if (feature[33]<=0.0):
                                bin_num[3] = 68
                            else:
                                bin_num[3] = 69
                        else:
                            if (feature[21]<=0.0):
                                bin_num[3] = 70
                            else:
                                bin_num[3] = 71
                else:
                    if (feature[17]<=0.0):
                        if (feature[2]<=3.0):
                            if (feature[19]<=0.0):
                                bin_num[3] = 72
                            else:
                                bin_num[3] = 73
                        else:
                            if (feature[29]<=0.0):
                                bin_num[3] = 74
                            else:
                                bin_num[3] = 75
                    else:
                        if (feature[12]<=2.0):
                            if (feature[26]<=0.0):
                                bin_num[3] = 76
                            else:
                                bin_num[3] = 77
                        else:
                            if (feature[1]<=3.0):
                                bin_num[3] = 78
                            else:
                                bin_num[3] = 79
            else:
                if (feature[23]<=0.0):
                    if (feature[17]<=0.0):
                        if (feature[27]<=0.0):
                            if (feature[29]<=0.0):
                                bin_num[3] = 80
                            else:
                                bin_num[3] = 81
                        else:
                            if (feature[22]<=0.0):
                                bin_num[3] = 82
                            else:
                                bin_num[3] = 83
                    else:
                        if (feature[29]<=0.0):
                            if (feature[19]<=0.0):
                                bin_num[3] = 84
                            else:
                                bin_num[3] = 85
                        else:
                            if (feature[20]<=0.0):
                                bin_num[3] = 86
                            else:
                                bin_num[3] = 87
                else:
                    if (feature[11]<=0.0):
                        if (feature[17]<=0.0):
                            if (feature[20]<=0.0):
                                bin_num[3] = 88
                            else:
                                bin_num[3] = 89
                        else:
                            if (feature[20]<=0.0):
                                bin_num[3] = 90
                            else:
                                bin_num[3] = 91
                    else:
                        if (feature[34]<=0.0):
                            if (feature[21]<=0.0):
                                bin_num[3] = 92
                            else:
                                bin_num[3] = 93
                        else:
                            if (feature[26]<=0.0):
                                bin_num[3] = 94
                            else:
                                bin_num[3] = 95
        else:
            if (feature[20]<=0.0):
                if (feature[28]<=0.0):
                    if (feature[2]<=3.0):
                        if (feature[23]<=0.0):
                            if (feature[27]<=0.0):
                                bin_num[3] = 96
                            else:
                                bin_num[3] = 97
                        else:
                            if (feature[11]<=0.0):
                                bin_num[3] = 98
                            else:
                                bin_num[3] = 99
                    else:
                        if (feature[5]<=15.0):
                            if (feature[33]<=0.0):
                                bin_num[3] = 100
                            else:
                                bin_num[3] = 101
                        else:
                            if (feature[10]<=1.0):
                                bin_num[3] = 102
                            else:
                                bin_num[3] = 103
                else:
                    if (feature[37]<=0.0):
                        if (feature[5]<=15.0):
                            if (feature[27]<=0.0):
                                bin_num[3] = 104
                            else:
                                bin_num[3] = 105
                        else:
                            if (feature[34]<=0.0):
                                bin_num[3] = 106
                            else:
                                bin_num[3] = 107
                    else:
                        if (feature[33]<=0.0):
                            if (feature[34]<=0.0):
                                bin_num[3] = 108
                            else:
                                bin_num[3] = 109
                        else:
                            if (feature[36]<=0.0):
                                bin_num[3] = 110
                            else:
                                bin_num[3] = 111
            else:
                if (feature[2]<=3.0):
                    if (feature[26]<=0.0):
                        if (feature[34]<=0.0):
                            if (feature[18]<=0.0):
                                bin_num[3] = 112
                            else:
                                bin_num[3] = 113
                        else:
                            if (feature[27]<=0.0):
                                bin_num[3] = 114
                            else:
                                bin_num[3] = 115
                    else:
                        if (feature[34]<=0.0):
                            if (feature[1]<=3.0):
                                bin_num[3] = 116
                            else:
                                bin_num[3] = 117
                        else:
                            if (feature[25]<=0.0):
                                bin_num[3] = 118
                            else:
                                bin_num[3] = 119
                else:
                    if (feature[5]<=15.0):
                        if (feature[25]<=0.0):
                            if (feature[17]<=0.0):
                                bin_num[3] = 120
                            else:
                                bin_num[3] = 121
                        else:
                            if (feature[29]<=0.0):
                                bin_num[3] = 122
                            else:
                                bin_num[3] = 123
                    else:
                        if (feature[18]<=0.0):
                            if (feature[28]<=0.0):
                                bin_num[3] = 124
                            else:
                                bin_num[3] = 125
                        else:
                            if (feature[34]<=0.0):
                                bin_num[3] = 126
                            else:
                                bin_num[3] = 127
    # Tree 4
    if (feature[6]<=3.0):
        if (feature[2]<=3.0):
            if (feature[8]<=35.0):
                if (feature[20]<=0.0):
                    if (feature[18]<=0.0):
                        if (feature[35]<=0.0):
                            if (feature[23]<=0.0):
                                bin_num[4] = 0
                            else:
                                bin_num[4] = 1
                        else:
                            if (feature[28]<=0.0):
                                bin_num[4] = 2
                            else:
                                bin_num[4] = 3
                    else:
                        if (feature[29]<=0.0):
                            if (feature[33]<=0.0):
                                bin_num[4] = 4
                            else:
                                bin_num[4] = 5
                        else:
                            if (feature[22]<=0.0):
                                bin_num[4] = 6
                            else:
                                bin_num[4] = 7
                else:
                    if (feature[18]<=0.0):
                        if (feature[0]<=0.0):
                            if (feature[23]<=0.0):
                                bin_num[4] = 8
                            else:
                                bin_num[4] = 9
                        else:
                            if (feature[10]<=1.0):
                                bin_num[4] = 10
                            else:
                                bin_num[4] = 11
                    else:
                        if (feature[29]<=0.0):
                            if (feature[19]<=0.0):
                                bin_num[4] = 12
                            else:
                                bin_num[4] = 13
                        else:
                            if (feature[34]<=0.0):
                                bin_num[4] = 14
                            else:
                                bin_num[4] = 15
            else:
                if (feature[10]<=1.0):
                    if (feature[5]<=16.0):
                        if (feature[4]<=2626.0):
                            if (feature[20]<=0.0):
                                bin_num[4] = 16
                            else:
                                bin_num[4] = 17
                        else:
                            if (feature[13]<=0.0):
                                bin_num[4] = 18
                            else:
                                bin_num[4] = 19
                    else:
                        if (feature[26]<=0.0):
                            if (feature[20]<=0.0):
                                bin_num[4] = 20
                            else:
                                bin_num[4] = 21
                        else:
                            if (feature[13]<=0.0):
                                bin_num[4] = 22
                            else:
                                bin_num[4] = 23
                else:
                    if (feature[0]<=0.0):
                        if (feature[7]<=7.0):
                            if (feature[29]<=0.0):
                                bin_num[4] = 24
                            else:
                                bin_num[4] = 25
                        else:
                            if (feature[4]<=2626.0):
                                bin_num[4] = 26
                            else:
                                bin_num[4] = 27
                    else:
                        if (feature[18]<=0.0):
                            if (feature[12]<=2.0):
                                bin_num[4] = 28
                            else:
                                bin_num[4] = 29
                        else:
                            if (feature[20]<=0.0):
                                bin_num[4] = 30
                            else:
                                bin_num[4] = 31
        else:
            if (feature[8]<=35.0):
                if (feature[18]<=0.0):
                    if (feature[23]<=0.0):
                        if (feature[37]<=0.0):
                            if (feature[4]<=2626.0):
                                bin_num[4] = 32
                            else:
                                bin_num[4] = 33
                        else:
                            if (feature[35]<=0.0):
                                bin_num[4] = 34
                            else:
                                bin_num[4] = 35
                    else:
                        if (feature[25]<=0.0):
                            if (feature[37]<=0.0):
                                bin_num[4] = 36
                            else:
                                bin_num[4] = 37
                        else:
                            if (feature[0]<=0.0):
                                bin_num[4] = 38
                            else:
                                bin_num[4] = 39
                else:
                    if (feature[20]<=0.0):
                        if (feature[34]<=0.0):
                            if (feature[33]<=0.0):
                                bin_num[4] = 40
                            else:
                                bin_num[4] = 41
                        else:
                            if (feature[26]<=0.0):
                                bin_num[4] = 42
                            else:
                                bin_num[4] = 43
                    else:
                        if (feature[29]<=0.0):
                            if (feature[27]<=0.0):
                                bin_num[4] = 44
                            else:
                                bin_num[4] = 45
                        else:
                            if (feature[1]<=3.0):
                                bin_num[4] = 46
                            else:
                                bin_num[4] = 47
            else:
                if (feature[18]<=0.0):
                    if (feature[10]<=1.0):
                        if (feature[37]<=0.0):
                            if (feature[4]<=2626.0):
                                bin_num[4] = 48
                            else:
                                bin_num[4] = 49
                        else:
                            if (feature[5]<=16.0):
                                bin_num[4] = 50
                            else:
                                bin_num[4] = 51
                    else:
                        if (feature[9]<=0.0):
                            if (feature[29]<=0.0):
                                bin_num[4] = 52
                            else:
                                bin_num[4] = 53
                        else:
                            if (feature[3]<=2.0):
                                bin_num[4] = 54
                            else:
                                bin_num[4] = 55
                else:
                    if (feature[19]<=0.0):
                        if (feature[24]<=0.0):
                            if (feature[29]<=0.0):
                                bin_num[4] = 56
                            else:
                                bin_num[4] = 57
                        else:
                            if (feature[17]<=0.0):
                                bin_num[4] = 58
                            else:
                                bin_num[4] = 59
                    else:
                        if (feature[27]<=0.0):
                            if (feature[29]<=0.0):
                                bin_num[4] = 60
                            else:
                                bin_num[4] = 61
                        else:
                            if (feature[20]<=0.0):
                                bin_num[4] = 62
                            else:
                                bin_num[4] = 63
    else:
        if (feature[5]<=16.0):
            if (feature[25]<=0.0):
                if (feature[23]<=0.0):
                    if (feature[17]<=0.0):
                        if (feature[0]<=0.0):
                            if (feature[29]<=0.0):
                                bin_num[4] = 64
                            else:
                                bin_num[4] = 65
                        else:
                            if (feature[27]<=0.0):
                                bin_num[4] = 66
                            else:
                                bin_num[4] = 67
                    else:
                        if (feature[35]<=0.0):
                            if (feature[1]<=3.0):
                                bin_num[4] = 68
                            else:
                                bin_num[4] = 69
                        else:
                            if (feature[11]<=0.0):
                                bin_num[4] = 70
                            else:
                                bin_num[4] = 71
                else:
                    if (feature[11]<=0.0):
                        if (feature[37]<=0.0):
                            if (feature[18]<=0.0):
                                bin_num[4] = 72
                            else:
                                bin_num[4] = 73
                        else:
                            if (feature[29]<=0.0):
                                bin_num[4] = 74
                            else:
                                bin_num[4] = 75
                    else:
                        if (feature[18]<=0.0):
                            if (feature[29]<=0.0):
                                bin_num[4] = 76
                            else:
                                bin_num[4] = 77
                        else:
                            if (feature[34]<=0.0):
                                bin_num[4] = 78
                            else:
                                bin_num[4] = 79
            else:
                if (feature[17]<=0.0):
                    if (feature[23]<=0.0):
                        if (feature[0]<=0.0):
                            if (feature[35]<=0.0):
                                bin_num[4] = 80
                            else:
                                bin_num[4] = 81
                        else:
                            if (feature[10]<=1.0):
                                bin_num[4] = 82
                            else:
                                bin_num[4] = 83
                    else:
                        if (feature[11]<=0.0):
                            if (feature[19]<=0.0):
                                bin_num[4] = 84
                            else:
                                bin_num[4] = 85
                        else:
                            if (feature[1]<=3.0):
                                bin_num[4] = 86
                            else:
                                bin_num[4] = 87
                else:
                    if (feature[20]<=0.0):
                        if (feature[33]<=0.0):
                            if (feature[22]<=0.0):
                                bin_num[4] = 88
                            else:
                                bin_num[4] = 89
                        else:
                            if (feature[1]<=3.0):
                                bin_num[4] = 90
                            else:
                                bin_num[4] = 91
                    else:
                        if (feature[29]<=0.0):
                            if (feature[10]<=1.0):
                                bin_num[4] = 92
                            else:
                                bin_num[4] = 93
                        else:
                            if (feature[34]<=0.0):
                                bin_num[4] = 94
                            else:
                                bin_num[4] = 95
        else:
            if (feature[7]<=7.0):
                if (feature[2]<=3.0):
                    if (feature[26]<=0.0):
                        if (feature[4]<=2626.0):
                            if (feature[34]<=0.0):
                                bin_num[4] = 96
                            else:
                                bin_num[4] = 97
                        else:
                            if (feature[8]<=35.0):
                                bin_num[4] = 98
                            else:
                                bin_num[4] = 99
                    else:
                        if (feature[37]<=0.0):
                            if (feature[4]<=2626.0):
                                bin_num[4] = 100
                            else:
                                bin_num[4] = 101
                        else:
                            if (feature[19]<=0.0):
                                bin_num[4] = 102
                            else:
                                bin_num[4] = 103
                else:
                    if (feature[4]<=2626.0):
                        if (feature[27]<=0.0):
                            if (feature[29]<=0.0):
                                bin_num[4] = 104
                            else:
                                bin_num[4] = 105
                        else:
                            if (feature[28]<=0.0):
                                bin_num[4] = 106
                            else:
                                bin_num[4] = 107
                    else:
                        if (feature[10]<=1.0):
                            if (feature[20]<=0.0):
                                bin_num[4] = 108
                            else:
                                bin_num[4] = 109
                        else:
                            if (feature[18]<=0.0):
                                bin_num[4] = 110
                            else:
                                bin_num[4] = 111
            else:
                if (feature[4]<=2626.0):
                    if (feature[34]<=0.0):
                        if (feature[27]<=0.0):
                            if (feature[29]<=0.0):
                                bin_num[4] = 112
                            else:
                                bin_num[4] = 113
                        else:
                            if (feature[28]<=0.0):
                                bin_num[4] = 114
                            else:
                                bin_num[4] = 115
                    else:
                        if (feature[26]<=0.0):
                            if (feature[33]<=0.0):
                                bin_num[4] = 116
                            else:
                                bin_num[4] = 117
                        else:
                            if (feature[2]<=3.0):
                                bin_num[4] = 118
                            else:
                                bin_num[4] = 119
                else:
                    if (feature[18]<=0.0):
                        if (feature[37]<=0.0):
                            if (feature[35]<=0.0):
                                bin_num[4] = 120
                            else:
                                bin_num[4] = 121
                        else:
                            if (feature[35]<=0.0):
                                bin_num[4] = 122
                            else:
                                bin_num[4] = 123
                    else:
                        if (feature[19]<=0.0):
                            if (feature[24]<=0.0):
                                bin_num[4] = 124
                            else:
                                bin_num[4] = 125
                        else:
                            if (feature[35]<=0.0):
                                bin_num[4] = 126
                            else:
                                bin_num[4] = 127
    # Tree 5
    if (feature[6]<=2.0):
        if (feature[2]<=3.0):
            if (feature[7]<=7.0):
                if (feature[13]<=0.0):
                    if (feature[5]<=15.0):
                        if (feature[29]<=0.0):
                            if (feature[17]<=0.0):
                                bin_num[5] = 0
                            else:
                                bin_num[5] = 1
                        else:
                            if (feature[8]<=34.0):
                                bin_num[5] = 2
                            else:
                                bin_num[5] = 3
                    else:
                        if (feature[8]<=34.0):
                            if (feature[23]<=0.0):
                                bin_num[5] = 4
                            else:
                                bin_num[5] = 5
                        else:
                            if (feature[29]<=0.0):
                                bin_num[5] = 6
                            else:
                                bin_num[5] = 7
                else:
                    if (feature[20]<=0.0):
                        if (feature[33]<=0.0):
                            if (feature[29]<=0.0):
                                bin_num[5] = 8
                            else:
                                bin_num[5] = 9
                        else:
                            if (feature[26]<=0.0):
                                bin_num[5] = 10
                            else:
                                bin_num[5] = 11
                    else:
                        if (feature[4]<=2642.0):
                            if (feature[26]<=0.0):
                                bin_num[5] = 12
                            else:
                                bin_num[5] = 13
                        else:
                            if (feature[18]<=0.0):
                                bin_num[5] = 14
                            else:
                                bin_num[5] = 15
            else:
                if (feature[4]<=2642.0):
                    if (feature[18]<=0.0):
                        if (feature[37]<=0.0):
                            if (feature[29]<=0.0):
                                bin_num[5] = 16
                            else:
                                bin_num[5] = 17
                        else:
                            if (feature[10]<=1.0):
                                bin_num[5] = 18
                            else:
                                bin_num[5] = 19
                    else:
                        if (feature[29]<=0.0):
                            if (feature[27]<=0.0):
                                bin_num[5] = 20
                            else:
                                bin_num[5] = 21
                        else:
                            if (feature[20]<=0.0):
                                bin_num[5] = 22
                            else:
                                bin_num[5] = 23
                else:
                    if (feature[5]<=15.0):
                        if (feature[12]<=2.0):
                            if (feature[18]<=0.0):
                                bin_num[5] = 24
                            else:
                                bin_num[5] = 25
                        else:
                            if (feature[26]<=0.0):
                                bin_num[5] = 26
                            else:
                                bin_num[5] = 27
                    else:
                        if (feature[8]<=34.0):
                            if (feature[12]<=2.0):
                                bin_num[5] = 28
                            else:
                                bin_num[5] = 29
                        else:
                            if (feature[18]<=0.0):
                                bin_num[5] = 30
                            else:
                                bin_num[5] = 31
        else:
            if (feature[20]<=0.0):
                if (feature[18]<=0.0):
                    if (feature[35]<=0.0):
                        if (feature[29]<=0.0):
                            if (feature[27]<=0.0):
                                bin_num[5] = 32
                            else:
                                bin_num[5] = 33
                        else:
                            if (feature[22]<=0.0):
                                bin_num[5] = 34
                            else:
                                bin_num[5] = 35
                    else:
                        if (feature[28]<=0.0):
                            if (feature[4]<=2642.0):
                                bin_num[5] = 36
                            else:
                                bin_num[5] = 37
                        else:
                            if (feature[34]<=0.0):
                                bin_num[5] = 38
                            else:
                                bin_num[5] = 39
                else:
                    if (feature[8]<=34.0):
                        if (feature[19]<=0.0):
                            if (feature[24]<=0.0):
                                bin_num[5] = 40
                            else:
                                bin_num[5] = 41
                        else:
                            if (feature[5]<=15.0):
                                bin_num[5] = 42
                            else:
                                bin_num[5] = 43
                    else:
                        if (feature[5]<=15.0):
                            if (feature[9]<=0.0):
                                bin_num[5] = 44
                            else:
                                bin_num[5] = 45
                        else:
                            if (feature[19]<=0.0):
                                bin_num[5] = 46
                            else:
                                bin_num[5] = 47
            else:
                if (feature[29]<=0.0):
                    if (feature[18]<=0.0):
                        if (feature[4]<=2642.0):
                            if (feature[13]<=0.0):
                                bin_num[5] = 48
                            else:
                                bin_num[5] = 49
                        else:
                            if (feature[27]<=0.0):
                                bin_num[5] = 50
                            else:
                                bin_num[5] = 51
                    else:
                        if (feature[27]<=0.0):
                            if (feature[4]<=2642.0):
                                bin_num[5] = 52
                            else:
                                bin_num[5] = 53
                        else:
                            if (feature[21]<=0.0):
                                bin_num[5] = 54
                            else:
                                bin_num[5] = 55
                else:
                    if (feature[1]<=2.0):
                        if (feature[34]<=0.0):
                            if (feature[35]<=0.0):
                                bin_num[5] = 56
                            else:
                                bin_num[5] = 57
                        else:
                            if (feature[12]<=2.0):
                                bin_num[5] = 58
                            else:
                                bin_num[5] = 59
                    else:
                        if (feature[4]<=2642.0):
                            if (feature[7]<=7.0):
                                bin_num[5] = 60
                            else:
                                bin_num[5] = 61
                        else:
                            if (feature[24]<=0.0):
                                bin_num[5] = 62
                            else:
                                bin_num[5] = 63
    else:
        if (feature[20]<=0.0):
            if (feature[27]<=0.0):
                if (feature[29]<=0.0):
                    if (feature[33]<=0.0):
                        if (feature[35]<=0.0):
                            if (feature[18]<=0.0):
                                bin_num[5] = 64
                            else:
                                bin_num[5] = 65
                        else:
                            if (feature[23]<=0.0):
                                bin_num[5] = 66
                            else:
                                bin_num[5] = 67
                    else:
                        if (feature[19]<=0.0):
                            if (feature[21]<=0.0):
                                bin_num[5] = 68
                            else:
                                bin_num[5] = 69
                        else:
                            if (feature[12]<=2.0):
                                bin_num[5] = 70
                            else:
                                bin_num[5] = 71
                else:
                    if (feature[22]<=0.0):
                        if (feature[0]<=0.0):
                            if (feature[28]<=0.0):
                                bin_num[5] = 72
                            else:
                                bin_num[5] = 73
                        else:
                            if (feature[17]<=0.0):
                                bin_num[5] = 74
                            else:
                                bin_num[5] = 75
                    else:
                        if (feature[34]<=0.0):
                            if (feature[18]<=0.0):
                                bin_num[5] = 76
                            else:
                                bin_num[5] = 77
                        else:
                            if (feature[21]<=0.0):
                                bin_num[5] = 78
                            else:
                                bin_num[5] = 79
            else:
                if (feature[21]<=0.0):
                    if (feature[22]<=0.0):
                        if (feature[33]<=0.0):
                            if (feature[37]<=0.0):
                                bin_num[5] = 80
                            else:
                                bin_num[5] = 81
                        else:
                            if (feature[9]<=0.0):
                                bin_num[5] = 82
                            else:
                                bin_num[5] = 83
                    else:
                        if (feature[0]<=0.0):
                            if (feature[18]<=0.0):
                                bin_num[5] = 84
                            else:
                                bin_num[5] = 85
                        else:
                            if (feature[18]<=0.0):
                                bin_num[5] = 86
                            else:
                                bin_num[5] = 87
                else:
                    if (feature[1]<=2.0):
                        if (feature[22]<=0.0):
                            if (feature[37]<=0.0):
                                bin_num[5] = 88
                            else:
                                bin_num[5] = 89
                        else:
                            if (feature[28]<=0.0):
                                bin_num[5] = 90
                            else:
                                bin_num[5] = 91
                    else:
                        if (feature[33]<=0.0):
                            if (feature[18]<=0.0):
                                bin_num[5] = 92
                            else:
                                bin_num[5] = 93
                        else:
                            if (feature[0]<=0.0):
                                bin_num[5] = 94
                            else:
                                bin_num[5] = 95
        else:
            if (feature[29]<=0.0):
                if (feature[18]<=0.0):
                    if (feature[35]<=0.0):
                        if (feature[19]<=0.0):
                            if (feature[24]<=0.0):
                                bin_num[5] = 96
                            else:
                                bin_num[5] = 97
                        else:
                            if (feature[27]<=0.0):
                                bin_num[5] = 98
                            else:
                                bin_num[5] = 99
                    else:
                        if (feature[12]<=2.0):
                            if (feature[26]<=0.0):
                                bin_num[5] = 100
                            else:
                                bin_num[5] = 101
                        else:
                            if (feature[28]<=0.0):
                                bin_num[5] = 102
                            else:
                                bin_num[5] = 103
                else:
                    if (feature[27]<=0.0):
                        if (feature[4]<=2642.0):
                            if (feature[17]<=0.0):
                                bin_num[5] = 104
                            else:
                                bin_num[5] = 105
                        else:
                            if (feature[7]<=7.0):
                                bin_num[5] = 106
                            else:
                                bin_num[5] = 107
                    else:
                        if (feature[19]<=0.0):
                            if (feature[24]<=0.0):
                                bin_num[5] = 108
                            else:
                                bin_num[5] = 109
                        else:
                            if (feature[21]<=0.0):
                                bin_num[5] = 110
                            else:
                                bin_num[5] = 111
            else:
                if (feature[34]<=0.0):
                    if (feature[2]<=3.0):
                        if (feature[17]<=0.0):
                            if (feature[35]<=0.0):
                                bin_num[5] = 112
                            else:
                                bin_num[5] = 113
                        else:
                            if (feature[0]<=0.0):
                                bin_num[5] = 114
                            else:
                                bin_num[5] = 115
                    else:
                        if (feature[1]<=2.0):
                            if (feature[17]<=0.0):
                                bin_num[5] = 116
                            else:
                                bin_num[5] = 117
                        else:
                            if (feature[5]<=15.0):
                                bin_num[5] = 118
                            else:
                                bin_num[5] = 119
                else:
                    if (feature[21]<=0.0):
                        if (feature[18]<=0.0):
                            if (feature[1]<=2.0):
                                bin_num[5] = 120
                            else:
                                bin_num[5] = 121
                        else:
                            if (feature[11]<=0.0):
                                bin_num[5] = 122
                            else:
                                bin_num[5] = 123
                    else:
                        if (feature[18]<=0.0):
                            if (feature[37]<=0.0):
                                bin_num[5] = 124
                            else:
                                bin_num[5] = 125
                        else:
                            if (feature[24]<=0.0):
                                bin_num[5] = 126
                            else:
                                bin_num[5] = 127
    # Tree 6
    if (feature[6]<=2.0):
        if (feature[7]<=7.0):
            if (feature[18]<=0.0):
                if (feature[37]<=0.0):
                    if (feature[25]<=0.0):
                        if (feature[23]<=0.0):
                            if (feature[2]<=3.0):
                                bin_num[6] = 0
                            else:
                                bin_num[6] = 1
                        else:
                            if (feature[4]<=2628.0):
                                bin_num[6] = 2
                            else:
                                bin_num[6] = 3
                    else:
                        if (feature[35]<=0.0):
                            if (feature[34]<=0.0):
                                bin_num[6] = 4
                            else:
                                bin_num[6] = 5
                        else:
                            if (feature[28]<=0.0):
                                bin_num[6] = 6
                            else:
                                bin_num[6] = 7
                else:
                    if (feature[21]<=0.0):
                        if (feature[29]<=0.0):
                            if (feature[17]<=0.0):
                                bin_num[6] = 8
                            else:
                                bin_num[6] = 9
                        else:
                            if (feature[28]<=0.0):
                                bin_num[6] = 10
                            else:
                                bin_num[6] = 11
                    else:
                        if (feature[28]<=0.0):
                            if (feature[26]<=0.0):
                                bin_num[6] = 12
                            else:
                                bin_num[6] = 13
                        else:
                            if (feature[34]<=0.0):
                                bin_num[6] = 14
                            else:
                                bin_num[6] = 15
            else:
                if (feature[19]<=0.0):
                    if (feature[24]<=0.0):
                        if (feature[29]<=0.0):
                            if (feature[22]<=0.0):
                                bin_num[6] = 16
                            else:
                                bin_num[6] = 17
                        else:
                            if (feature[20]<=0.0):
                                bin_num[6] = 18
                            else:
                                bin_num[6] = 19
                    else:
                        if (feature[13]<=0.0):
                            if (feature[4]<=2628.0):
                                bin_num[6] = 20
                            else:
                                bin_num[6] = 21
                        else:
                            if (feature[29]<=0.0):
                                bin_num[6] = 22
                            else:
                                bin_num[6] = 23
                else:
                    if (feature[11]<=0.0):
                        if (feature[27]<=0.0):
                            if (feature[35]<=0.0):
                                bin_num[6] = 24
                            else:
                                bin_num[6] = 25
                        else:
                            if (feature[22]<=0.0):
                                bin_num[6] = 26
                            else:
                                bin_num[6] = 27
                    else:
                        if (feature[23]<=0.0):
                            if (feature[0]<=0.0):
                                bin_num[6] = 28
                            else:
                                bin_num[6] = 29
                        else:
                            if (feature[21]<=0.0):
                                bin_num[6] = 30
                            else:
                                bin_num[6] = 31
        else:
            if (feature[4]<=2628.0):
                if (feature[17]<=0.0):
                    if (feature[20]<=0.0):
                        if (feature[29]<=0.0):
                            if (feature[27]<=0.0):
                                bin_num[6] = 32
                            else:
                                bin_num[6] = 33
                        else:
                            if (feature[22]<=0.0):
                                bin_num[6] = 34
                            else:
                                bin_num[6] = 35
                    else:
                        if (feature[27]<=0.0):
                            if (feature[29]<=0.0):
                                bin_num[6] = 36
                            else:
                                bin_num[6] = 37
                        else:
                            if (feature[21]<=0.0):
                                bin_num[6] = 38
                            else:
                                bin_num[6] = 39
                else:
                    if (feature[8]<=35.0):
                        if (feature[29]<=0.0):
                            if (feature[25]<=0.0):
                                bin_num[6] = 40
                            else:
                                bin_num[6] = 41
                        else:
                            if (feature[20]<=0.0):
                                bin_num[6] = 42
                            else:
                                bin_num[6] = 43
                    else:
                        if (feature[27]<=0.0):
                            if (feature[29]<=0.0):
                                bin_num[6] = 44
                            else:
                                bin_num[6] = 45
                        else:
                            if (feature[28]<=0.0):
                                bin_num[6] = 46
                            else:
                                bin_num[6] = 47
            else:
                if (feature[5]<=15.0):
                    if (feature[13]<=0.0):
                        if (feature[27]<=0.0):
                            if (feature[29]<=0.0):
                                bin_num[6] = 48
                            else:
                                bin_num[6] = 49
                        else:
                            if (feature[22]<=0.0):
                                bin_num[6] = 50
                            else:
                                bin_num[6] = 51
                    else:
                        if (feature[12]<=2.0):
                            if (feature[18]<=0.0):
                                bin_num[6] = 52
                            else:
                                bin_num[6] = 53
                        else:
                            if (feature[8]<=35.0):
                                bin_num[6] = 54
                            else:
                                bin_num[6] = 55
                else:
                    if (feature[8]<=35.0):
                        if (feature[29]<=0.0):
                            if (feature[27]<=0.0):
                                bin_num[6] = 56
                            else:
                                bin_num[6] = 57
                        else:
                            if (feature[12]<=2.0):
                                bin_num[6] = 58
                            else:
                                bin_num[6] = 59
                    else:
                        if (feature[18]<=0.0):
                            if (feature[37]<=0.0):
                                bin_num[6] = 60
                            else:
                                bin_num[6] = 61
                        else:
                            if (feature[19]<=0.0):
                                bin_num[6] = 62
                            else:
                                bin_num[6] = 63
    else:
        if (feature[25]<=0.0):
            if (feature[5]<=15.0):
                if (feature[17]<=0.0):
                    if (feature[23]<=0.0):
                        if (feature[0]<=0.0):
                            if (feature[29]<=0.0):
                                bin_num[6] = 64
                            else:
                                bin_num[6] = 65
                        else:
                            if (feature[38]<=0.0):
                                bin_num[6] = 66
                            else:
                                bin_num[6] = 67
                    else:
                        if (feature[11]<=0.0):
                            if (feature[37]<=0.0):
                                bin_num[6] = 68
                            else:
                                bin_num[6] = 69
                        else:
                            if (feature[18]<=0.0):
                                bin_num[6] = 70
                            else:
                                bin_num[6] = 71
                else:
                    if (feature[11]<=0.0):
                        if (feature[29]<=0.0):
                            if (feature[27]<=0.0):
                                bin_num[6] = 72
                            else:
                                bin_num[6] = 73
                        else:
                            if (feature[9]<=0.0):
                                bin_num[6] = 74
                            else:
                                bin_num[6] = 75
                    else:
                        if (feature[34]<=0.0):
                            if (feature[33]<=0.0):
                                bin_num[6] = 76
                            else:
                                bin_num[6] = 77
                        else:
                            if (feature[18]<=0.0):
                                bin_num[6] = 78
                            else:
                                bin_num[6] = 79
            else:
                if (feature[7]<=7.0):
                    if (feature[2]<=3.0):
                        if (feature[4]<=2628.0):
                            if (feature[9]<=0.0):
                                bin_num[6] = 80
                            else:
                                bin_num[6] = 81
                        else:
                            if (feature[37]<=0.0):
                                bin_num[6] = 82
                            else:
                                bin_num[6] = 83
                    else:
                        if (feature[4]<=2628.0):
                            if (feature[20]<=0.0):
                                bin_num[6] = 84
                            else:
                                bin_num[6] = 85
                        else:
                            if (feature[20]<=0.0):
                                bin_num[6] = 86
                            else:
                                bin_num[6] = 87
                else:
                    if (feature[4]<=2628.0):
                        if (feature[34]<=0.0):
                            if (feature[23]<=0.0):
                                bin_num[6] = 88
                            else:
                                bin_num[6] = 89
                        else:
                            if (feature[26]<=0.0):
                                bin_num[6] = 90
                            else:
                                bin_num[6] = 91
                    else:
                        if (feature[26]<=0.0):
                            if (feature[8]<=35.0):
                                bin_num[6] = 92
                            else:
                                bin_num[6] = 93
                        else:
                            if (feature[2]<=3.0):
                                bin_num[6] = 94
                            else:
                                bin_num[6] = 95
        else:
            if (feature[7]<=7.0):
                if (feature[19]<=0.0):
                    if (feature[35]<=0.0):
                        if (feature[24]<=0.0):
                            if (feature[28]<=0.0):
                                bin_num[6] = 96
                            else:
                                bin_num[6] = 97
                        else:
                            if (feature[2]<=3.0):
                                bin_num[6] = 98
                            else:
                                bin_num[6] = 99
                    else:
                        if (feature[28]<=0.0):
                            if (feature[34]<=0.0):
                                bin_num[6] = 100
                            else:
                                bin_num[6] = 101
                        else:
                            if (feature[23]<=0.0):
                                bin_num[6] = 102
                            else:
                                bin_num[6] = 103
                else:
                    if (feature[23]<=0.0):
                        if (feature[2]<=3.0):
                            if (feature[17]<=0.0):
                                bin_num[6] = 104
                            else:
                                bin_num[6] = 105
                        else:
                            if (feature[21]<=0.0):
                                bin_num[6] = 106
                            else:
                                bin_num[6] = 107
                    else:
                        if (feature[2]<=3.0):
                            if (feature[8]<=35.0):
                                bin_num[6] = 108
                            else:
                                bin_num[6] = 109
                        else:
                            if (feature[29]<=0.0):
                                bin_num[6] = 110
                            else:
                                bin_num[6] = 111
            else:
                if (feature[17]<=0.0):
                    if (feature[23]<=0.0):
                        if (feature[34]<=0.0):
                            if (feature[19]<=0.0):
                                bin_num[6] = 112
                            else:
                                bin_num[6] = 113
                        else:
                            if (feature[10]<=1.0):
                                bin_num[6] = 114
                            else:
                                bin_num[6] = 115
                    else:
                        if (feature[11]<=0.0):
                            if (feature[19]<=0.0):
                                bin_num[6] = 116
                            else:
                                bin_num[6] = 117
                        else:
                            if (feature[29]<=0.0):
                                bin_num[6] = 118
                            else:
                                bin_num[6] = 119
                else:
                    if (feature[1]<=2.0):
                        if (feature[34]<=0.0):
                            if (feature[33]<=0.0):
                                bin_num[6] = 120
                            else:
                                bin_num[6] = 121
                        else:
                            if (feature[26]<=0.0):
                                bin_num[6] = 122
                            else:
                                bin_num[6] = 123
                    else:
                        if (feature[4]<=2628.0):
                            if (feature[34]<=0.0):
                                bin_num[6] = 124
                            else:
                                bin_num[6] = 125
                        else:
                            if (feature[8]<=35.0):
                                bin_num[6] = 126
                            else:
                                bin_num[6] = 127
    # Tree 7
    if (feature[17]<=0.0):
        if (feature[11]<=0.0):
            if (feature[2]<=3.0):
                if (feature[23]<=0.0):
                    if (feature[8]<=34.0):
                        if (feature[20]<=0.0):
                            if (feature[33]<=0.0):
                                bin_num[7] = 0
                            else:
                                bin_num[7] = 1
                        else:
                            if (feature[26]<=0.0):
                                bin_num[7] = 2
                            else:
                                bin_num[7] = 3
                    else:
                        if (feature[26]<=0.0):
                            if (feature[20]<=0.0):
                                bin_num[7] = 4
                            else:
                                bin_num[7] = 5
                        else:
                            if (feature[37]<=0.0):
                                bin_num[7] = 6
                            else:
                                bin_num[7] = 7
                else:
                    if (feature[5]<=16.0):
                        if (feature[36]<=0.0):
                            if (feature[38]<=0.0):
                                bin_num[7] = 8
                            else:
                                bin_num[7] = 9
                        else:
                            if (feature[8]<=34.0):
                                bin_num[7] = 10
                            else:
                                bin_num[7] = 11
                    else:
                        if (feature[7]<=7.0):
                            if (feature[29]<=0.0):
                                bin_num[7] = 12
                            else:
                                bin_num[7] = 13
                        else:
                            if (feature[37]<=0.0):
                                bin_num[7] = 14
                            else:
                                bin_num[7] = 15
            else:
                if (feature[23]<=0.0):
                    if (feature[8]<=34.0):
                        if (feature[36]<=0.0):
                            if (feature[20]<=0.0):
                                bin_num[7] = 16
                            else:
                                bin_num[7] = 17
                        else:
                            if (feature[13]<=0.0):
                                bin_num[7] = 18
                            else:
                                bin_num[7] = 19
                    else:
                        if (feature[20]<=0.0):
                            if (feature[6]<=2.0):
                                bin_num[7] = 20
                            else:
                                bin_num[7] = 21
                        else:
                            if (feature[18]<=0.0):
                                bin_num[7] = 22
                            else:
                                bin_num[7] = 23
                else:
                    if (feature[22]<=0.0):
                        if (feature[34]<=0.0):
                            if (feature[27]<=0.0):
                                bin_num[7] = 24
                            else:
                                bin_num[7] = 25
                        else:
                            if (feature[5]<=16.0):
                                bin_num[7] = 26
                            else:
                                bin_num[7] = 27
                    else:
                        if (feature[29]<=0.0):
                            if (feature[6]<=2.0):
                                bin_num[7] = 28
                            else:
                                bin_num[7] = 29
                        else:
                            if (feature[18]<=0.0):
                                bin_num[7] = 30
                            else:
                                bin_num[7] = 31
        else:
            if (feature[23]<=0.0):
                if (feature[35]<=0.0):
                    if (feature[25]<=0.0):
                        if (feature[10]<=1.0):
                            if (feature[0]<=0.0):
                                bin_num[7] = 32
                            else:
                                bin_num[7] = 33
                        else:
                            if (feature[20]<=0.0):
                                bin_num[7] = 34
                            else:
                                bin_num[7] = 35
                    else:
                        if (feature[6]<=2.0):
                            if (feature[3]<=2.0):
                                bin_num[7] = 36
                            else:
                                bin_num[7] = 37
                        else:
                            if (feature[19]<=0.0):
                                bin_num[7] = 38
                            else:
                                bin_num[7] = 39
                else:
                    if (feature[20]<=0.0):
                        if (feature[3]<=2.0):
                            if (feature[37]<=0.0):
                                bin_num[7] = 40
                            else:
                                bin_num[7] = 41
                        else:
                            if (feature[25]<=0.0):
                                bin_num[7] = 42
                            else:
                                bin_num[7] = 43
                    else:
                        if (feature[18]<=0.0):
                            if (feature[24]<=0.0):
                                bin_num[7] = 44
                            else:
                                bin_num[7] = 45
                        else:
                            if (feature[19]<=0.0):
                                bin_num[7] = 46
                            else:
                                bin_num[7] = 47
            else:
                if (feature[18]<=0.0):
                    if (feature[2]<=3.0):
                        if (feature[29]<=0.0):
                            if (feature[37]<=0.0):
                                bin_num[7] = 48
                            else:
                                bin_num[7] = 49
                        else:
                            if (feature[25]<=0.0):
                                bin_num[7] = 50
                            else:
                                bin_num[7] = 51
                    else:
                        if (feature[35]<=0.0):
                            if (feature[29]<=0.0):
                                bin_num[7] = 52
                            else:
                                bin_num[7] = 53
                        else:
                            if (feature[28]<=0.0):
                                bin_num[7] = 54
                            else:
                                bin_num[7] = 55
                else:
                    if (feature[34]<=0.0):
                        if (feature[21]<=0.0):
                            if (feature[20]<=0.0):
                                bin_num[7] = 56
                            else:
                                bin_num[7] = 57
                        else:
                            if (feature[2]<=3.0):
                                bin_num[7] = 58
                            else:
                                bin_num[7] = 59
                    else:
                        if (feature[10]<=1.0):
                            if (feature[29]<=0.0):
                                bin_num[7] = 60
                            else:
                                bin_num[7] = 61
                        else:
                            if (feature[21]<=0.0):
                                bin_num[7] = 62
                            else:
                                bin_num[7] = 63
    else:
        if (feature[4]<=2681.0):
            if (feature[34]<=0.0):
                if (feature[12]<=2.0):
                    if (feature[27]<=0.0):
                        if (feature[35]<=0.0):
                            if (feature[20]<=0.0):
                                bin_num[7] = 64
                            else:
                                bin_num[7] = 65
                        else:
                            if (feature[33]<=0.0):
                                bin_num[7] = 66
                            else:
                                bin_num[7] = 67
                    else:
                        if (feature[3]<=2.0):
                            if (feature[28]<=0.0):
                                bin_num[7] = 68
                            else:
                                bin_num[7] = 69
                        else:
                            if (feature[10]<=1.0):
                                bin_num[7] = 70
                            else:
                                bin_num[7] = 71
                else:
                    if (feature[20]<=0.0):
                        if (feature[3]<=2.0):
                            if (feature[1]<=2.0):
                                bin_num[7] = 72
                            else:
                                bin_num[7] = 73
                        else:
                            if (feature[1]<=2.0):
                                bin_num[7] = 74
                            else:
                                bin_num[7] = 75
                    else:
                        if (feature[18]<=0.0):
                            if (feature[29]<=0.0):
                                bin_num[7] = 76
                            else:
                                bin_num[7] = 77
                        else:
                            if (feature[1]<=2.0):
                                bin_num[7] = 78
                            else:
                                bin_num[7] = 79
            else:
                if (feature[26]<=0.0):
                    if (feature[33]<=0.0):
                        if (feature[18]<=0.0):
                            if (feature[28]<=0.0):
                                bin_num[7] = 80
                            else:
                                bin_num[7] = 81
                        else:
                            if (feature[20]<=0.0):
                                bin_num[7] = 82
                            else:
                                bin_num[7] = 83
                    else:
                        if (feature[1]<=2.0):
                            if (feature[10]<=1.0):
                                bin_num[7] = 84
                            else:
                                bin_num[7] = 85
                        else:
                            if (feature[9]<=0.0):
                                bin_num[7] = 86
                            else:
                                bin_num[7] = 87
                else:
                    if (feature[2]<=3.0):
                        if (feature[21]<=0.0):
                            if (feature[22]<=0.0):
                                bin_num[7] = 88
                            else:
                                bin_num[7] = 89
                        else:
                            if (feature[22]<=0.0):
                                bin_num[7] = 90
                            else:
                                bin_num[7] = 91
                    else:
                        if (feature[5]<=16.0):
                            if (feature[25]<=0.0):
                                bin_num[7] = 92
                            else:
                                bin_num[7] = 93
                        else:
                            if (feature[10]<=1.0):
                                bin_num[7] = 94
                            else:
                                bin_num[7] = 95
        else:
            if (feature[7]<=7.0):
                if (feature[2]<=3.0):
                    if (feature[26]<=0.0):
                        if (feature[20]<=0.0):
                            if (feature[8]<=34.0):
                                bin_num[7] = 96
                            else:
                                bin_num[7] = 97
                        else:
                            if (feature[10]<=1.0):
                                bin_num[7] = 98
                            else:
                                bin_num[7] = 99
                    else:
                        if (feature[13]<=0.0):
                            if (feature[8]<=34.0):
                                bin_num[7] = 100
                            else:
                                bin_num[7] = 101
                        else:
                            if (feature[28]<=0.0):
                                bin_num[7] = 102
                            else:
                                bin_num[7] = 103
                else:
                    if (feature[18]<=0.0):
                        if (feature[37]<=0.0):
                            if (feature[28]<=0.0):
                                bin_num[7] = 104
                            else:
                                bin_num[7] = 105
                        else:
                            if (feature[29]<=0.0):
                                bin_num[7] = 106
                            else:
                                bin_num[7] = 107
                    else:
                        if (feature[34]<=0.0):
                            if (feature[23]<=0.0):
                                bin_num[7] = 108
                            else:
                                bin_num[7] = 109
                        else:
                            if (feature[26]<=0.0):
                                bin_num[7] = 110
                            else:
                                bin_num[7] = 111
            else:
                if (feature[10]<=1.0):
                    if (feature[13]<=0.0):
                        if (feature[27]<=0.0):
                            if (feature[29]<=0.0):
                                bin_num[7] = 112
                            else:
                                bin_num[7] = 113
                        else:
                            if (feature[34]<=0.0):
                                bin_num[7] = 114
                            else:
                                bin_num[7] = 115
                    else:
                        if (feature[18]<=0.0):
                            if (feature[37]<=0.0):
                                bin_num[7] = 116
                            else:
                                bin_num[7] = 117
                        else:
                            if (feature[19]<=0.0):
                                bin_num[7] = 118
                            else:
                                bin_num[7] = 119
                else:
                    if (feature[12]<=2.0):
                        if (feature[26]<=0.0):
                            if (feature[2]<=3.0):
                                bin_num[7] = 120
                            else:
                                bin_num[7] = 121
                        else:
                            if (feature[2]<=3.0):
                                bin_num[7] = 122
                            else:
                                bin_num[7] = 123
                    else:
                        if (feature[3]<=2.0):
                            if (feature[26]<=0.0):
                                bin_num[7] = 124
                            else:
                                bin_num[7] = 125
                        else:
                            if (feature[18]<=0.0):
                                bin_num[7] = 126
                            else:
                                bin_num[7] = 127
    # Tree 8
    if (feature[6]<=2.0):
        if (feature[7]<=7.0):
            if (feature[13]<=0.0):
                if (feature[5]<=16.0):
                    if (feature[34]<=0.0):
                        if (feature[8]<=34.0):
                            if (feature[17]<=0.0):
                                bin_num[8] = 0
                            else:
                                bin_num[8] = 1
                        else:
                            if (feature[18]<=0.0):
                                bin_num[8] = 2
                            else:
                                bin_num[8] = 3
                    else:
                        if (feature[26]<=0.0):
                            if (feature[20]<=0.0):
                                bin_num[8] = 4
                            else:
                                bin_num[8] = 5
                        else:
                            if (feature[18]<=0.0):
                                bin_num[8] = 6
                            else:
                                bin_num[8] = 7
                else:
                    if (feature[8]<=34.0):
                        if (feature[23]<=0.0):
                            if (feature[29]<=0.0):
                                bin_num[8] = 8
                            else:
                                bin_num[8] = 9
                        else:
                            if (feature[17]<=0.0):
                                bin_num[8] = 10
                            else:
                                bin_num[8] = 11
                    else:
                        if (feature[20]<=0.0):
                            if (feature[29]<=0.0):
                                bin_num[8] = 12
                            else:
                                bin_num[8] = 13
                        else:
                            if (feature[21]<=0.0):
                                bin_num[8] = 14
                            else:
                                bin_num[8] = 15
            else:
                if (feature[4]<=2674.0):
                    if (feature[27]<=0.0):
                        if (feature[29]<=0.0):
                            if (feature[11]<=0.0):
                                bin_num[8] = 16
                            else:
                                bin_num[8] = 17
                        else:
                            if (feature[34]<=0.0):
                                bin_num[8] = 18
                            else:
                                bin_num[8] = 19
                    else:
                        if (feature[22]<=0.0):
                            if (feature[20]<=0.0):
                                bin_num[8] = 20
                            else:
                                bin_num[8] = 21
                        else:
                            if (feature[28]<=0.0):
                                bin_num[8] = 22
                            else:
                                bin_num[8] = 23
                else:
                    if (feature[20]<=0.0):
                        if (feature[2]<=3.0):
                            if (feature[8]<=34.0):
                                bin_num[8] = 24
                            else:
                                bin_num[8] = 25
                        else:
                            if (feature[23]<=0.0):
                                bin_num[8] = 26
                            else:
                                bin_num[8] = 27
                    else:
                        if (feature[18]<=0.0):
                            if (feature[25]<=0.0):
                                bin_num[8] = 28
                            else:
                                bin_num[8] = 29
                        else:
                            if (feature[29]<=0.0):
                                bin_num[8] = 30
                            else:
                                bin_num[8] = 31
        else:
            if (feature[13]<=0.0):
                if (feature[27]<=0.0):
                    if (feature[5]<=16.0):
                        if (feature[24]<=0.0):
                            if (feature[19]<=0.0):
                                bin_num[8] = 32
                            else:
                                bin_num[8] = 33
                        else:
                            if (feature[4]<=2674.0):
                                bin_num[8] = 34
                            else:
                                bin_num[8] = 35
                    else:
                        if (feature[29]<=0.0):
                            if (feature[26]<=0.0):
                                bin_num[8] = 36
                            else:
                                bin_num[8] = 37
                        else:
                            if (feature[4]<=2674.0):
                                bin_num[8] = 38
                            else:
                                bin_num[8] = 39
                else:
                    if (feature[22]<=0.0):
                        if (feature[18]<=0.0):
                            if (feature[28]<=0.0):
                                bin_num[8] = 40
                            else:
                                bin_num[8] = 41
                        else:
                            if (feature[8]<=34.0):
                                bin_num[8] = 42
                            else:
                                bin_num[8] = 43
                    else:
                        if (feature[34]<=0.0):
                            if (feature[24]<=0.0):
                                bin_num[8] = 44
                            else:
                                bin_num[8] = 45
                        else:
                            if (feature[2]<=3.0):
                                bin_num[8] = 46
                            else:
                                bin_num[8] = 47
            else:
                if (feature[4]<=2674.0):
                    if (feature[29]<=0.0):
                        if (feature[27]<=0.0):
                            if (feature[20]<=0.0):
                                bin_num[8] = 48
                            else:
                                bin_num[8] = 49
                        else:
                            if (feature[22]<=0.0):
                                bin_num[8] = 50
                            else:
                                bin_num[8] = 51
                    else:
                        if (feature[20]<=0.0):
                            if (feature[22]<=0.0):
                                bin_num[8] = 52
                            else:
                                bin_num[8] = 53
                        else:
                            if (feature[1]<=2.0):
                                bin_num[8] = 54
                            else:
                                bin_num[8] = 55
                else:
                    if (feature[5]<=16.0):
                        if (feature[12]<=2.0):
                            if (feature[20]<=0.0):
                                bin_num[8] = 56
                            else:
                                bin_num[8] = 57
                        else:
                            if (feature[8]<=34.0):
                                bin_num[8] = 58
                            else:
                                bin_num[8] = 59
                    else:
                        if (feature[8]<=34.0):
                            if (feature[29]<=0.0):
                                bin_num[8] = 60
                            else:
                                bin_num[8] = 61
                        else:
                            if (feature[18]<=0.0):
                                bin_num[8] = 62
                            else:
                                bin_num[8] = 63
    else:
        if (feature[35]<=0.0):
            if (feature[18]<=0.0):
                if (feature[19]<=0.0):
                    if (feature[24]<=0.0):
                        if (feature[28]<=0.0):
                            if (feature[21]<=0.0):
                                bin_num[8] = 64
                            else:
                                bin_num[8] = 65
                        else:
                            if (feature[26]<=0.0):
                                bin_num[8] = 66
                            else:
                                bin_num[8] = 67
                    else:
                        if (feature[37]<=0.0):
                            if (feature[5]<=16.0):
                                bin_num[8] = 68
                            else:
                                bin_num[8] = 69
                        else:
                            if (feature[3]<=2.0):
                                bin_num[8] = 70
                            else:
                                bin_num[8] = 71
                else:
                    if (feature[37]<=0.0):
                        if (feature[5]<=16.0):
                            if (feature[27]<=0.0):
                                bin_num[8] = 72
                            else:
                                bin_num[8] = 73
                        else:
                            if (feature[7]<=7.0):
                                bin_num[8] = 74
                            else:
                                bin_num[8] = 75
                    else:
                        if (feature[26]<=0.0):
                            if (feature[23]<=0.0):
                                bin_num[8] = 76
                            else:
                                bin_num[8] = 77
                        else:
                            if (feature[22]<=0.0):
                                bin_num[8] = 78
                            else:
                                bin_num[8] = 79
            else:
                if (feature[24]<=0.0):
                    if (feature[19]<=0.0):
                        if (feature[29]<=0.0):
                            if (feature[22]<=0.0):
                                bin_num[8] = 80
                            else:
                                bin_num[8] = 81
                        else:
                            if (feature[20]<=0.0):
                                bin_num[8] = 82
                            else:
                                bin_num[8] = 83
                    else:
                        if (feature[27]<=0.0):
                            if (feature[5]<=16.0):
                                bin_num[8] = 84
                            else:
                                bin_num[8] = 85
                        else:
                            if (feature[2]<=3.0):
                                bin_num[8] = 86
                            else:
                                bin_num[8] = 87
                else:
                    if (feature[2]<=3.0):
                        if (feature[23]<=0.0):
                            if (feature[17]<=0.0):
                                bin_num[8] = 88
                            else:
                                bin_num[8] = 89
                        else:
                            if (feature[11]<=0.0):
                                bin_num[8] = 90
                            else:
                                bin_num[8] = 91
                    else:
                        if (feature[1]<=2.0):
                            if (feature[22]<=0.0):
                                bin_num[8] = 92
                            else:
                                bin_num[8] = 93
                        else:
                            if (feature[26]<=0.0):
                                bin_num[8] = 94
                            else:
                                bin_num[8] = 95
        else:
            if (feature[37]<=0.0):
                if (feature[5]<=16.0):
                    if (feature[24]<=0.0):
                        if (feature[11]<=0.0):
                            if (feature[17]<=0.0):
                                bin_num[8] = 96
                            else:
                                bin_num[8] = 97
                        else:
                            if (feature[23]<=0.0):
                                bin_num[8] = 98
                            else:
                                bin_num[8] = 99
                    else:
                        if (feature[27]<=0.0):
                            if (feature[29]<=0.0):
                                bin_num[8] = 100
                            else:
                                bin_num[8] = 101
                        else:
                            if (feature[1]<=2.0):
                                bin_num[8] = 102
                            else:
                                bin_num[8] = 103
                else:
                    if (feature[10]<=1.0):
                        if (feature[7]<=7.0):
                            if (feature[20]<=0.0):
                                bin_num[8] = 104
                            else:
                                bin_num[8] = 105
                        else:
                            if (feature[8]<=34.0):
                                bin_num[8] = 106
                            else:
                                bin_num[8] = 107
                    else:
                        if (feature[7]<=7.0):
                            if (feature[23]<=0.0):
                                bin_num[8] = 108
                            else:
                                bin_num[8] = 109
                        else:
                            if (feature[4]<=2674.0):
                                bin_num[8] = 110
                            else:
                                bin_num[8] = 111
            else:
                if (feature[28]<=0.0):
                    if (feature[29]<=0.0):
                        if (feature[22]<=0.0):
                            if (feature[26]<=0.0):
                                bin_num[8] = 112
                            else:
                                bin_num[8] = 113
                        else:
                            if (feature[23]<=0.0):
                                bin_num[8] = 114
                            else:
                                bin_num[8] = 115
                    else:
                        if (feature[19]<=0.0):
                            if (feature[17]<=0.0):
                                bin_num[8] = 116
                            else:
                                bin_num[8] = 117
                        else:
                            if (feature[20]<=0.0):
                                bin_num[8] = 118
                            else:
                                bin_num[8] = 119
                else:
                    if (feature[20]<=0.0):
                        if (feature[33]<=0.0):
                            if (feature[34]<=0.0):
                                bin_num[8] = 120
                            else:
                                bin_num[8] = 121
                        else:
                            if (feature[2]<=3.0):
                                bin_num[8] = 122
                            else:
                                bin_num[8] = 123
                    else:
                        if (feature[23]<=0.0):
                            if (feature[27]<=0.0):
                                bin_num[8] = 124
                            else:
                                bin_num[8] = 125
                        else:
                            if (feature[27]<=0.0):
                                bin_num[8] = 126
                            else:
                                bin_num[8] = 127
    # Tree 9
    if (feature[6]<=3.0):
        if (feature[8]<=34.0):
            if (feature[18]<=0.0):
                if (feature[35]<=0.0):
                    if (feature[37]<=0.0):
                        if (feature[25]<=0.0):
                            if (feature[23]<=0.0):
                                bin_num[9] = 0
                            else:
                                bin_num[9] = 1
                        else:
                            if (feature[34]<=0.0):
                                bin_num[9] = 2
                            else:
                                bin_num[9] = 3
                    else:
                        if (feature[5]<=15.0):
                            if (feature[17]<=0.0):
                                bin_num[9] = 4
                            else:
                                bin_num[9] = 5
                        else:
                            if (feature[7]<=7.0):
                                bin_num[9] = 6
                            else:
                                bin_num[9] = 7
                else:
                    if (feature[28]<=0.0):
                        if (feature[37]<=0.0):
                            if (feature[25]<=0.0):
                                bin_num[9] = 8
                            else:
                                bin_num[9] = 9
                        else:
                            if (feature[2]<=3.0):
                                bin_num[9] = 10
                            else:
                                bin_num[9] = 11
                    else:
                        if (feature[34]<=0.0):
                            if (feature[37]<=0.0):
                                bin_num[9] = 12
                            else:
                                bin_num[9] = 13
                        else:
                            if (feature[23]<=0.0):
                                bin_num[9] = 14
                            else:
                                bin_num[9] = 15
            else:
                if (feature[19]<=0.0):
                    if (feature[24]<=0.0):
                        if (feature[29]<=0.0):
                            if (feature[20]<=0.0):
                                bin_num[9] = 16
                            else:
                                bin_num[9] = 17
                        else:
                            if (feature[20]<=0.0):
                                bin_num[9] = 18
                            else:
                                bin_num[9] = 19
                    else:
                        if (feature[5]<=15.0):
                            if (feature[0]<=0.0):
                                bin_num[9] = 20
                            else:
                                bin_num[9] = 21
                        else:
                            if (feature[29]<=0.0):
                                bin_num[9] = 22
                            else:
                                bin_num[9] = 23
                else:
                    if (feature[5]<=15.0):
                        if (feature[4]<=2689.0):
                            if (feature[11]<=0.0):
                                bin_num[9] = 24
                            else:
                                bin_num[9] = 25
                        else:
                            if (feature[20]<=0.0):
                                bin_num[9] = 26
                            else:
                                bin_num[9] = 27
                    else:
                        if (feature[2]<=3.0):
                            if (feature[29]<=0.0):
                                bin_num[9] = 28
                            else:
                                bin_num[9] = 29
                        else:
                            if (feature[38]<=0.0):
                                bin_num[9] = 30
                            else:
                                bin_num[9] = 31
        else:
            if (feature[5]<=15.0):
                if (feature[10]<=1.0):
                    if (feature[9]<=0.0):
                        if (feature[4]<=2689.0):
                            if (feature[12]<=2.0):
                                bin_num[9] = 32
                            else:
                                bin_num[9] = 33
                        else:
                            if (feature[13]<=0.0):
                                bin_num[9] = 34
                            else:
                                bin_num[9] = 35
                    else:
                        if (feature[12]<=2.0):
                            if (feature[27]<=0.0):
                                bin_num[9] = 36
                            else:
                                bin_num[9] = 37
                        else:
                            if (feature[38]<=0.0):
                                bin_num[9] = 38
                            else:
                                bin_num[9] = 39
                else:
                    if (feature[18]<=0.0):
                        if (feature[38]<=0.0):
                            if (feature[3]<=2.0):
                                bin_num[9] = 40
                            else:
                                bin_num[9] = 41
                        else:
                            if (feature[37]<=0.0):
                                bin_num[9] = 42
                            else:
                                bin_num[9] = 43
                    else:
                        if (feature[12]<=2.0):
                            if (feature[19]<=0.0):
                                bin_num[9] = 44
                            else:
                                bin_num[9] = 45
                        else:
                            if (feature[20]<=0.0):
                                bin_num[9] = 46
                            else:
                                bin_num[9] = 47
            else:
                if (feature[10]<=1.0):
                    if (feature[2]<=3.0):
                        if (feature[26]<=0.0):
                            if (feature[18]<=0.0):
                                bin_num[9] = 48
                            else:
                                bin_num[9] = 49
                        else:
                            if (feature[22]<=0.0):
                                bin_num[9] = 50
                            else:
                                bin_num[9] = 51
                    else:
                        if (feature[20]<=0.0):
                            if (feature[38]<=0.0):
                                bin_num[9] = 52
                            else:
                                bin_num[9] = 53
                        else:
                            if (feature[29]<=0.0):
                                bin_num[9] = 54
                            else:
                                bin_num[9] = 55
                else:
                    if (feature[18]<=0.0):
                        if (feature[9]<=0.0):
                            if (feature[26]<=0.0):
                                bin_num[9] = 56
                            else:
                                bin_num[9] = 57
                        else:
                            if (feature[25]<=0.0):
                                bin_num[9] = 58
                            else:
                                bin_num[9] = 59
                    else:
                        if (feature[19]<=0.0):
                            if (feature[24]<=0.0):
                                bin_num[9] = 60
                            else:
                                bin_num[9] = 61
                        else:
                            if (feature[20]<=0.0):
                                bin_num[9] = 62
                            else:
                                bin_num[9] = 63
    else:
        if (feature[20]<=0.0):
            if (feature[27]<=0.0):
                if (feature[29]<=0.0):
                    if (feature[33]<=0.0):
                        if (feature[22]<=0.0):
                            if (feature[18]<=0.0):
                                bin_num[9] = 64
                            else:
                                bin_num[9] = 65
                        else:
                            if (feature[37]<=0.0):
                                bin_num[9] = 66
                            else:
                                bin_num[9] = 67
                    else:
                        if (feature[19]<=0.0):
                            if (feature[21]<=0.0):
                                bin_num[9] = 68
                            else:
                                bin_num[9] = 69
                        else:
                            if (feature[18]<=0.0):
                                bin_num[9] = 70
                            else:
                                bin_num[9] = 71
                else:
                    if (feature[22]<=0.0):
                        if (feature[28]<=0.0):
                            if (feature[19]<=0.0):
                                bin_num[9] = 72
                            else:
                                bin_num[9] = 73
                        else:
                            if (feature[37]<=0.0):
                                bin_num[9] = 74
                            else:
                                bin_num[9] = 75
                    else:
                        if (feature[34]<=0.0):
                            if (feature[35]<=0.0):
                                bin_num[9] = 76
                            else:
                                bin_num[9] = 77
                        else:
                            if (feature[21]<=0.0):
                                bin_num[9] = 78
                            else:
                                bin_num[9] = 79
            else:
                if (feature[21]<=0.0):
                    if (feature[22]<=0.0):
                        if (feature[33]<=0.0):
                            if (feature[1]<=2.0):
                                bin_num[9] = 80
                            else:
                                bin_num[9] = 81
                        else:
                            if (feature[23]<=0.0):
                                bin_num[9] = 82
                            else:
                                bin_num[9] = 83
                    else:
                        if (feature[0]<=0.0):
                            if (feature[23]<=0.0):
                                bin_num[9] = 84
                            else:
                                bin_num[9] = 85
                        else:
                            if (feature[37]<=0.0):
                                bin_num[9] = 86
                            else:
                                bin_num[9] = 87
                else:
                    if (feature[1]<=2.0):
                        if (feature[33]<=0.0):
                            if (feature[28]<=0.0):
                                bin_num[9] = 88
                            else:
                                bin_num[9] = 89
                        else:
                            if (feature[37]<=0.0):
                                bin_num[9] = 90
                            else:
                                bin_num[9] = 91
                    else:
                        if (feature[33]<=0.0):
                            if (feature[18]<=0.0):
                                bin_num[9] = 92
                            else:
                                bin_num[9] = 93
                        else:
                            if (feature[0]<=0.0):
                                bin_num[9] = 94
                            else:
                                bin_num[9] = 95
        else:
            if (feature[29]<=0.0):
                if (feature[18]<=0.0):
                    if (feature[12]<=2.0):
                        if (feature[26]<=0.0):
                            if (feature[19]<=0.0):
                                bin_num[9] = 96
                            else:
                                bin_num[9] = 97
                        else:
                            if (feature[3]<=2.0):
                                bin_num[9] = 98
                            else:
                                bin_num[9] = 99
                    else:
                        if (feature[21]<=0.0):
                            if (feature[19]<=0.0):
                                bin_num[9] = 100
                            else:
                                bin_num[9] = 101
                        else:
                            if (feature[28]<=0.0):
                                bin_num[9] = 102
                            else:
                                bin_num[9] = 103
                else:
                    if (feature[10]<=1.0):
                        if (feature[8]<=34.0):
                            if (feature[13]<=0.0):
                                bin_num[9] = 104
                            else:
                                bin_num[9] = 105
                        else:
                            if (feature[5]<=15.0):
                                bin_num[9] = 106
                            else:
                                bin_num[9] = 107
                    else:
                        if (feature[27]<=0.0):
                            if (feature[38]<=0.0):
                                bin_num[9] = 108
                            else:
                                bin_num[9] = 109
                        else:
                            if (feature[23]<=0.0):
                                bin_num[9] = 110
                            else:
                                bin_num[9] = 111
            else:
                if (feature[34]<=0.0):
                    if (feature[2]<=3.0):
                        if (feature[28]<=0.0):
                            if (feature[23]<=0.0):
                                bin_num[9] = 112
                            else:
                                bin_num[9] = 113
                        else:
                            if (feature[23]<=0.0):
                                bin_num[9] = 114
                            else:
                                bin_num[9] = 115
                    else:
                        if (feature[1]<=2.0):
                            if (feature[17]<=0.0):
                                bin_num[9] = 116
                            else:
                                bin_num[9] = 117
                        else:
                            if (feature[21]<=0.0):
                                bin_num[9] = 118
                            else:
                                bin_num[9] = 119
                else:
                    if (feature[21]<=0.0):
                        if (feature[18]<=0.0):
                            if (feature[28]<=0.0):
                                bin_num[9] = 120
                            else:
                                bin_num[9] = 121
                        else:
                            if (feature[5]<=15.0):
                                bin_num[9] = 122
                            else:
                                bin_num[9] = 123
                    else:
                        if (feature[37]<=0.0):
                            if (feature[24]<=0.0):
                                bin_num[9] = 124
                            else:
                                bin_num[9] = 125
                        else:
                            if (feature[0]<=0.0):
                                bin_num[9] = 126
                            else:
                                bin_num[9] = 127
    # Tree 10
    if (feature[17]<=0.0):
        if (feature[2]<=3.0):
            if (feature[18]<=0.0):
                if (feature[26]<=0.0):
                    if (feature[35]<=0.0):
                        if (feature[19]<=0.0):
                            if (feature[24]<=0.0):
                                bin_num[10] = 0
                            else:
                                bin_num[10] = 1
                        else:
                            if (feature[11]<=0.0):
                                bin_num[10] = 2
                            else:
                                bin_num[10] = 3
                    else:
                        if (feature[28]<=0.0):
                            if (feature[37]<=0.0):
                                bin_num[10] = 4
                            else:
                                bin_num[10] = 5
                        else:
                            if (feature[11]<=0.0):
                                bin_num[10] = 6
                            else:
                                bin_num[10] = 7
                else:
                    if (feature[21]<=0.0):
                        if (feature[22]<=0.0):
                            if (feature[33]<=0.0):
                                bin_num[10] = 8
                            else:
                                bin_num[10] = 9
                        else:
                            if (feature[19]<=0.0):
                                bin_num[10] = 10
                            else:
                                bin_num[10] = 11
                    else:
                        if (feature[34]<=0.0):
                            if (feature[28]<=0.0):
                                bin_num[10] = 12
                            else:
                                bin_num[10] = 13
                        else:
                            if (feature[19]<=0.0):
                                bin_num[10] = 14
                            else:
                                bin_num[10] = 15
            else:
                if (feature[20]<=0.0):
                    if (feature[33]<=0.0):
                        if (feature[22]<=0.0):
                            if (feature[27]<=0.0):
                                bin_num[10] = 16
                            else:
                                bin_num[10] = 17
                        else:
                            if (feature[29]<=0.0):
                                bin_num[10] = 18
                            else:
                                bin_num[10] = 19
                    else:
                        if (feature[1]<=2.0):
                            if (feature[27]<=0.0):
                                bin_num[10] = 20
                            else:
                                bin_num[10] = 21
                        else:
                            if (feature[36]<=0.0):
                                bin_num[10] = 22
                            else:
                                bin_num[10] = 23
                else:
                    if (feature[26]<=0.0):
                        if (feature[34]<=0.0):
                            if (feature[24]<=0.0):
                                bin_num[10] = 24
                            else:
                                bin_num[10] = 25
                        else:
                            if (feature[21]<=0.0):
                                bin_num[10] = 26
                            else:
                                bin_num[10] = 27
                    else:
                        if (feature[11]<=0.0):
                            if (feature[36]<=0.0):
                                bin_num[10] = 28
                            else:
                                bin_num[10] = 29
                        else:
                            if (feature[23]<=0.0):
                                bin_num[10] = 30
                            else:
                                bin_num[10] = 31
        else:
            if (feature[11]<=0.0):
                if (feature[23]<=0.0):
                    if (feature[8]<=32.0):
                        if (feature[36]<=0.0):
                            if (feature[38]<=0.0):
                                bin_num[10] = 32
                            else:
                                bin_num[10] = 33
                        else:
                            if (feature[7]<=7.0):
                                bin_num[10] = 34
                            else:
                                bin_num[10] = 35
                    else:
                        if (feature[20]<=0.0):
                            if (feature[38]<=0.0):
                                bin_num[10] = 36
                            else:
                                bin_num[10] = 37
                        else:
                            if (feature[27]<=0.0):
                                bin_num[10] = 38
                            else:
                                bin_num[10] = 39
                else:
                    if (feature[22]<=0.0):
                        if (feature[34]<=0.0):
                            if (feature[27]<=0.0):
                                bin_num[10] = 40
                            else:
                                bin_num[10] = 41
                        else:
                            if (feature[26]<=0.0):
                                bin_num[10] = 42
                            else:
                                bin_num[10] = 43
                    else:
                        if (feature[29]<=0.0):
                            if (feature[0]<=0.0):
                                bin_num[10] = 44
                            else:
                                bin_num[10] = 45
                        else:
                            if (feature[18]<=0.0):
                                bin_num[10] = 46
                            else:
                                bin_num[10] = 47
            else:
                if (feature[23]<=0.0):
                    if (feature[25]<=0.0):
                        if (feature[10]<=1.0):
                            if (feature[21]<=0.0):
                                bin_num[10] = 48
                            else:
                                bin_num[10] = 49
                        else:
                            if (feature[35]<=0.0):
                                bin_num[10] = 50
                            else:
                                bin_num[10] = 51
                    else:
                        if (feature[6]<=2.0):
                            if (feature[0]<=0.0):
                                bin_num[10] = 52
                            else:
                                bin_num[10] = 53
                        else:
                            if (feature[1]<=2.0):
                                bin_num[10] = 54
                            else:
                                bin_num[10] = 55
                else:
                    if (feature[18]<=0.0):
                        if (feature[29]<=0.0):
                            if (feature[22]<=0.0):
                                bin_num[10] = 56
                            else:
                                bin_num[10] = 57
                        else:
                            if (feature[28]<=0.0):
                                bin_num[10] = 58
                            else:
                                bin_num[10] = 59
                    else:
                        if (feature[34]<=0.0):
                            if (feature[21]<=0.0):
                                bin_num[10] = 60
                            else:
                                bin_num[10] = 61
                        else:
                            if (feature[10]<=1.0):
                                bin_num[10] = 62
                            else:
                                bin_num[10] = 63
    else:
        if (feature[4]<=2656.0):
            if (feature[34]<=0.0):
                if (feature[12]<=2.0):
                    if (feature[11]<=0.0):
                        if (feature[25]<=0.0):
                            if (feature[3]<=2.0):
                                bin_num[10] = 64
                            else:
                                bin_num[10] = 65
                        else:
                            if (feature[33]<=0.0):
                                bin_num[10] = 66
                            else:
                                bin_num[10] = 67
                    else:
                        if (feature[33]<=0.0):
                            if (feature[27]<=0.0):
                                bin_num[10] = 68
                            else:
                                bin_num[10] = 69
                        else:
                            if (feature[3]<=2.0):
                                bin_num[10] = 70
                            else:
                                bin_num[10] = 71
                else:
                    if (feature[3]<=2.0):
                        if (feature[7]<=7.0):
                            if (feature[5]<=15.0):
                                bin_num[10] = 72
                            else:
                                bin_num[10] = 73
                        else:
                            if (feature[1]<=2.0):
                                bin_num[10] = 74
                            else:
                                bin_num[10] = 75
                    else:
                        if (feature[20]<=0.0):
                            if (feature[23]<=0.0):
                                bin_num[10] = 76
                            else:
                                bin_num[10] = 77
                        else:
                            if (feature[1]<=2.0):
                                bin_num[10] = 78
                            else:
                                bin_num[10] = 79
            else:
                if (feature[26]<=0.0):
                    if (feature[33]<=0.0):
                        if (feature[18]<=0.0):
                            if (feature[28]<=0.0):
                                bin_num[10] = 80
                            else:
                                bin_num[10] = 81
                        else:
                            if (feature[10]<=1.0):
                                bin_num[10] = 82
                            else:
                                bin_num[10] = 83
                    else:
                        if (feature[1]<=2.0):
                            if (feature[19]<=0.0):
                                bin_num[10] = 84
                            else:
                                bin_num[10] = 85
                        else:
                            if (feature[25]<=0.0):
                                bin_num[10] = 86
                            else:
                                bin_num[10] = 87
                else:
                    if (feature[2]<=3.0):
                        if (feature[21]<=0.0):
                            if (feature[22]<=0.0):
                                bin_num[10] = 88
                            else:
                                bin_num[10] = 89
                        else:
                            if (feature[22]<=0.0):
                                bin_num[10] = 90
                            else:
                                bin_num[10] = 91
                    else:
                        if (feature[10]<=1.0):
                            if (feature[6]<=2.0):
                                bin_num[10] = 92
                            else:
                                bin_num[10] = 93
                        else:
                            if (feature[12]<=2.0):
                                bin_num[10] = 94
                            else:
                                bin_num[10] = 95
        else:
            if (feature[7]<=7.0):
                if (feature[29]<=0.0):
                    if (feature[20]<=0.0):
                        if (feature[27]<=0.0):
                            if (feature[8]<=32.0):
                                bin_num[10] = 96
                            else:
                                bin_num[10] = 97
                        else:
                            if (feature[22]<=0.0):
                                bin_num[10] = 98
                            else:
                                bin_num[10] = 99
                    else:
                        if (feature[10]<=1.0):
                            if (feature[18]<=0.0):
                                bin_num[10] = 100
                            else:
                                bin_num[10] = 101
                        else:
                            if (feature[5]<=15.0):
                                bin_num[10] = 102
                            else:
                                bin_num[10] = 103
                else:
                    if (feature[34]<=0.0):
                        if (feature[28]<=0.0):
                            if (feature[18]<=0.0):
                                bin_num[10] = 104
                            else:
                                bin_num[10] = 105
                        else:
                            if (feature[22]<=0.0):
                                bin_num[10] = 106
                            else:
                                bin_num[10] = 107
                    else:
                        if (feature[22]<=0.0):
                            if (feature[20]<=0.0):
                                bin_num[10] = 108
                            else:
                                bin_num[10] = 109
                        else:
                            if (feature[21]<=0.0):
                                bin_num[10] = 110
                            else:
                                bin_num[10] = 111
            else:
                if (feature[10]<=1.0):
                    if (feature[13]<=0.0):
                        if (feature[27]<=0.0):
                            if (feature[29]<=0.0):
                                bin_num[10] = 112
                            else:
                                bin_num[10] = 113
                        else:
                            if (feature[28]<=0.0):
                                bin_num[10] = 114
                            else:
                                bin_num[10] = 115
                    else:
                        if (feature[8]<=32.0):
                            if (feature[12]<=2.0):
                                bin_num[10] = 116
                            else:
                                bin_num[10] = 117
                        else:
                            if (feature[26]<=0.0):
                                bin_num[10] = 118
                            else:
                                bin_num[10] = 119
                else:
                    if (feature[12]<=2.0):
                        if (feature[2]<=3.0):
                            if (feature[26]<=0.0):
                                bin_num[10] = 120
                            else:
                                bin_num[10] = 121
                        else:
                            if (feature[20]<=0.0):
                                bin_num[10] = 122
                            else:
                                bin_num[10] = 123
                    else:
                        if (feature[3]<=2.0):
                            if (feature[2]<=3.0):
                                bin_num[10] = 124
                            else:
                                bin_num[10] = 125
                        else:
                            if (feature[18]<=0.0):
                                bin_num[10] = 126
                            else:
                                bin_num[10] = 127
    # Tree 11
    if (feature[17]<=0.0):
        if (feature[2]<=3.0):
            if (feature[11]<=0.0):
                if (feature[23]<=0.0):
                    if (feature[8]<=33.0):
                        if (feature[36]<=0.0):
                            if (feature[38]<=0.0):
                                bin_num[11] = 0
                            else:
                                bin_num[11] = 1
                        else:
                            if (feature[7]<=7.0):
                                bin_num[11] = 2
                            else:
                                bin_num[11] = 3
                    else:
                        if (feature[26]<=0.0):
                            if (feature[20]<=0.0):
                                bin_num[11] = 4
                            else:
                                bin_num[11] = 5
                        else:
                            if (feature[13]<=0.0):
                                bin_num[11] = 6
                            else:
                                bin_num[11] = 7
                else:
                    if (feature[5]<=15.0):
                        if (feature[36]<=0.0):
                            if (feature[38]<=0.0):
                                bin_num[11] = 8
                            else:
                                bin_num[11] = 9
                        else:
                            if (feature[25]<=0.0):
                                bin_num[11] = 10
                            else:
                                bin_num[11] = 11
                    else:
                        if (feature[7]<=7.0):
                            if (feature[29]<=0.0):
                                bin_num[11] = 12
                            else:
                                bin_num[11] = 13
                        else:
                            if (feature[37]<=0.0):
                                bin_num[11] = 14
                            else:
                                bin_num[11] = 15
            else:
                if (feature[23]<=0.0):
                    if (feature[26]<=0.0):
                        if (feature[3]<=2.0):
                            if (feature[8]<=33.0):
                                bin_num[11] = 16
                            else:
                                bin_num[11] = 17
                        else:
                            if (feature[1]<=2.0):
                                bin_num[11] = 18
                            else:
                                bin_num[11] = 19
                    else:
                        if (feature[21]<=0.0):
                            if (feature[22]<=0.0):
                                bin_num[11] = 20
                            else:
                                bin_num[11] = 21
                        else:
                            if (feature[34]<=0.0):
                                bin_num[11] = 22
                            else:
                                bin_num[11] = 23
                else:
                    if (feature[18]<=0.0):
                        if (feature[37]<=0.0):
                            if (feature[21]<=0.0):
                                bin_num[11] = 24
                            else:
                                bin_num[11] = 25
                        else:
                            if (feature[0]<=0.0):
                                bin_num[11] = 26
                            else:
                                bin_num[11] = 27
                    else:
                        if (feature[34]<=0.0):
                            if (feature[5]<=15.0):
                                bin_num[11] = 28
                            else:
                                bin_num[11] = 29
                        else:
                            if (feature[10]<=1.0):
                                bin_num[11] = 30
                            else:
                                bin_num[11] = 31
        else:
            if (feature[4]<=2678.0):
                if (feature[13]<=0.0):
                    if (feature[37]<=0.0):
                        if (feature[24]<=0.0):
                            if (feature[18]<=0.0):
                                bin_num[11] = 32
                            else:
                                bin_num[11] = 33
                        else:
                            if (feature[34]<=0.0):
                                bin_num[11] = 34
                            else:
                                bin_num[11] = 35
                    else:
                        if (feature[34]<=0.0):
                            if (feature[33]<=0.0):
                                bin_num[11] = 36
                            else:
                                bin_num[11] = 37
                        else:
                            if (feature[0]<=0.0):
                                bin_num[11] = 38
                            else:
                                bin_num[11] = 39
                else:
                    if (feature[1]<=2.0):
                        if (feature[27]<=0.0):
                            if (feature[29]<=0.0):
                                bin_num[11] = 40
                            else:
                                bin_num[11] = 41
                        else:
                            if (feature[22]<=0.0):
                                bin_num[11] = 42
                            else:
                                bin_num[11] = 43
                    else:
                        if (feature[20]<=0.0):
                            if (feature[29]<=0.0):
                                bin_num[11] = 44
                            else:
                                bin_num[11] = 45
                        else:
                            if (feature[21]<=0.0):
                                bin_num[11] = 46
                            else:
                                bin_num[11] = 47
            else:
                if (feature[5]<=15.0):
                    if (feature[6]<=2.0):
                        if (feature[36]<=0.0):
                            if (feature[23]<=0.0):
                                bin_num[11] = 48
                            else:
                                bin_num[11] = 49
                        else:
                            if (feature[7]<=7.0):
                                bin_num[11] = 50
                            else:
                                bin_num[11] = 51
                    else:
                        if (feature[12]<=2.0):
                            if (feature[10]<=1.0):
                                bin_num[11] = 52
                            else:
                                bin_num[11] = 53
                        else:
                            if (feature[10]<=1.0):
                                bin_num[11] = 54
                            else:
                                bin_num[11] = 55
                else:
                    if (feature[8]<=33.0):
                        if (feature[29]<=0.0):
                            if (feature[27]<=0.0):
                                bin_num[11] = 56
                            else:
                                bin_num[11] = 57
                        else:
                            if (feature[20]<=0.0):
                                bin_num[11] = 58
                            else:
                                bin_num[11] = 59
                    else:
                        if (feature[3]<=2.0):
                            if (feature[37]<=0.0):
                                bin_num[11] = 60
                            else:
                                bin_num[11] = 61
                        else:
                            if (feature[18]<=0.0):
                                bin_num[11] = 62
                            else:
                                bin_num[11] = 63
    else:
        if (feature[4]<=2678.0):
            if (feature[34]<=0.0):
                if (feature[35]<=0.0):
                    if (feature[25]<=0.0):
                        if (feature[12]<=2.0):
                            if (feature[3]<=2.0):
                                bin_num[11] = 64
                            else:
                                bin_num[11] = 65
                        else:
                            if (feature[3]<=2.0):
                                bin_num[11] = 66
                            else:
                                bin_num[11] = 67
                    else:
                        if (feature[19]<=0.0):
                            if (feature[24]<=0.0):
                                bin_num[11] = 68
                            else:
                                bin_num[11] = 69
                        else:
                            if (feature[3]<=2.0):
                                bin_num[11] = 70
                            else:
                                bin_num[11] = 71
                else:
                    if (feature[28]<=0.0):
                        if (feature[33]<=0.0):
                            if (feature[27]<=0.0):
                                bin_num[11] = 72
                            else:
                                bin_num[11] = 73
                        else:
                            if (feature[18]<=0.0):
                                bin_num[11] = 74
                            else:
                                bin_num[11] = 75
                    else:
                        if (feature[20]<=0.0):
                            if (feature[37]<=0.0):
                                bin_num[11] = 76
                            else:
                                bin_num[11] = 77
                        else:
                            if (feature[18]<=0.0):
                                bin_num[11] = 78
                            else:
                                bin_num[11] = 79
            else:
                if (feature[26]<=0.0):
                    if (feature[33]<=0.0):
                        if (feature[20]<=0.0):
                            if (feature[22]<=0.0):
                                bin_num[11] = 80
                            else:
                                bin_num[11] = 81
                        else:
                            if (feature[21]<=0.0):
                                bin_num[11] = 82
                            else:
                                bin_num[11] = 83
                    else:
                        if (feature[1]<=2.0):
                            if (feature[25]<=0.0):
                                bin_num[11] = 84
                            else:
                                bin_num[11] = 85
                        else:
                            if (feature[9]<=0.0):
                                bin_num[11] = 86
                            else:
                                bin_num[11] = 87
                else:
                    if (feature[2]<=3.0):
                        if (feature[28]<=0.0):
                            if (feature[19]<=0.0):
                                bin_num[11] = 88
                            else:
                                bin_num[11] = 89
                        else:
                            if (feature[3]<=2.0):
                                bin_num[11] = 90
                            else:
                                bin_num[11] = 91
                    else:
                        if (feature[10]<=1.0):
                            if (feature[21]<=0.0):
                                bin_num[11] = 92
                            else:
                                bin_num[11] = 93
                        else:
                            if (feature[12]<=2.0):
                                bin_num[11] = 94
                            else:
                                bin_num[11] = 95
        else:
            if (feature[7]<=7.0):
                if (feature[2]<=3.0):
                    if (feature[35]<=0.0):
                        if (feature[26]<=0.0):
                            if (feature[18]<=0.0):
                                bin_num[11] = 96
                            else:
                                bin_num[11] = 97
                        else:
                            if (feature[28]<=0.0):
                                bin_num[11] = 98
                            else:
                                bin_num[11] = 99
                    else:
                        if (feature[37]<=0.0):
                            if (feature[8]<=33.0):
                                bin_num[11] = 100
                            else:
                                bin_num[11] = 101
                        else:
                            if (feature[8]<=33.0):
                                bin_num[11] = 102
                            else:
                                bin_num[11] = 103
                else:
                    if (feature[18]<=0.0):
                        if (feature[37]<=0.0):
                            if (feature[35]<=0.0):
                                bin_num[11] = 104
                            else:
                                bin_num[11] = 105
                        else:
                            if (feature[28]<=0.0):
                                bin_num[11] = 106
                            else:
                                bin_num[11] = 107
                    else:
                        if (feature[19]<=0.0):
                            if (feature[24]<=0.0):
                                bin_num[11] = 108
                            else:
                                bin_num[11] = 109
                        else:
                            if (feature[27]<=0.0):
                                bin_num[11] = 110
                            else:
                                bin_num[11] = 111
            else:
                if (feature[10]<=1.0):
                    if (feature[18]<=0.0):
                        if (feature[37]<=0.0):
                            if (feature[26]<=0.0):
                                bin_num[11] = 112
                            else:
                                bin_num[11] = 113
                        else:
                            if (feature[26]<=0.0):
                                bin_num[11] = 114
                            else:
                                bin_num[11] = 115
                    else:
                        if (feature[19]<=0.0):
                            if (feature[24]<=0.0):
                                bin_num[11] = 116
                            else:
                                bin_num[11] = 117
                        else:
                            if (feature[13]<=0.0):
                                bin_num[11] = 118
                            else:
                                bin_num[11] = 119
                else:
                    if (feature[26]<=0.0):
                        if (feature[34]<=0.0):
                            if (feature[18]<=0.0):
                                bin_num[11] = 120
                            else:
                                bin_num[11] = 121
                        else:
                            if (feature[20]<=0.0):
                                bin_num[11] = 122
                            else:
                                bin_num[11] = 123
                    else:
                        if (feature[37]<=0.0):
                            if (feature[28]<=0.0):
                                bin_num[11] = 124
                            else:
                                bin_num[11] = 125
                        else:
                            if (feature[21]<=0.0):
                                bin_num[11] = 126
                            else:
                                bin_num[11] = 127
    # Tree 12
    if (feature[17]<=0.0):
        if (feature[18]<=0.0):
            if (feature[37]<=0.0):
                if (feature[35]<=0.0):
                    if (feature[4]<=2748.0):
                        if (feature[34]<=0.0):
                            if (feature[13]<=0.0):
                                bin_num[12] = 0
                            else:
                                bin_num[12] = 1
                        else:
                            if (feature[28]<=0.0):
                                bin_num[12] = 2
                            else:
                                bin_num[12] = 3
                    else:
                        if (feature[25]<=0.0):
                            if (feature[23]<=0.0):
                                bin_num[12] = 4
                            else:
                                bin_num[12] = 5
                        else:
                            if (feature[20]<=0.0):
                                bin_num[12] = 6
                            else:
                                bin_num[12] = 7
                else:
                    if (feature[28]<=0.0):
                        if (feature[4]<=2748.0):
                            if (feature[12]<=2.0):
                                bin_num[12] = 8
                            else:
                                bin_num[12] = 9
                        else:
                            if (feature[25]<=0.0):
                                bin_num[12] = 10
                            else:
                                bin_num[12] = 11
                    else:
                        if (feature[25]<=0.0):
                            if (feature[23]<=0.0):
                                bin_num[12] = 12
                            else:
                                bin_num[12] = 13
                        else:
                            if (feature[8]<=34.0):
                                bin_num[12] = 14
                            else:
                                bin_num[12] = 15
            else:
                if (feature[35]<=0.0):
                    if (feature[19]<=0.0):
                        if (feature[24]<=0.0):
                            if (feature[28]<=0.0):
                                bin_num[12] = 16
                            else:
                                bin_num[12] = 17
                        else:
                            if (feature[3]<=2.0):
                                bin_num[12] = 18
                            else:
                                bin_num[12] = 19
                    else:
                        if (feature[2]<=3.0):
                            if (feature[26]<=0.0):
                                bin_num[12] = 20
                            else:
                                bin_num[12] = 21
                        else:
                            if (feature[27]<=0.0):
                                bin_num[12] = 22
                            else:
                                bin_num[12] = 23
                else:
                    if (feature[28]<=0.0):
                        if (feature[29]<=0.0):
                            if (feature[22]<=0.0):
                                bin_num[12] = 24
                            else:
                                bin_num[12] = 25
                        else:
                            if (feature[10]<=1.0):
                                bin_num[12] = 26
                            else:
                                bin_num[12] = 27
                    else:
                        if (feature[34]<=0.0):
                            if (feature[33]<=0.0):
                                bin_num[12] = 28
                            else:
                                bin_num[12] = 29
                        else:
                            if (feature[22]<=0.0):
                                bin_num[12] = 30
                            else:
                                bin_num[12] = 31
        else:
            if (feature[11]<=0.0):
                if (feature[19]<=0.0):
                    if (feature[24]<=0.0):
                        if (feature[29]<=0.0):
                            if (feature[28]<=0.0):
                                bin_num[12] = 32
                            else:
                                bin_num[12] = 33
                        else:
                            if (feature[20]<=0.0):
                                bin_num[12] = 34
                            else:
                                bin_num[12] = 35
                    else:
                        if (feature[35]<=0.0):
                            if (feature[23]<=0.0):
                                bin_num[12] = 36
                            else:
                                bin_num[12] = 37
                        else:
                            if (feature[7]<=7.0):
                                bin_num[12] = 38
                            else:
                                bin_num[12] = 39
                else:
                    if (feature[27]<=0.0):
                        if (feature[35]<=0.0):
                            if (feature[13]<=0.0):
                                bin_num[12] = 40
                            else:
                                bin_num[12] = 41
                        else:
                            if (feature[7]<=7.0):
                                bin_num[12] = 42
                            else:
                                bin_num[12] = 43
                    else:
                        if (feature[22]<=0.0):
                            if (feature[36]<=0.0):
                                bin_num[12] = 44
                            else:
                                bin_num[12] = 45
                        else:
                            if (feature[34]<=0.0):
                                bin_num[12] = 46
                            else:
                                bin_num[12] = 47
            else:
                if (feature[23]<=0.0):
                    if (feature[10]<=1.0):
                        if (feature[20]<=0.0):
                            if (feature[21]<=0.0):
                                bin_num[12] = 48
                            else:
                                bin_num[12] = 49
                        else:
                            if (feature[35]<=0.0):
                                bin_num[12] = 50
                            else:
                                bin_num[12] = 51
                    else:
                        if (feature[27]<=0.0):
                            if (feature[34]<=0.0):
                                bin_num[12] = 52
                            else:
                                bin_num[12] = 53
                        else:
                            if (feature[33]<=0.0):
                                bin_num[12] = 54
                            else:
                                bin_num[12] = 55
                else:
                    if (feature[34]<=0.0):
                        if (feature[21]<=0.0):
                            if (feature[27]<=0.0):
                                bin_num[12] = 56
                            else:
                                bin_num[12] = 57
                        else:
                            if (feature[20]<=0.0):
                                bin_num[12] = 58
                            else:
                                bin_num[12] = 59
                    else:
                        if (feature[10]<=1.0):
                            if (feature[29]<=0.0):
                                bin_num[12] = 60
                            else:
                                bin_num[12] = 61
                        else:
                            if (feature[8]<=34.0):
                                bin_num[12] = 62
                            else:
                                bin_num[12] = 63
    else:
        if (feature[4]<=2748.0):
            if (feature[20]<=0.0):
                if (feature[27]<=0.0):
                    if (feature[29]<=0.0):
                        if (feature[33]<=0.0):
                            if (feature[23]<=0.0):
                                bin_num[12] = 64
                            else:
                                bin_num[12] = 65
                        else:
                            if (feature[11]<=0.0):
                                bin_num[12] = 66
                            else:
                                bin_num[12] = 67
                    else:
                        if (feature[22]<=0.0):
                            if (feature[21]<=0.0):
                                bin_num[12] = 68
                            else:
                                bin_num[12] = 69
                        else:
                            if (feature[1]<=2.0):
                                bin_num[12] = 70
                            else:
                                bin_num[12] = 71
                else:
                    if (feature[21]<=0.0):
                        if (feature[22]<=0.0):
                            if (feature[33]<=0.0):
                                bin_num[12] = 72
                            else:
                                bin_num[12] = 73
                        else:
                            if (feature[37]<=0.0):
                                bin_num[12] = 74
                            else:
                                bin_num[12] = 75
                    else:
                        if (feature[1]<=2.0):
                            if (feature[22]<=0.0):
                                bin_num[12] = 76
                            else:
                                bin_num[12] = 77
                        else:
                            if (feature[28]<=0.0):
                                bin_num[12] = 78
                            else:
                                bin_num[12] = 79
            else:
                if (feature[29]<=0.0):
                    if (feature[18]<=0.0):
                        if (feature[34]<=0.0):
                            if (feature[12]<=2.0):
                                bin_num[12] = 80
                            else:
                                bin_num[12] = 81
                        else:
                            if (feature[28]<=0.0):
                                bin_num[12] = 82
                            else:
                                bin_num[12] = 83
                    else:
                        if (feature[26]<=0.0):
                            if (feature[21]<=0.0):
                                bin_num[12] = 84
                            else:
                                bin_num[12] = 85
                        else:
                            if (feature[2]<=3.0):
                                bin_num[12] = 86
                            else:
                                bin_num[12] = 87
                else:
                    if (feature[34]<=0.0):
                        if (feature[23]<=0.0):
                            if (feature[12]<=2.0):
                                bin_num[12] = 88
                            else:
                                bin_num[12] = 89
                        else:
                            if (feature[18]<=0.0):
                                bin_num[12] = 90
                            else:
                                bin_num[12] = 91
                    else:
                        if (feature[21]<=0.0):
                            if (feature[7]<=7.0):
                                bin_num[12] = 92
                            else:
                                bin_num[12] = 93
                        else:
                            if (feature[37]<=0.0):
                                bin_num[12] = 94
                            else:
                                bin_num[12] = 95
        else:
            if (feature[7]<=7.0):
                if (feature[29]<=0.0):
                    if (feature[20]<=0.0):
                        if (feature[33]<=0.0):
                            if (feature[8]<=34.0):
                                bin_num[12] = 96
                            else:
                                bin_num[12] = 97
                        else:
                            if (feature[1]<=2.0):
                                bin_num[12] = 98
                            else:
                                bin_num[12] = 99
                    else:
                        if (feature[10]<=1.0):
                            if (feature[18]<=0.0):
                                bin_num[12] = 100
                            else:
                                bin_num[12] = 101
                        else:
                            if (feature[5]<=15.0):
                                bin_num[12] = 102
                            else:
                                bin_num[12] = 103
                else:
                    if (feature[34]<=0.0):
                        if (feature[28]<=0.0):
                            if (feature[18]<=0.0):
                                bin_num[12] = 104
                            else:
                                bin_num[12] = 105
                        else:
                            if (feature[20]<=0.0):
                                bin_num[12] = 106
                            else:
                                bin_num[12] = 107
                    else:
                        if (feature[22]<=0.0):
                            if (feature[20]<=0.0):
                                bin_num[12] = 108
                            else:
                                bin_num[12] = 109
                        else:
                            if (feature[21]<=0.0):
                                bin_num[12] = 110
                            else:
                                bin_num[12] = 111
            else:
                if (feature[26]<=0.0):
                    if (feature[34]<=0.0):
                        if (feature[18]<=0.0):
                            if (feature[35]<=0.0):
                                bin_num[12] = 112
                            else:
                                bin_num[12] = 113
                        else:
                            if (feature[19]<=0.0):
                                bin_num[12] = 114
                            else:
                                bin_num[12] = 115
                    else:
                        if (feature[20]<=0.0):
                            if (feature[22]<=0.0):
                                bin_num[12] = 116
                            else:
                                bin_num[12] = 117
                        else:
                            if (feature[21]<=0.0):
                                bin_num[12] = 118
                            else:
                                bin_num[12] = 119
                else:
                    if (feature[13]<=0.0):
                        if (feature[33]<=0.0):
                            if (feature[5]<=15.0):
                                bin_num[12] = 120
                            else:
                                bin_num[12] = 121
                        else:
                            if (feature[19]<=0.0):
                                bin_num[12] = 122
                            else:
                                bin_num[12] = 123
                    else:
                        if (feature[2]<=3.0):
                            if (feature[37]<=0.0):
                                bin_num[12] = 124
                            else:
                                bin_num[12] = 125
                        else:
                            if (feature[12]<=2.0):
                                bin_num[12] = 126
                            else:
                                bin_num[12] = 127
    # Tree 13
    if (feature[20]<=0.0):
        if (feature[18]<=0.0):
            if (feature[37]<=0.0):
                if (feature[35]<=0.0):
                    if (feature[4]<=2723.0):
                        if (feature[19]<=0.0):
                            if (feature[24]<=0.0):
                                bin_num[13] = 0
                            else:
                                bin_num[13] = 1
                        else:
                            if (feature[1]<=2.0):
                                bin_num[13] = 2
                            else:
                                bin_num[13] = 3
                    else:
                        if (feature[7]<=7.0):
                            if (feature[29]<=0.0):
                                bin_num[13] = 4
                            else:
                                bin_num[13] = 5
                        else:
                            if (feature[13]<=0.0):
                                bin_num[13] = 6
                            else:
                                bin_num[13] = 7
                else:
                    if (feature[28]<=0.0):
                        if (feature[4]<=2723.0):
                            if (feature[13]<=0.0):
                                bin_num[13] = 8
                            else:
                                bin_num[13] = 9
                        else:
                            if (feature[7]<=7.0):
                                bin_num[13] = 10
                            else:
                                bin_num[13] = 11
                    else:
                        if (feature[34]<=0.0):
                            if (feature[33]<=0.0):
                                bin_num[13] = 12
                            else:
                                bin_num[13] = 13
                        else:
                            if (feature[22]<=0.0):
                                bin_num[13] = 14
                            else:
                                bin_num[13] = 15
            else:
                if (feature[35]<=0.0):
                    if (feature[19]<=0.0):
                        if (feature[24]<=0.0):
                            if (feature[28]<=0.0):
                                bin_num[13] = 16
                            else:
                                bin_num[13] = 17
                        else:
                            if (feature[26]<=0.0):
                                bin_num[13] = 18
                            else:
                                bin_num[13] = 19
                    else:
                        if (feature[27]<=0.0):
                            if (feature[3]<=2.0):
                                bin_num[13] = 20
                            else:
                                bin_num[13] = 21
                        else:
                            if (feature[22]<=0.0):
                                bin_num[13] = 22
                            else:
                                bin_num[13] = 23
                else:
                    if (feature[28]<=0.0):
                        if (feature[33]<=0.0):
                            if (feature[29]<=0.0):
                                bin_num[13] = 24
                            else:
                                bin_num[13] = 25
                        else:
                            if (feature[5]<=16.0):
                                bin_num[13] = 26
                            else:
                                bin_num[13] = 27
                    else:
                        if (feature[33]<=0.0):
                            if (feature[34]<=0.0):
                                bin_num[13] = 28
                            else:
                                bin_num[13] = 29
                        else:
                            if (feature[17]<=0.0):
                                bin_num[13] = 30
                            else:
                                bin_num[13] = 31
        else:
            if (feature[33]<=0.0):
                if (feature[22]<=0.0):
                    if (feature[27]<=0.0):
                        if (feature[26]<=0.0):
                            if (feature[23]<=0.0):
                                bin_num[13] = 32
                            else:
                                bin_num[13] = 33
                        else:
                            if (feature[21]<=0.0):
                                bin_num[13] = 34
                            else:
                                bin_num[13] = 35
                    else:
                        if (feature[21]<=0.0):
                            if (feature[12]<=2.0):
                                bin_num[13] = 36
                            else:
                                bin_num[13] = 37
                        else:
                            if (feature[34]<=0.0):
                                bin_num[13] = 38
                            else:
                                bin_num[13] = 39
                else:
                    if (feature[29]<=0.0):
                        if (feature[19]<=0.0):
                            if (feature[24]<=0.0):
                                bin_num[13] = 40
                            else:
                                bin_num[13] = 41
                        else:
                            if (feature[35]<=0.0):
                                bin_num[13] = 42
                            else:
                                bin_num[13] = 43
                    else:
                        if (feature[24]<=0.0):
                            if (feature[19]<=0.0):
                                bin_num[13] = 44
                            else:
                                bin_num[13] = 45
                        else:
                            if (feature[35]<=0.0):
                                bin_num[13] = 46
                            else:
                                bin_num[13] = 47
            else:
                if (feature[1]<=2.0):
                    if (feature[27]<=0.0):
                        if (feature[23]<=0.0):
                            if (feature[34]<=0.0):
                                bin_num[13] = 48
                            else:
                                bin_num[13] = 49
                        else:
                            if (feature[17]<=0.0):
                                bin_num[13] = 50
                            else:
                                bin_num[13] = 51
                    else:
                        if (feature[21]<=0.0):
                            if (feature[0]<=0.0):
                                bin_num[13] = 52
                            else:
                                bin_num[13] = 53
                        else:
                            if (feature[34]<=0.0):
                                bin_num[13] = 54
                            else:
                                bin_num[13] = 55
                else:
                    if (feature[26]<=0.0):
                        if (feature[8]<=34.0):
                            if (feature[29]<=0.0):
                                bin_num[13] = 56
                            else:
                                bin_num[13] = 57
                        else:
                            if (feature[12]<=2.0):
                                bin_num[13] = 58
                            else:
                                bin_num[13] = 59
                    else:
                        if (feature[2]<=3.0):
                            if (feature[10]<=1.0):
                                bin_num[13] = 60
                            else:
                                bin_num[13] = 61
                        else:
                            if (feature[5]<=16.0):
                                bin_num[13] = 62
                            else:
                                bin_num[13] = 63
    else:
        if (feature[6]<=2.0):
            if (feature[18]<=0.0):
                if (feature[34]<=0.0):
                    if (feature[4]<=2723.0):
                        if (feature[12]<=2.0):
                            if (feature[3]<=2.0):
                                bin_num[13] = 64
                            else:
                                bin_num[13] = 65
                        else:
                            if (feature[25]<=0.0):
                                bin_num[13] = 66
                            else:
                                bin_num[13] = 67
                    else:
                        if (feature[25]<=0.0):
                            if (feature[23]<=0.0):
                                bin_num[13] = 68
                            else:
                                bin_num[13] = 69
                        else:
                            if (feature[35]<=0.0):
                                bin_num[13] = 70
                            else:
                                bin_num[13] = 71
                else:
                    if (feature[26]<=0.0):
                        if (feature[21]<=0.0):
                            if (feature[29]<=0.0):
                                bin_num[13] = 72
                            else:
                                bin_num[13] = 73
                        else:
                            if (feature[12]<=2.0):
                                bin_num[13] = 74
                            else:
                                bin_num[13] = 75
                    else:
                        if (feature[28]<=0.0):
                            if (feature[19]<=0.0):
                                bin_num[13] = 76
                            else:
                                bin_num[13] = 77
                        else:
                            if (feature[23]<=0.0):
                                bin_num[13] = 78
                            else:
                                bin_num[13] = 79
            else:
                if (feature[19]<=0.0):
                    if (feature[24]<=0.0):
                        if (feature[28]<=0.0):
                            if (feature[29]<=0.0):
                                bin_num[13] = 80
                            else:
                                bin_num[13] = 81
                        else:
                            if (feature[26]<=0.0):
                                bin_num[13] = 82
                            else:
                                bin_num[13] = 83
                    else:
                        if (feature[29]<=0.0):
                            if (feature[0]<=0.0):
                                bin_num[13] = 84
                            else:
                                bin_num[13] = 85
                        else:
                            if (feature[35]<=0.0):
                                bin_num[13] = 86
                            else:
                                bin_num[13] = 87
                else:
                    if (feature[35]<=0.0):
                        if (feature[27]<=0.0):
                            if (feature[29]<=0.0):
                                bin_num[13] = 88
                            else:
                                bin_num[13] = 89
                        else:
                            if (feature[21]<=0.0):
                                bin_num[13] = 90
                            else:
                                bin_num[13] = 91
                    else:
                        if (feature[4]<=2723.0):
                            if (feature[7]<=7.0):
                                bin_num[13] = 92
                            else:
                                bin_num[13] = 93
                        else:
                            if (feature[7]<=7.0):
                                bin_num[13] = 94
                            else:
                                bin_num[13] = 95
        else:
            if (feature[29]<=0.0):
                if (feature[18]<=0.0):
                    if (feature[12]<=2.0):
                        if (feature[26]<=0.0):
                            if (feature[19]<=0.0):
                                bin_num[13] = 96
                            else:
                                bin_num[13] = 97
                        else:
                            if (feature[3]<=2.0):
                                bin_num[13] = 98
                            else:
                                bin_num[13] = 99
                    else:
                        if (feature[21]<=0.0):
                            if (feature[27]<=0.0):
                                bin_num[13] = 100
                            else:
                                bin_num[13] = 101
                        else:
                            if (feature[28]<=0.0):
                                bin_num[13] = 102
                            else:
                                bin_num[13] = 103
                else:
                    if (feature[35]<=0.0):
                        if (feature[24]<=0.0):
                            if (feature[19]<=0.0):
                                bin_num[13] = 104
                            else:
                                bin_num[13] = 105
                        else:
                            if (feature[27]<=0.0):
                                bin_num[13] = 106
                            else:
                                bin_num[13] = 107
                    else:
                        if (feature[28]<=0.0):
                            if (feature[11]<=0.0):
                                bin_num[13] = 108
                            else:
                                bin_num[13] = 109
                        else:
                            if (feature[21]<=0.0):
                                bin_num[13] = 110
                            else:
                                bin_num[13] = 111
            else:
                if (feature[10]<=1.0):
                    if (feature[0]<=0.0):
                        if (feature[12]<=2.0):
                            if (feature[8]<=34.0):
                                bin_num[13] = 112
                            else:
                                bin_num[13] = 113
                        else:
                            if (feature[5]<=16.0):
                                bin_num[13] = 114
                            else:
                                bin_num[13] = 115
                    else:
                        if (feature[7]<=7.0):
                            if (feature[21]<=0.0):
                                bin_num[13] = 116
                            else:
                                bin_num[13] = 117
                        else:
                            if (feature[23]<=0.0):
                                bin_num[13] = 118
                            else:
                                bin_num[13] = 119
                else:
                    if (feature[25]<=0.0):
                        if (feature[12]<=2.0):
                            if (feature[37]<=0.0):
                                bin_num[13] = 120
                            else:
                                bin_num[13] = 121
                        else:
                            if (feature[5]<=16.0):
                                bin_num[13] = 122
                            else:
                                bin_num[13] = 123
                    else:
                        if (feature[28]<=0.0):
                            if (feature[0]<=0.0):
                                bin_num[13] = 124
                            else:
                                bin_num[13] = 125
                        else:
                            if (feature[1]<=2.0):
                                bin_num[13] = 126
                            else:
                                bin_num[13] = 127
    # Tree 14
    if (feature[6]<=2.0):
        if (feature[7]<=7.0):
            if (feature[13]<=0.0):
                if (feature[5]<=15.0):
                    if (feature[21]<=0.0):
                        if (feature[29]<=0.0):
                            if (feature[18]<=0.0):
                                bin_num[14] = 0
                            else:
                                bin_num[14] = 1
                        else:
                            if (feature[8]<=34.0):
                                bin_num[14] = 2
                            else:
                                bin_num[14] = 3
                    else:
                        if (feature[22]<=0.0):
                            if (feature[27]<=0.0):
                                bin_num[14] = 4
                            else:
                                bin_num[14] = 5
                        else:
                            if (feature[29]<=0.0):
                                bin_num[14] = 6
                            else:
                                bin_num[14] = 7
                else:
                    if (feature[8]<=34.0):
                        if (feature[23]<=0.0):
                            if (feature[12]<=2.0):
                                bin_num[14] = 8
                            else:
                                bin_num[14] = 9
                        else:
                            if (feature[17]<=0.0):
                                bin_num[14] = 10
                            else:
                                bin_num[14] = 11
                    else:
                        if (feature[38]<=0.0):
                            if (feature[21]<=0.0):
                                bin_num[14] = 12
                            else:
                                bin_num[14] = 13
                        else:
                            if (feature[34]<=0.0):
                                bin_num[14] = 14
                            else:
                                bin_num[14] = 15
            else:
                if (feature[4]<=2763.0):
                    if (feature[10]<=1.0):
                        if (feature[21]<=0.0):
                            if (feature[11]<=0.0):
                                bin_num[14] = 16
                            else:
                                bin_num[14] = 17
                        else:
                            if (feature[34]<=0.0):
                                bin_num[14] = 18
                            else:
                                bin_num[14] = 19
                    else:
                        if (feature[0]<=0.0):
                            if (feature[36]<=0.0):
                                bin_num[14] = 20
                            else:
                                bin_num[14] = 21
                        else:
                            if (feature[1]<=2.0):
                                bin_num[14] = 22
                            else:
                                bin_num[14] = 23
                else:
                    if (feature[36]<=0.0):
                        if (feature[23]<=0.0):
                            if (feature[2]<=3.0):
                                bin_num[14] = 24
                            else:
                                bin_num[14] = 25
                        else:
                            if (feature[5]<=15.0):
                                bin_num[14] = 26
                            else:
                                bin_num[14] = 27
                    else:
                        if (feature[8]<=34.0):
                            if (feature[2]<=3.0):
                                bin_num[14] = 28
                            else:
                                bin_num[14] = 29
                        else:
                            if (feature[10]<=1.0):
                                bin_num[14] = 30
                            else:
                                bin_num[14] = 31
        else:
            if (feature[13]<=0.0):
                if (feature[27]<=0.0):
                    if (feature[5]<=15.0):
                        if (feature[24]<=0.0):
                            if (feature[22]<=0.0):
                                bin_num[14] = 32
                            else:
                                bin_num[14] = 33
                        else:
                            if (feature[17]<=0.0):
                                bin_num[14] = 34
                            else:
                                bin_num[14] = 35
                    else:
                        if (feature[17]<=0.0):
                            if (feature[26]<=0.0):
                                bin_num[14] = 36
                            else:
                                bin_num[14] = 37
                        else:
                            if (feature[8]<=34.0):
                                bin_num[14] = 38
                            else:
                                bin_num[14] = 39
                else:
                    if (feature[22]<=0.0):
                        if (feature[18]<=0.0):
                            if (feature[21]<=0.0):
                                bin_num[14] = 40
                            else:
                                bin_num[14] = 41
                        else:
                            if (feature[8]<=34.0):
                                bin_num[14] = 42
                            else:
                                bin_num[14] = 43
                    else:
                        if (feature[34]<=0.0):
                            if (feature[1]<=2.0):
                                bin_num[14] = 44
                            else:
                                bin_num[14] = 45
                        else:
                            if (feature[2]<=3.0):
                                bin_num[14] = 46
                            else:
                                bin_num[14] = 47
            else:
                if (feature[4]<=2763.0):
                    if (feature[8]<=34.0):
                        if (feature[29]<=0.0):
                            if (feature[17]<=0.0):
                                bin_num[14] = 48
                            else:
                                bin_num[14] = 49
                        else:
                            if (feature[20]<=0.0):
                                bin_num[14] = 50
                            else:
                                bin_num[14] = 51
                    else:
                        if (feature[27]<=0.0):
                            if (feature[29]<=0.0):
                                bin_num[14] = 52
                            else:
                                bin_num[14] = 53
                        else:
                            if (feature[28]<=0.0):
                                bin_num[14] = 54
                            else:
                                bin_num[14] = 55
                else:
                    if (feature[5]<=15.0):
                        if (feature[12]<=2.0):
                            if (feature[2]<=3.0):
                                bin_num[14] = 56
                            else:
                                bin_num[14] = 57
                        else:
                            if (feature[17]<=0.0):
                                bin_num[14] = 58
                            else:
                                bin_num[14] = 59
                    else:
                        if (feature[8]<=34.0):
                            if (feature[38]<=0.0):
                                bin_num[14] = 60
                            else:
                                bin_num[14] = 61
                        else:
                            if (feature[17]<=0.0):
                                bin_num[14] = 62
                            else:
                                bin_num[14] = 63
    else:
        if (feature[35]<=0.0):
            if (feature[18]<=0.0):
                if (feature[19]<=0.0):
                    if (feature[24]<=0.0):
                        if (feature[28]<=0.0):
                            if (feature[34]<=0.0):
                                bin_num[14] = 64
                            else:
                                bin_num[14] = 65
                        else:
                            if (feature[21]<=0.0):
                                bin_num[14] = 66
                            else:
                                bin_num[14] = 67
                    else:
                        if (feature[1]<=2.0):
                            if (feature[3]<=2.0):
                                bin_num[14] = 68
                            else:
                                bin_num[14] = 69
                        else:
                            if (feature[20]<=0.0):
                                bin_num[14] = 70
                            else:
                                bin_num[14] = 71
                else:
                    if (feature[27]<=0.0):
                        if (feature[3]<=2.0):
                            if (feature[26]<=0.0):
                                bin_num[14] = 72
                            else:
                                bin_num[14] = 73
                        else:
                            if (feature[20]<=0.0):
                                bin_num[14] = 74
                            else:
                                bin_num[14] = 75
                    else:
                        if (feature[33]<=0.0):
                            if (feature[23]<=0.0):
                                bin_num[14] = 76
                            else:
                                bin_num[14] = 77
                        else:
                            if (feature[1]<=2.0):
                                bin_num[14] = 78
                            else:
                                bin_num[14] = 79
            else:
                if (feature[24]<=0.0):
                    if (feature[19]<=0.0):
                        if (feature[23]<=0.0):
                            if (feature[33]<=0.0):
                                bin_num[14] = 80
                            else:
                                bin_num[14] = 81
                        else:
                            if (feature[11]<=0.0):
                                bin_num[14] = 82
                            else:
                                bin_num[14] = 83
                    else:
                        if (feature[27]<=0.0):
                            if (feature[3]<=2.0):
                                bin_num[14] = 84
                            else:
                                bin_num[14] = 85
                        else:
                            if (feature[2]<=3.0):
                                bin_num[14] = 86
                            else:
                                bin_num[14] = 87
                else:
                    if (feature[8]<=34.0):
                        if (feature[11]<=0.0):
                            if (feature[9]<=0.0):
                                bin_num[14] = 88
                            else:
                                bin_num[14] = 89
                        else:
                            if (feature[23]<=0.0):
                                bin_num[14] = 90
                            else:
                                bin_num[14] = 91
                    else:
                        if (feature[10]<=1.0):
                            if (feature[5]<=15.0):
                                bin_num[14] = 92
                            else:
                                bin_num[14] = 93
                        else:
                            if (feature[36]<=0.0):
                                bin_num[14] = 94
                            else:
                                bin_num[14] = 95
        else:
            if (feature[24]<=0.0):
                if (feature[23]<=0.0):
                    if (feature[3]<=2.0):
                        if (feature[21]<=0.0):
                            if (feature[26]<=0.0):
                                bin_num[14] = 96
                            else:
                                bin_num[14] = 97
                        else:
                            if (feature[2]<=3.0):
                                bin_num[14] = 98
                            else:
                                bin_num[14] = 99
                    else:
                        if (feature[17]<=0.0):
                            if (feature[18]<=0.0):
                                bin_num[14] = 100
                            else:
                                bin_num[14] = 101
                        else:
                            if (feature[10]<=1.0):
                                bin_num[14] = 102
                            else:
                                bin_num[14] = 103
                else:
                    if (feature[11]<=0.0):
                        if (feature[37]<=0.0):
                            if (feature[13]<=0.0):
                                bin_num[14] = 104
                            else:
                                bin_num[14] = 105
                        else:
                            if (feature[22]<=0.0):
                                bin_num[14] = 106
                            else:
                                bin_num[14] = 107
                    else:
                        if (feature[18]<=0.0):
                            if (feature[28]<=0.0):
                                bin_num[14] = 108
                            else:
                                bin_num[14] = 109
                        else:
                            if (feature[5]<=15.0):
                                bin_num[14] = 110
                            else:
                                bin_num[14] = 111
            else:
                if (feature[25]<=0.0):
                    if (feature[29]<=0.0):
                        if (feature[3]<=2.0):
                            if (feature[27]<=0.0):
                                bin_num[14] = 112
                            else:
                                bin_num[14] = 113
                        else:
                            if (feature[26]<=0.0):
                                bin_num[14] = 114
                            else:
                                bin_num[14] = 115
                    else:
                        if (feature[7]<=7.0):
                            if (feature[2]<=3.0):
                                bin_num[14] = 116
                            else:
                                bin_num[14] = 117
                        else:
                            if (feature[36]<=0.0):
                                bin_num[14] = 118
                            else:
                                bin_num[14] = 119
                else:
                    if (feature[22]<=0.0):
                        if (feature[20]<=0.0):
                            if (feature[33]<=0.0):
                                bin_num[14] = 120
                            else:
                                bin_num[14] = 121
                        else:
                            if (feature[23]<=0.0):
                                bin_num[14] = 122
                            else:
                                bin_num[14] = 123
                    else:
                        if (feature[17]<=0.0):
                            if (feature[10]<=1.0):
                                bin_num[14] = 124
                            else:
                                bin_num[14] = 125
                        else:
                            if (feature[29]<=0.0):
                                bin_num[14] = 126
                            else:
                                bin_num[14] = 127
    # Tree 15
    if (feature[6]<=3.0):
        if (feature[8]<=35.0):
            if (feature[36]<=0.0):
                if (feature[17]<=0.0):
                    if (feature[38]<=0.0):
                        if (feature[11]<=0.0):
                            if (feature[5]<=16.0):
                                bin_num[15] = 0
                            else:
                                bin_num[15] = 1
                        else:
                            if (feature[23]<=0.0):
                                bin_num[15] = 2
                            else:
                                bin_num[15] = 3
                    else:
                        if (feature[7]<=7.0):
                            if (feature[13]<=0.0):
                                bin_num[15] = 4
                            else:
                                bin_num[15] = 5
                        else:
                            if (feature[13]<=0.0):
                                bin_num[15] = 6
                            else:
                                bin_num[15] = 7
                else:
                    if (feature[5]<=16.0):
                        if (feature[4]<=2753.0):
                            if (feature[10]<=1.0):
                                bin_num[15] = 8
                            else:
                                bin_num[15] = 9
                        else:
                            if (feature[20]<=0.0):
                                bin_num[15] = 10
                            else:
                                bin_num[15] = 11
                    else:
                        if (feature[29]<=0.0):
                            if (feature[37]<=0.0):
                                bin_num[15] = 12
                            else:
                                bin_num[15] = 13
                        else:
                            if (feature[20]<=0.0):
                                bin_num[15] = 14
                            else:
                                bin_num[15] = 15
            else:
                if (feature[7]<=7.0):
                    if (feature[13]<=0.0):
                        if (feature[5]<=16.0):
                            if (feature[34]<=0.0):
                                bin_num[15] = 16
                            else:
                                bin_num[15] = 17
                        else:
                            if (feature[23]<=0.0):
                                bin_num[15] = 18
                            else:
                                bin_num[15] = 19
                    else:
                        if (feature[10]<=1.0):
                            if (feature[18]<=0.0):
                                bin_num[15] = 20
                            else:
                                bin_num[15] = 21
                        else:
                            if (feature[5]<=16.0):
                                bin_num[15] = 22
                            else:
                                bin_num[15] = 23
                else:
                    if (feature[13]<=0.0):
                        if (feature[34]<=0.0):
                            if (feature[5]<=16.0):
                                bin_num[15] = 24
                            else:
                                bin_num[15] = 25
                        else:
                            if (feature[18]<=0.0):
                                bin_num[15] = 26
                            else:
                                bin_num[15] = 27
                    else:
                        if (feature[18]<=0.0):
                            if (feature[25]<=0.0):
                                bin_num[15] = 28
                            else:
                                bin_num[15] = 29
                        else:
                            if (feature[29]<=0.0):
                                bin_num[15] = 30
                            else:
                                bin_num[15] = 31
        else:
            if (feature[10]<=1.0):
                if (feature[5]<=16.0):
                    if (feature[9]<=0.0):
                        if (feature[13]<=0.0):
                            if (feature[18]<=0.0):
                                bin_num[15] = 32
                            else:
                                bin_num[15] = 33
                        else:
                            if (feature[22]<=0.0):
                                bin_num[15] = 34
                            else:
                                bin_num[15] = 35
                    else:
                        if (feature[12]<=2.0):
                            if (feature[27]<=0.0):
                                bin_num[15] = 36
                            else:
                                bin_num[15] = 37
                        else:
                            if (feature[38]<=0.0):
                                bin_num[15] = 38
                            else:
                                bin_num[15] = 39
                else:
                    if (feature[3]<=2.0):
                        if (feature[38]<=0.0):
                            if (feature[18]<=0.0):
                                bin_num[15] = 40
                            else:
                                bin_num[15] = 41
                        else:
                            if (feature[18]<=0.0):
                                bin_num[15] = 42
                            else:
                                bin_num[15] = 43
                    else:
                        if (feature[20]<=0.0):
                            if (feature[2]<=3.0):
                                bin_num[15] = 44
                            else:
                                bin_num[15] = 45
                        else:
                            if (feature[17]<=0.0):
                                bin_num[15] = 46
                            else:
                                bin_num[15] = 47
            else:
                if (feature[0]<=0.0):
                    if (feature[18]<=0.0):
                        if (feature[25]<=0.0):
                            if (feature[23]<=0.0):
                                bin_num[15] = 48
                            else:
                                bin_num[15] = 49
                        else:
                            if (feature[23]<=0.0):
                                bin_num[15] = 50
                            else:
                                bin_num[15] = 51
                    else:
                        if (feature[19]<=0.0):
                            if (feature[24]<=0.0):
                                bin_num[15] = 52
                            else:
                                bin_num[15] = 53
                        else:
                            if (feature[38]<=0.0):
                                bin_num[15] = 54
                            else:
                                bin_num[15] = 55
                else:
                    if (feature[3]<=2.0):
                        if (feature[36]<=0.0):
                            if (feature[38]<=0.0):
                                bin_num[15] = 56
                            else:
                                bin_num[15] = 57
                        else:
                            if (feature[1]<=2.0):
                                bin_num[15] = 58
                            else:
                                bin_num[15] = 59
                    else:
                        if (feature[21]<=0.0):
                            if (feature[37]<=0.0):
                                bin_num[15] = 60
                            else:
                                bin_num[15] = 61
                        else:
                            if (feature[12]<=2.0):
                                bin_num[15] = 62
                            else:
                                bin_num[15] = 63
    else:
        if (feature[10]<=1.0):
            if (feature[5]<=16.0):
                if (feature[34]<=0.0):
                    if (feature[8]<=35.0):
                        if (feature[13]<=0.0):
                            if (feature[0]<=0.0):
                                bin_num[15] = 64
                            else:
                                bin_num[15] = 65
                        else:
                            if (feature[18]<=0.0):
                                bin_num[15] = 66
                            else:
                                bin_num[15] = 67
                    else:
                        if (feature[9]<=0.0):
                            if (feature[27]<=0.0):
                                bin_num[15] = 68
                            else:
                                bin_num[15] = 69
                        else:
                            if (feature[2]<=3.0):
                                bin_num[15] = 70
                            else:
                                bin_num[15] = 71
                else:
                    if (feature[21]<=0.0):
                        if (feature[29]<=0.0):
                            if (feature[25]<=0.0):
                                bin_num[15] = 72
                            else:
                                bin_num[15] = 73
                        else:
                            if (feature[18]<=0.0):
                                bin_num[15] = 74
                            else:
                                bin_num[15] = 75
                    else:
                        if (feature[12]<=2.0):
                            if (feature[3]<=2.0):
                                bin_num[15] = 76
                            else:
                                bin_num[15] = 77
                        else:
                            if (feature[29]<=0.0):
                                bin_num[15] = 78
                            else:
                                bin_num[15] = 79
            else:
                if (feature[8]<=35.0):
                    if (feature[13]<=0.0):
                        if (feature[23]<=0.0):
                            if (feature[25]<=0.0):
                                bin_num[15] = 80
                            else:
                                bin_num[15] = 81
                        else:
                            if (feature[4]<=2753.0):
                                bin_num[15] = 82
                            else:
                                bin_num[15] = 83
                    else:
                        if (feature[37]<=0.0):
                            if (feature[18]<=0.0):
                                bin_num[15] = 84
                            else:
                                bin_num[15] = 85
                        else:
                            if (feature[7]<=7.0):
                                bin_num[15] = 86
                            else:
                                bin_num[15] = 87
                else:
                    if (feature[7]<=7.0):
                        if (feature[17]<=0.0):
                            if (feature[20]<=0.0):
                                bin_num[15] = 88
                            else:
                                bin_num[15] = 89
                        else:
                            if (feature[4]<=2753.0):
                                bin_num[15] = 90
                            else:
                                bin_num[15] = 91
                    else:
                        if (feature[3]<=2.0):
                            if (feature[18]<=0.0):
                                bin_num[15] = 92
                            else:
                                bin_num[15] = 93
                        else:
                            if (feature[12]<=2.0):
                                bin_num[15] = 94
                            else:
                                bin_num[15] = 95
        else:
            if (feature[36]<=0.0):
                if (feature[38]<=0.0):
                    if (feature[23]<=0.0):
                        if (feature[25]<=0.0):
                            if (feature[27]<=0.0):
                                bin_num[15] = 96
                            else:
                                bin_num[15] = 97
                        else:
                            if (feature[17]<=0.0):
                                bin_num[15] = 98
                            else:
                                bin_num[15] = 99
                    else:
                        if (feature[11]<=0.0):
                            if (feature[37]<=0.0):
                                bin_num[15] = 100
                            else:
                                bin_num[15] = 101
                        else:
                            if (feature[8]<=35.0):
                                bin_num[15] = 102
                            else:
                                bin_num[15] = 103
                else:
                    if (feature[0]<=0.0):
                        if (feature[8]<=35.0):
                            if (feature[5]<=16.0):
                                bin_num[15] = 104
                            else:
                                bin_num[15] = 105
                        else:
                            if (feature[5]<=16.0):
                                bin_num[15] = 106
                            else:
                                bin_num[15] = 107
                    else:
                        if (feature[37]<=0.0):
                            if (feature[8]<=35.0):
                                bin_num[15] = 108
                            else:
                                bin_num[15] = 109
                        else:
                            if (feature[8]<=35.0):
                                bin_num[15] = 110
                            else:
                                bin_num[15] = 111
            else:
                if (feature[8]<=35.0):
                    if (feature[0]<=0.0):
                        if (feature[33]<=0.0):
                            if (feature[12]<=2.0):
                                bin_num[15] = 112
                            else:
                                bin_num[15] = 113
                        else:
                            if (feature[19]<=0.0):
                                bin_num[15] = 114
                            else:
                                bin_num[15] = 115
                    else:
                        if (feature[37]<=0.0):
                            if (feature[1]<=2.0):
                                bin_num[15] = 116
                            else:
                                bin_num[15] = 117
                        else:
                            if (feature[33]<=0.0):
                                bin_num[15] = 118
                            else:
                                bin_num[15] = 119
                else:
                    if (feature[0]<=0.0):
                        if (feature[2]<=3.0):
                            if (feature[7]<=7.0):
                                bin_num[15] = 120
                            else:
                                bin_num[15] = 121
                        else:
                            if (feature[37]<=0.0):
                                bin_num[15] = 122
                            else:
                                bin_num[15] = 123
                    else:
                        if (feature[37]<=0.0):
                            if (feature[12]<=2.0):
                                bin_num[15] = 124
                            else:
                                bin_num[15] = 125
                        else:
                            if (feature[5]<=16.0):
                                bin_num[15] = 126
                            else:
                                bin_num[15] = 127
    # Tree 16
    if (feature[20]<=0.0):
        if (feature[17]<=0.0):
            if (feature[2]<=3.0):
                if (feature[33]<=0.0):
                    if (feature[22]<=0.0):
                        if (feature[27]<=0.0):
                            if (feature[29]<=0.0):
                                bin_num[16] = 0
                            else:
                                bin_num[16] = 1
                        else:
                            if (feature[21]<=0.0):
                                bin_num[16] = 2
                            else:
                                bin_num[16] = 3
                    else:
                        if (feature[29]<=0.0):
                            if (feature[26]<=0.0):
                                bin_num[16] = 4
                            else:
                                bin_num[16] = 5
                        else:
                            if (feature[34]<=0.0):
                                bin_num[16] = 6
                            else:
                                bin_num[16] = 7
                else:
                    if (feature[1]<=2.0):
                        if (feature[27]<=0.0):
                            if (feature[26]<=0.0):
                                bin_num[16] = 8
                            else:
                                bin_num[16] = 9
                        else:
                            if (feature[21]<=0.0):
                                bin_num[16] = 10
                            else:
                                bin_num[16] = 11
                    else:
                        if (feature[37]<=0.0):
                            if (feature[4]<=2652.0):
                                bin_num[16] = 12
                            else:
                                bin_num[16] = 13
                        else:
                            if (feature[5]<=14.0):
                                bin_num[16] = 14
                            else:
                                bin_num[16] = 15
            else:
                if (feature[13]<=0.0):
                    if (feature[7]<=7.0):
                        if (feature[5]<=14.0):
                            if (feature[18]<=0.0):
                                bin_num[16] = 16
                            else:
                                bin_num[16] = 17
                        else:
                            if (feature[8]<=33.0):
                                bin_num[16] = 18
                            else:
                                bin_num[16] = 19
                    else:
                        if (feature[28]<=0.0):
                            if (feature[26]<=0.0):
                                bin_num[16] = 20
                            else:
                                bin_num[16] = 21
                        else:
                            if (feature[4]<=2652.0):
                                bin_num[16] = 22
                            else:
                                bin_num[16] = 23
                else:
                    if (feature[1]<=2.0):
                        if (feature[33]<=0.0):
                            if (feature[22]<=0.0):
                                bin_num[16] = 24
                            else:
                                bin_num[16] = 25
                        else:
                            if (feature[27]<=0.0):
                                bin_num[16] = 26
                            else:
                                bin_num[16] = 27
                    else:
                        if (feature[4]<=2652.0):
                            if (feature[26]<=0.0):
                                bin_num[16] = 28
                            else:
                                bin_num[16] = 29
                        else:
                            if (feature[7]<=7.0):
                                bin_num[16] = 30
                            else:
                                bin_num[16] = 31
        else:
            if (feature[22]<=0.0):
                if (feature[33]<=0.0):
                    if (feature[27]<=0.0):
                        if (feature[1]<=2.0):
                            if (feature[29]<=0.0):
                                bin_num[16] = 32
                            else:
                                bin_num[16] = 33
                        else:
                            if (feature[26]<=0.0):
                                bin_num[16] = 34
                            else:
                                bin_num[16] = 35
                    else:
                        if (feature[21]<=0.0):
                            if (feature[1]<=2.0):
                                bin_num[16] = 36
                            else:
                                bin_num[16] = 37
                        else:
                            if (feature[37]<=0.0):
                                bin_num[16] = 38
                            else:
                                bin_num[16] = 39
                else:
                    if (feature[1]<=2.0):
                        if (feature[25]<=0.0):
                            if (feature[29]<=0.0):
                                bin_num[16] = 40
                            else:
                                bin_num[16] = 41
                        else:
                            if (feature[21]<=0.0):
                                bin_num[16] = 42
                            else:
                                bin_num[16] = 43
                    else:
                        if (feature[27]<=0.0):
                            if (feature[25]<=0.0):
                                bin_num[16] = 44
                            else:
                                bin_num[16] = 45
                        else:
                            if (feature[2]<=3.0):
                                bin_num[16] = 46
                            else:
                                bin_num[16] = 47
            else:
                if (feature[29]<=0.0):
                    if (feature[1]<=2.0):
                        if (feature[12]<=2.0):
                            if (feature[35]<=0.0):
                                bin_num[16] = 48
                            else:
                                bin_num[16] = 49
                        else:
                            if (feature[2]<=3.0):
                                bin_num[16] = 50
                            else:
                                bin_num[16] = 51
                    else:
                        if (feature[26]<=0.0):
                            if (feature[18]<=0.0):
                                bin_num[16] = 52
                            else:
                                bin_num[16] = 53
                        else:
                            if (feature[21]<=0.0):
                                bin_num[16] = 54
                            else:
                                bin_num[16] = 55
                else:
                    if (feature[6]<=2.0):
                        if (feature[34]<=0.0):
                            if (feature[18]<=0.0):
                                bin_num[16] = 56
                            else:
                                bin_num[16] = 57
                        else:
                            if (feature[21]<=0.0):
                                bin_num[16] = 58
                            else:
                                bin_num[16] = 59
                    else:
                        if (feature[5]<=14.0):
                            if (feature[37]<=0.0):
                                bin_num[16] = 60
                            else:
                                bin_num[16] = 61
                        else:
                            if (feature[21]<=0.0):
                                bin_num[16] = 62
                            else:
                                bin_num[16] = 63
    else:
        if (feature[29]<=0.0):
            if (feature[17]<=0.0):
                if (feature[18]<=0.0):
                    if (feature[34]<=0.0):
                        if (feature[4]<=2652.0):
                            if (feature[12]<=2.0):
                                bin_num[16] = 64
                            else:
                                bin_num[16] = 65
                        else:
                            if (feature[10]<=1.0):
                                bin_num[16] = 66
                            else:
                                bin_num[16] = 67
                    else:
                        if (feature[28]<=0.0):
                            if (feature[21]<=0.0):
                                bin_num[16] = 68
                            else:
                                bin_num[16] = 69
                        else:
                            if (feature[13]<=0.0):
                                bin_num[16] = 70
                            else:
                                bin_num[16] = 71
                else:
                    if (feature[27]<=0.0):
                        if (feature[4]<=2652.0):
                            if (feature[24]<=0.0):
                                bin_num[16] = 72
                            else:
                                bin_num[16] = 73
                        else:
                            if (feature[19]<=0.0):
                                bin_num[16] = 74
                            else:
                                bin_num[16] = 75
                    else:
                        if (feature[21]<=0.0):
                            if (feature[10]<=1.0):
                                bin_num[16] = 76
                            else:
                                bin_num[16] = 77
                        else:
                            if (feature[34]<=0.0):
                                bin_num[16] = 78
                            else:
                                bin_num[16] = 79
            else:
                if (feature[4]<=2652.0):
                    if (feature[1]<=2.0):
                        if (feature[9]<=0.0):
                            if (feature[12]<=2.0):
                                bin_num[16] = 80
                            else:
                                bin_num[16] = 81
                        else:
                            if (feature[2]<=3.0):
                                bin_num[16] = 82
                            else:
                                bin_num[16] = 83
                    else:
                        if (feature[26]<=0.0):
                            if (feature[34]<=0.0):
                                bin_num[16] = 84
                            else:
                                bin_num[16] = 85
                        else:
                            if (feature[2]<=3.0):
                                bin_num[16] = 86
                            else:
                                bin_num[16] = 87
                else:
                    if (feature[26]<=0.0):
                        if (feature[34]<=0.0):
                            if (feature[7]<=7.0):
                                bin_num[16] = 88
                            else:
                                bin_num[16] = 89
                        else:
                            if (feature[21]<=0.0):
                                bin_num[16] = 90
                            else:
                                bin_num[16] = 91
                    else:
                        if (feature[2]<=3.0):
                            if (feature[28]<=0.0):
                                bin_num[16] = 92
                            else:
                                bin_num[16] = 93
                        else:
                            if (feature[21]<=0.0):
                                bin_num[16] = 94
                            else:
                                bin_num[16] = 95
        else:
            if (feature[10]<=1.0):
                if (feature[4]<=2652.0):
                    if (feature[1]<=2.0):
                        if (feature[34]<=0.0):
                            if (feature[2]<=3.0):
                                bin_num[16] = 96
                            else:
                                bin_num[16] = 97
                        else:
                            if (feature[21]<=0.0):
                                bin_num[16] = 98
                            else:
                                bin_num[16] = 99
                    else:
                        if (feature[7]<=7.0):
                            if (feature[23]<=0.0):
                                bin_num[16] = 100
                            else:
                                bin_num[16] = 101
                        else:
                            if (feature[12]<=2.0):
                                bin_num[16] = 102
                            else:
                                bin_num[16] = 103
                else:
                    if (feature[34]<=0.0):
                        if (feature[2]<=3.0):
                            if (feature[28]<=0.0):
                                bin_num[16] = 104
                            else:
                                bin_num[16] = 105
                        else:
                            if (feature[1]<=2.0):
                                bin_num[16] = 106
                            else:
                                bin_num[16] = 107
                    else:
                        if (feature[21]<=0.0):
                            if (feature[23]<=0.0):
                                bin_num[16] = 108
                            else:
                                bin_num[16] = 109
                        else:
                            if (feature[18]<=0.0):
                                bin_num[16] = 110
                            else:
                                bin_num[16] = 111
            else:
                if (feature[23]<=0.0):
                    if (feature[12]<=2.0):
                        if (feature[25]<=0.0):
                            if (feature[37]<=0.0):
                                bin_num[16] = 112
                            else:
                                bin_num[16] = 113
                        else:
                            if (feature[34]<=0.0):
                                bin_num[16] = 114
                            else:
                                bin_num[16] = 115
                    else:
                        if (feature[5]<=14.0):
                            if (feature[37]<=0.0):
                                bin_num[16] = 116
                            else:
                                bin_num[16] = 117
                        else:
                            if (feature[1]<=2.0):
                                bin_num[16] = 118
                            else:
                                bin_num[16] = 119
                else:
                    if (feature[18]<=0.0):
                        if (feature[1]<=2.0):
                            if (feature[28]<=0.0):
                                bin_num[16] = 120
                            else:
                                bin_num[16] = 121
                        else:
                            if (feature[28]<=0.0):
                                bin_num[16] = 122
                            else:
                                bin_num[16] = 123
                    else:
                        if (feature[17]<=0.0):
                            if (feature[11]<=0.0):
                                bin_num[16] = 124
                            else:
                                bin_num[16] = 125
                        else:
                            if (feature[21]<=0.0):
                                bin_num[16] = 126
                            else:
                                bin_num[16] = 127
    # Tree 17
    if (feature[20]<=0.0):
        if (feature[18]<=0.0):
            if (feature[37]<=0.0):
                if (feature[35]<=0.0):
                    if (feature[19]<=0.0):
                        if (feature[24]<=0.0):
                            if (feature[28]<=0.0):
                                bin_num[17] = 0
                            else:
                                bin_num[17] = 1
                        else:
                            if (feature[23]<=0.0):
                                bin_num[17] = 2
                            else:
                                bin_num[17] = 3
                    else:
                        if (feature[26]<=0.0):
                            if (feature[25]<=0.0):
                                bin_num[17] = 4
                            else:
                                bin_num[17] = 5
                        else:
                            if (feature[2]<=3.0):
                                bin_num[17] = 6
                            else:
                                bin_num[17] = 7
                else:
                    if (feature[28]<=0.0):
                        if (feature[4]<=2635.0):
                            if (feature[1]<=2.0):
                                bin_num[17] = 8
                            else:
                                bin_num[17] = 9
                        else:
                            if (feature[23]<=0.0):
                                bin_num[17] = 10
                            else:
                                bin_num[17] = 11
                    else:
                        if (feature[34]<=0.0):
                            if (feature[33]<=0.0):
                                bin_num[17] = 12
                            else:
                                bin_num[17] = 13
                        else:
                            if (feature[22]<=0.0):
                                bin_num[17] = 14
                            else:
                                bin_num[17] = 15
            else:
                if (feature[35]<=0.0):
                    if (feature[19]<=0.0):
                        if (feature[24]<=0.0):
                            if (feature[28]<=0.0):
                                bin_num[17] = 16
                            else:
                                bin_num[17] = 17
                        else:
                            if (feature[9]<=0.0):
                                bin_num[17] = 18
                            else:
                                bin_num[17] = 19
                    else:
                        if (feature[26]<=0.0):
                            if (feature[22]<=0.0):
                                bin_num[17] = 20
                            else:
                                bin_num[17] = 21
                        else:
                            if (feature[1]<=2.0):
                                bin_num[17] = 22
                            else:
                                bin_num[17] = 23
                else:
                    if (feature[28]<=0.0):
                        if (feature[29]<=0.0):
                            if (feature[5]<=16.0):
                                bin_num[17] = 24
                            else:
                                bin_num[17] = 25
                        else:
                            if (feature[33]<=0.0):
                                bin_num[17] = 26
                            else:
                                bin_num[17] = 27
                    else:
                        if (feature[33]<=0.0):
                            if (feature[29]<=0.0):
                                bin_num[17] = 28
                            else:
                                bin_num[17] = 29
                        else:
                            if (feature[23]<=0.0):
                                bin_num[17] = 30
                            else:
                                bin_num[17] = 31
        else:
            if (feature[33]<=0.0):
                if (feature[22]<=0.0):
                    if (feature[27]<=0.0):
                        if (feature[26]<=0.0):
                            if (feature[29]<=0.0):
                                bin_num[17] = 32
                            else:
                                bin_num[17] = 33
                        else:
                            if (feature[21]<=0.0):
                                bin_num[17] = 34
                            else:
                                bin_num[17] = 35
                    else:
                        if (feature[21]<=0.0):
                            if (feature[6]<=2.0):
                                bin_num[17] = 36
                            else:
                                bin_num[17] = 37
                        else:
                            if (feature[12]<=2.0):
                                bin_num[17] = 38
                            else:
                                bin_num[17] = 39
                else:
                    if (feature[29]<=0.0):
                        if (feature[19]<=0.0):
                            if (feature[24]<=0.0):
                                bin_num[17] = 40
                            else:
                                bin_num[17] = 41
                        else:
                            if (feature[3]<=2.0):
                                bin_num[17] = 42
                            else:
                                bin_num[17] = 43
                    else:
                        if (feature[24]<=0.0):
                            if (feature[19]<=0.0):
                                bin_num[17] = 44
                            else:
                                bin_num[17] = 45
                        else:
                            if (feature[35]<=0.0):
                                bin_num[17] = 46
                            else:
                                bin_num[17] = 47
            else:
                if (feature[1]<=2.0):
                    if (feature[27]<=0.0):
                        if (feature[23]<=0.0):
                            if (feature[34]<=0.0):
                                bin_num[17] = 48
                            else:
                                bin_num[17] = 49
                        else:
                            if (feature[10]<=1.0):
                                bin_num[17] = 50
                            else:
                                bin_num[17] = 51
                    else:
                        if (feature[21]<=0.0):
                            if (feature[23]<=0.0):
                                bin_num[17] = 52
                            else:
                                bin_num[17] = 53
                        else:
                            if (feature[34]<=0.0):
                                bin_num[17] = 54
                            else:
                                bin_num[17] = 55
                else:
                    if (feature[26]<=0.0):
                        if (feature[19]<=0.0):
                            if (feature[29]<=0.0):
                                bin_num[17] = 56
                            else:
                                bin_num[17] = 57
                        else:
                            if (feature[11]<=0.0):
                                bin_num[17] = 58
                            else:
                                bin_num[17] = 59
                    else:
                        if (feature[2]<=3.0):
                            if (feature[10]<=1.0):
                                bin_num[17] = 60
                            else:
                                bin_num[17] = 61
                        else:
                            if (feature[21]<=0.0):
                                bin_num[17] = 62
                            else:
                                bin_num[17] = 63
    else:
        if (feature[6]<=2.0):
            if (feature[18]<=0.0):
                if (feature[34]<=0.0):
                    if (feature[35]<=0.0):
                        if (feature[19]<=0.0):
                            if (feature[4]<=2635.0):
                                bin_num[17] = 64
                            else:
                                bin_num[17] = 65
                        else:
                            if (feature[25]<=0.0):
                                bin_num[17] = 66
                            else:
                                bin_num[17] = 67
                    else:
                        if (feature[26]<=0.0):
                            if (feature[24]<=0.0):
                                bin_num[17] = 68
                            else:
                                bin_num[17] = 69
                        else:
                            if (feature[12]<=2.0):
                                bin_num[17] = 70
                            else:
                                bin_num[17] = 71
                else:
                    if (feature[26]<=0.0):
                        if (feature[21]<=0.0):
                            if (feature[27]<=0.0):
                                bin_num[17] = 72
                            else:
                                bin_num[17] = 73
                        else:
                            if (feature[9]<=0.0):
                                bin_num[17] = 74
                            else:
                                bin_num[17] = 75
                    else:
                        if (feature[23]<=0.0):
                            if (feature[28]<=0.0):
                                bin_num[17] = 76
                            else:
                                bin_num[17] = 77
                        else:
                            if (feature[25]<=0.0):
                                bin_num[17] = 78
                            else:
                                bin_num[17] = 79
            else:
                if (feature[19]<=0.0):
                    if (feature[24]<=0.0):
                        if (feature[28]<=0.0):
                            if (feature[29]<=0.0):
                                bin_num[17] = 80
                            else:
                                bin_num[17] = 81
                        else:
                            if (feature[26]<=0.0):
                                bin_num[17] = 82
                            else:
                                bin_num[17] = 83
                    else:
                        if (feature[35]<=0.0):
                            if (feature[13]<=0.0):
                                bin_num[17] = 84
                            else:
                                bin_num[17] = 85
                        else:
                            if (feature[4]<=2635.0):
                                bin_num[17] = 86
                            else:
                                bin_num[17] = 87
                else:
                    if (feature[35]<=0.0):
                        if (feature[27]<=0.0):
                            if (feature[29]<=0.0):
                                bin_num[17] = 88
                            else:
                                bin_num[17] = 89
                        else:
                            if (feature[21]<=0.0):
                                bin_num[17] = 90
                            else:
                                bin_num[17] = 91
                    else:
                        if (feature[4]<=2635.0):
                            if (feature[7]<=7.0):
                                bin_num[17] = 92
                            else:
                                bin_num[17] = 93
                        else:
                            if (feature[2]<=3.0):
                                bin_num[17] = 94
                            else:
                                bin_num[17] = 95
        else:
            if (feature[29]<=0.0):
                if (feature[10]<=1.0):
                    if (feature[5]<=16.0):
                        if (feature[13]<=0.0):
                            if (feature[0]<=0.0):
                                bin_num[17] = 96
                            else:
                                bin_num[17] = 97
                        else:
                            if (feature[8]<=35.0):
                                bin_num[17] = 98
                            else:
                                bin_num[17] = 99
                    else:
                        if (feature[8]<=35.0):
                            if (feature[18]<=0.0):
                                bin_num[17] = 100
                            else:
                                bin_num[17] = 101
                        else:
                            if (feature[3]<=2.0):
                                bin_num[17] = 102
                            else:
                                bin_num[17] = 103
                else:
                    if (feature[38]<=0.0):
                        if (feature[36]<=0.0):
                            if (feature[18]<=0.0):
                                bin_num[17] = 104
                            else:
                                bin_num[17] = 105
                        else:
                            if (feature[8]<=35.0):
                                bin_num[17] = 106
                            else:
                                bin_num[17] = 107
                    else:
                        if (feature[9]<=0.0):
                            if (feature[8]<=35.0):
                                bin_num[17] = 108
                            else:
                                bin_num[17] = 109
                        else:
                            if (feature[8]<=35.0):
                                bin_num[17] = 110
                            else:
                                bin_num[17] = 111
            else:
                if (feature[34]<=0.0):
                    if (feature[2]<=3.0):
                        if (feature[28]<=0.0):
                            if (feature[21]<=0.0):
                                bin_num[17] = 112
                            else:
                                bin_num[17] = 113
                        else:
                            if (feature[4]<=2635.0):
                                bin_num[17] = 114
                            else:
                                bin_num[17] = 115
                    else:
                        if (feature[5]<=16.0):
                            if (feature[23]<=0.0):
                                bin_num[17] = 116
                            else:
                                bin_num[17] = 117
                        else:
                            if (feature[18]<=0.0):
                                bin_num[17] = 118
                            else:
                                bin_num[17] = 119
                else:
                    if (feature[21]<=0.0):
                        if (feature[5]<=16.0):
                            if (feature[11]<=0.0):
                                bin_num[17] = 120
                            else:
                                bin_num[17] = 121
                        else:
                            if (feature[1]<=2.0):
                                bin_num[17] = 122
                            else:
                                bin_num[17] = 123
                    else:
                        if (feature[17]<=0.0):
                            if (feature[36]<=0.0):
                                bin_num[17] = 124
                            else:
                                bin_num[17] = 125
                        else:
                            if (feature[37]<=0.0):
                                bin_num[17] = 126
                            else:
                                bin_num[17] = 127
    # Tree 18
    if (feature[4]<=2756.0):
        if (feature[13]<=0.0):
            if (feature[25]<=0.0):
                if (feature[24]<=0.0):
                    if (feature[37]<=0.0):
                        if (feature[2]<=3.0):
                            if (feature[28]<=0.0):
                                bin_num[18] = 0
                            else:
                                bin_num[18] = 1
                        else:
                            if (feature[18]<=0.0):
                                bin_num[18] = 2
                            else:
                                bin_num[18] = 3
                    else:
                        if (feature[34]<=0.0):
                            if (feature[22]<=0.0):
                                bin_num[18] = 4
                            else:
                                bin_num[18] = 5
                        else:
                            if (feature[2]<=3.0):
                                bin_num[18] = 6
                            else:
                                bin_num[18] = 7
                else:
                    if (feature[35]<=0.0):
                        if (feature[18]<=0.0):
                            if (feature[37]<=0.0):
                                bin_num[18] = 8
                            else:
                                bin_num[18] = 9
                        else:
                            if (feature[34]<=0.0):
                                bin_num[18] = 10
                            else:
                                bin_num[18] = 11
                    else:
                        if (feature[18]<=0.0):
                            if (feature[37]<=0.0):
                                bin_num[18] = 12
                            else:
                                bin_num[18] = 13
                        else:
                            if (feature[33]<=0.0):
                                bin_num[18] = 14
                            else:
                                bin_num[18] = 15
            else:
                if (feature[28]<=0.0):
                    if (feature[38]<=0.0):
                        if (feature[34]<=0.0):
                            if (feature[21]<=0.0):
                                bin_num[18] = 16
                            else:
                                bin_num[18] = 17
                        else:
                            if (feature[21]<=0.0):
                                bin_num[18] = 18
                            else:
                                bin_num[18] = 19
                    else:
                        if (feature[5]<=15.0):
                            if (feature[27]<=0.0):
                                bin_num[18] = 20
                            else:
                                bin_num[18] = 21
                        else:
                            if (feature[34]<=0.0):
                                bin_num[18] = 22
                            else:
                                bin_num[18] = 23
                else:
                    if (feature[23]<=0.0):
                        if (feature[9]<=0.0):
                            if (feature[5]<=15.0):
                                bin_num[18] = 24
                            else:
                                bin_num[18] = 25
                        else:
                            if (feature[20]<=0.0):
                                bin_num[18] = 26
                            else:
                                bin_num[18] = 27
                    else:
                        if (feature[2]<=3.0):
                            if (feature[5]<=15.0):
                                bin_num[18] = 28
                            else:
                                bin_num[18] = 29
                        else:
                            if (feature[0]<=0.0):
                                bin_num[18] = 30
                            else:
                                bin_num[18] = 31
        else:
            if (feature[1]<=2.0):
                if (feature[34]<=0.0):
                    if (feature[9]<=0.0):
                        if (feature[12]<=2.0):
                            if (feature[3]<=2.0):
                                bin_num[18] = 32
                            else:
                                bin_num[18] = 33
                        else:
                            if (feature[5]<=15.0):
                                bin_num[18] = 34
                            else:
                                bin_num[18] = 35
                    else:
                        if (feature[33]<=0.0):
                            if (feature[23]<=0.0):
                                bin_num[18] = 36
                            else:
                                bin_num[18] = 37
                        else:
                            if (feature[29]<=0.0):
                                bin_num[18] = 38
                            else:
                                bin_num[18] = 39
                else:
                    if (feature[26]<=0.0):
                        if (feature[21]<=0.0):
                            if (feature[3]<=2.0):
                                bin_num[18] = 40
                            else:
                                bin_num[18] = 41
                        else:
                            if (feature[22]<=0.0):
                                bin_num[18] = 42
                            else:
                                bin_num[18] = 43
                    else:
                        if (feature[21]<=0.0):
                            if (feature[33]<=0.0):
                                bin_num[18] = 44
                            else:
                                bin_num[18] = 45
                        else:
                            if (feature[22]<=0.0):
                                bin_num[18] = 46
                            else:
                                bin_num[18] = 47
            else:
                if (feature[20]<=0.0):
                    if (feature[29]<=0.0):
                        if (feature[23]<=0.0):
                            if (feature[0]<=0.0):
                                bin_num[18] = 48
                            else:
                                bin_num[18] = 49
                        else:
                            if (feature[11]<=0.0):
                                bin_num[18] = 50
                            else:
                                bin_num[18] = 51
                    else:
                        if (feature[22]<=0.0):
                            if (feature[28]<=0.0):
                                bin_num[18] = 52
                            else:
                                bin_num[18] = 53
                        else:
                            if (feature[10]<=1.0):
                                bin_num[18] = 54
                            else:
                                bin_num[18] = 55
                else:
                    if (feature[18]<=0.0):
                        if (feature[12]<=2.0):
                            if (feature[34]<=0.0):
                                bin_num[18] = 56
                            else:
                                bin_num[18] = 57
                        else:
                            if (feature[37]<=0.0):
                                bin_num[18] = 58
                            else:
                                bin_num[18] = 59
                    else:
                        if (feature[27]<=0.0):
                            if (feature[26]<=0.0):
                                bin_num[18] = 60
                            else:
                                bin_num[18] = 61
                        else:
                            if (feature[19]<=0.0):
                                bin_num[18] = 62
                            else:
                                bin_num[18] = 63
    else:
        if (feature[7]<=7.0):
            if (feature[34]<=0.0):
                if (feature[2]<=3.0):
                    if (feature[20]<=0.0):
                        if (feature[33]<=0.0):
                            if (feature[22]<=0.0):
                                bin_num[18] = 64
                            else:
                                bin_num[18] = 65
                        else:
                            if (feature[26]<=0.0):
                                bin_num[18] = 66
                            else:
                                bin_num[18] = 67
                    else:
                        if (feature[5]<=15.0):
                            if (feature[1]<=2.0):
                                bin_num[18] = 68
                            else:
                                bin_num[18] = 69
                        else:
                            if (feature[10]<=1.0):
                                bin_num[18] = 70
                            else:
                                bin_num[18] = 71
                else:
                    if (feature[10]<=1.0):
                        if (feature[18]<=0.0):
                            if (feature[37]<=0.0):
                                bin_num[18] = 72
                            else:
                                bin_num[18] = 73
                        else:
                            if (feature[19]<=0.0):
                                bin_num[18] = 74
                            else:
                                bin_num[18] = 75
                    else:
                        if (feature[28]<=0.0):
                            if (feature[27]<=0.0):
                                bin_num[18] = 76
                            else:
                                bin_num[18] = 77
                        else:
                            if (feature[37]<=0.0):
                                bin_num[18] = 78
                            else:
                                bin_num[18] = 79
            else:
                if (feature[26]<=0.0):
                    if (feature[6]<=2.0):
                        if (feature[20]<=0.0):
                            if (feature[1]<=2.0):
                                bin_num[18] = 80
                            else:
                                bin_num[18] = 81
                        else:
                            if (feature[21]<=0.0):
                                bin_num[18] = 82
                            else:
                                bin_num[18] = 83
                    else:
                        if (feature[18]<=0.0):
                            if (feature[28]<=0.0):
                                bin_num[18] = 84
                            else:
                                bin_num[18] = 85
                        else:
                            if (feature[13]<=0.0):
                                bin_num[18] = 86
                            else:
                                bin_num[18] = 87
                else:
                    if (feature[13]<=0.0):
                        if (feature[8]<=33.0):
                            if (feature[17]<=0.0):
                                bin_num[18] = 88
                            else:
                                bin_num[18] = 89
                        else:
                            if (feature[25]<=0.0):
                                bin_num[18] = 90
                            else:
                                bin_num[18] = 91
                    else:
                        if (feature[23]<=0.0):
                            if (feature[25]<=0.0):
                                bin_num[18] = 92
                            else:
                                bin_num[18] = 93
                        else:
                            if (feature[36]<=0.0):
                                bin_num[18] = 94
                            else:
                                bin_num[18] = 95
        else:
            if (feature[5]<=15.0):
                if (feature[13]<=0.0):
                    if (feature[27]<=0.0):
                        if (feature[29]<=0.0):
                            if (feature[26]<=0.0):
                                bin_num[18] = 96
                            else:
                                bin_num[18] = 97
                        else:
                            if (feature[3]<=2.0):
                                bin_num[18] = 98
                            else:
                                bin_num[18] = 99
                    else:
                        if (feature[22]<=0.0):
                            if (feature[18]<=0.0):
                                bin_num[18] = 100
                            else:
                                bin_num[18] = 101
                        else:
                            if (feature[6]<=2.0):
                                bin_num[18] = 102
                            else:
                                bin_num[18] = 103
                else:
                    if (feature[12]<=2.0):
                        if (feature[2]<=3.0):
                            if (feature[26]<=0.0):
                                bin_num[18] = 104
                            else:
                                bin_num[18] = 105
                        else:
                            if (feature[10]<=1.0):
                                bin_num[18] = 106
                            else:
                                bin_num[18] = 107
                    else:
                        if (feature[6]<=2.0):
                            if (feature[3]<=2.0):
                                bin_num[18] = 108
                            else:
                                bin_num[18] = 109
                        else:
                            if (feature[10]<=1.0):
                                bin_num[18] = 110
                            else:
                                bin_num[18] = 111
            else:
                if (feature[8]<=33.0):
                    if (feature[29]<=0.0):
                        if (feature[21]<=0.0):
                            if (feature[26]<=0.0):
                                bin_num[18] = 112
                            else:
                                bin_num[18] = 113
                        else:
                            if (feature[12]<=2.0):
                                bin_num[18] = 114
                            else:
                                bin_num[18] = 115
                    else:
                        if (feature[12]<=2.0):
                            if (feature[2]<=3.0):
                                bin_num[18] = 116
                            else:
                                bin_num[18] = 117
                        else:
                            if (feature[20]<=0.0):
                                bin_num[18] = 118
                            else:
                                bin_num[18] = 119
                else:
                    if (feature[26]<=0.0):
                        if (feature[34]<=0.0):
                            if (feature[10]<=1.0):
                                bin_num[18] = 120
                            else:
                                bin_num[18] = 121
                        else:
                            if (feature[20]<=0.0):
                                bin_num[18] = 122
                            else:
                                bin_num[18] = 123
                    else:
                        if (feature[2]<=3.0):
                            if (feature[21]<=0.0):
                                bin_num[18] = 124
                            else:
                                bin_num[18] = 125
                        else:
                            if (feature[10]<=1.0):
                                bin_num[18] = 126
                            else:
                                bin_num[18] = 127
    # Tree 19
    if (feature[6]<=3.0):
        if (feature[8]<=34.0):
            if (feature[36]<=0.0):
                if (feature[17]<=0.0):
                    if (feature[38]<=0.0):
                        if (feature[11]<=0.0):
                            if (feature[5]<=15.0):
                                bin_num[19] = 0
                            else:
                                bin_num[19] = 1
                        else:
                            if (feature[23]<=0.0):
                                bin_num[19] = 2
                            else:
                                bin_num[19] = 3
                    else:
                        if (feature[7]<=7.0):
                            if (feature[13]<=0.0):
                                bin_num[19] = 4
                            else:
                                bin_num[19] = 5
                        else:
                            if (feature[12]<=2.0):
                                bin_num[19] = 6
                            else:
                                bin_num[19] = 7
                else:
                    if (feature[5]<=15.0):
                        if (feature[4]<=2688.0):
                            if (feature[10]<=1.0):
                                bin_num[19] = 8
                            else:
                                bin_num[19] = 9
                        else:
                            if (feature[10]<=1.0):
                                bin_num[19] = 10
                            else:
                                bin_num[19] = 11
                    else:
                        if (feature[13]<=0.0):
                            if (feature[23]<=0.0):
                                bin_num[19] = 12
                            else:
                                bin_num[19] = 13
                        else:
                            if (feature[37]<=0.0):
                                bin_num[19] = 14
                            else:
                                bin_num[19] = 15
            else:
                if (feature[7]<=7.0):
                    if (feature[13]<=0.0):
                        if (feature[5]<=15.0):
                            if (feature[12]<=2.0):
                                bin_num[19] = 16
                            else:
                                bin_num[19] = 17
                        else:
                            if (feature[23]<=0.0):
                                bin_num[19] = 18
                            else:
                                bin_num[19] = 19
                    else:
                        if (feature[10]<=1.0):
                            if (feature[29]<=0.0):
                                bin_num[19] = 20
                            else:
                                bin_num[19] = 21
                        else:
                            if (feature[5]<=15.0):
                                bin_num[19] = 22
                            else:
                                bin_num[19] = 23
                else:
                    if (feature[13]<=0.0):
                        if (feature[22]<=0.0):
                            if (feature[34]<=0.0):
                                bin_num[19] = 24
                            else:
                                bin_num[19] = 25
                        else:
                            if (feature[29]<=0.0):
                                bin_num[19] = 26
                            else:
                                bin_num[19] = 27
                    else:
                        if (feature[18]<=0.0):
                            if (feature[25]<=0.0):
                                bin_num[19] = 28
                            else:
                                bin_num[19] = 29
                        else:
                            if (feature[5]<=15.0):
                                bin_num[19] = 30
                            else:
                                bin_num[19] = 31
        else:
            if (feature[5]<=15.0):
                if (feature[10]<=1.0):
                    if (feature[9]<=0.0):
                        if (feature[29]<=0.0):
                            if (feature[27]<=0.0):
                                bin_num[19] = 32
                            else:
                                bin_num[19] = 33
                        else:
                            if (feature[13]<=0.0):
                                bin_num[19] = 34
                            else:
                                bin_num[19] = 35
                    else:
                        if (feature[12]<=2.0):
                            if (feature[1]<=2.0):
                                bin_num[19] = 36
                            else:
                                bin_num[19] = 37
                        else:
                            if (feature[38]<=0.0):
                                bin_num[19] = 38
                            else:
                                bin_num[19] = 39
                else:
                    if (feature[18]<=0.0):
                        if (feature[38]<=0.0):
                            if (feature[3]<=2.0):
                                bin_num[19] = 40
                            else:
                                bin_num[19] = 41
                        else:
                            if (feature[37]<=0.0):
                                bin_num[19] = 42
                            else:
                                bin_num[19] = 43
                    else:
                        if (feature[12]<=2.0):
                            if (feature[36]<=0.0):
                                bin_num[19] = 44
                            else:
                                bin_num[19] = 45
                        else:
                            if (feature[4]<=2688.0):
                                bin_num[19] = 46
                            else:
                                bin_num[19] = 47
            else:
                if (feature[10]<=1.0):
                    if (feature[3]<=2.0):
                        if (feature[38]<=0.0):
                            if (feature[29]<=0.0):
                                bin_num[19] = 48
                            else:
                                bin_num[19] = 49
                        else:
                            if (feature[18]<=0.0):
                                bin_num[19] = 50
                            else:
                                bin_num[19] = 51
                    else:
                        if (feature[38]<=0.0):
                            if (feature[2]<=3.0):
                                bin_num[19] = 52
                            else:
                                bin_num[19] = 53
                        else:
                            if (feature[24]<=0.0):
                                bin_num[19] = 54
                            else:
                                bin_num[19] = 55
                else:
                    if (feature[36]<=0.0):
                        if (feature[17]<=0.0):
                            if (feature[23]<=0.0):
                                bin_num[19] = 56
                            else:
                                bin_num[19] = 57
                        else:
                            if (feature[18]<=0.0):
                                bin_num[19] = 58
                            else:
                                bin_num[19] = 59
                    else:
                        if (feature[2]<=3.0):
                            if (feature[22]<=0.0):
                                bin_num[19] = 60
                            else:
                                bin_num[19] = 61
                        else:
                            if (feature[18]<=0.0):
                                bin_num[19] = 62
                            else:
                                bin_num[19] = 63
    else:
        if (feature[10]<=1.0):
            if (feature[8]<=34.0):
                if (feature[13]<=0.0):
                    if (feature[23]<=0.0):
                        if (feature[5]<=15.0):
                            if (feature[2]<=3.0):
                                bin_num[19] = 64
                            else:
                                bin_num[19] = 65
                        else:
                            if (feature[25]<=0.0):
                                bin_num[19] = 66
                            else:
                                bin_num[19] = 67
                    else:
                        if (feature[0]<=0.0):
                            if (feature[21]<=0.0):
                                bin_num[19] = 68
                            else:
                                bin_num[19] = 69
                        else:
                            if (feature[18]<=0.0):
                                bin_num[19] = 70
                            else:
                                bin_num[19] = 71
                else:
                    if (feature[29]<=0.0):
                        if (feature[21]<=0.0):
                            if (feature[37]<=0.0):
                                bin_num[19] = 72
                            else:
                                bin_num[19] = 73
                        else:
                            if (feature[18]<=0.0):
                                bin_num[19] = 74
                            else:
                                bin_num[19] = 75
                    else:
                        if (feature[2]<=3.0):
                            if (feature[37]<=0.0):
                                bin_num[19] = 76
                            else:
                                bin_num[19] = 77
                        else:
                            if (feature[18]<=0.0):
                                bin_num[19] = 78
                            else:
                                bin_num[19] = 79
            else:
                if (feature[5]<=15.0):
                    if (feature[9]<=0.0):
                        if (feature[12]<=2.0):
                            if (feature[27]<=0.0):
                                bin_num[19] = 80
                            else:
                                bin_num[19] = 81
                        else:
                            if (feature[27]<=0.0):
                                bin_num[19] = 82
                            else:
                                bin_num[19] = 83
                    else:
                        if (feature[12]<=2.0):
                            if (feature[34]<=0.0):
                                bin_num[19] = 84
                            else:
                                bin_num[19] = 85
                        else:
                            if (feature[7]<=7.0):
                                bin_num[19] = 86
                            else:
                                bin_num[19] = 87
                else:
                    if (feature[7]<=7.0):
                        if (feature[17]<=0.0):
                            if (feature[37]<=0.0):
                                bin_num[19] = 88
                            else:
                                bin_num[19] = 89
                        else:
                            if (feature[4]<=2688.0):
                                bin_num[19] = 90
                            else:
                                bin_num[19] = 91
                    else:
                        if (feature[2]<=3.0):
                            if (feature[26]<=0.0):
                                bin_num[19] = 92
                            else:
                                bin_num[19] = 93
                        else:
                            if (feature[3]<=2.0):
                                bin_num[19] = 94
                            else:
                                bin_num[19] = 95
        else:
            if (feature[36]<=0.0):
                if (feature[38]<=0.0):
                    if (feature[23]<=0.0):
                        if (feature[25]<=0.0):
                            if (feature[35]<=0.0):
                                bin_num[19] = 96
                            else:
                                bin_num[19] = 97
                        else:
                            if (feature[17]<=0.0):
                                bin_num[19] = 98
                            else:
                                bin_num[19] = 99
                    else:
                        if (feature[18]<=0.0):
                            if (feature[22]<=0.0):
                                bin_num[19] = 100
                            else:
                                bin_num[19] = 101
                        else:
                            if (feature[11]<=0.0):
                                bin_num[19] = 102
                            else:
                                bin_num[19] = 103
                else:
                    if (feature[0]<=0.0):
                        if (feature[8]<=34.0):
                            if (feature[5]<=15.0):
                                bin_num[19] = 104
                            else:
                                bin_num[19] = 105
                        else:
                            if (feature[20]<=0.0):
                                bin_num[19] = 106
                            else:
                                bin_num[19] = 107
                    else:
                        if (feature[37]<=0.0):
                            if (feature[8]<=34.0):
                                bin_num[19] = 108
                            else:
                                bin_num[19] = 109
                        else:
                            if (feature[8]<=34.0):
                                bin_num[19] = 110
                            else:
                                bin_num[19] = 111
            else:
                if (feature[8]<=34.0):
                    if (feature[0]<=0.0):
                        if (feature[5]<=15.0):
                            if (feature[37]<=0.0):
                                bin_num[19] = 112
                            else:
                                bin_num[19] = 113
                        else:
                            if (feature[12]<=2.0):
                                bin_num[19] = 114
                            else:
                                bin_num[19] = 115
                    else:
                        if (feature[37]<=0.0):
                            if (feature[1]<=2.0):
                                bin_num[19] = 116
                            else:
                                bin_num[19] = 117
                        else:
                            if (feature[33]<=0.0):
                                bin_num[19] = 118
                            else:
                                bin_num[19] = 119
                else:
                    if (feature[0]<=0.0):
                        if (feature[2]<=3.0):
                            if (feature[7]<=7.0):
                                bin_num[19] = 120
                            else:
                                bin_num[19] = 121
                        else:
                            if (feature[37]<=0.0):
                                bin_num[19] = 122
                            else:
                                bin_num[19] = 123
                    else:
                        if (feature[37]<=0.0):
                            if (feature[12]<=2.0):
                                bin_num[19] = 124
                            else:
                                bin_num[19] = 125
                        else:
                            if (feature[21]<=0.0):
                                bin_num[19] = 126
                            else:
                                bin_num[19] = 127
    # Tree 20
    if (feature[6]<=3.0):
        if (feature[8]<=34.0):
            if (feature[34]<=0.0):
                if (feature[7]<=7.0):
                    if (feature[36]<=0.0):
                        if (feature[17]<=0.0):
                            if (feature[38]<=0.0):
                                bin_num[20] = 0
                            else:
                                bin_num[20] = 1
                        else:
                            if (feature[23]<=0.0):
                                bin_num[20] = 2
                            else:
                                bin_num[20] = 3
                    else:
                        if (feature[18]<=0.0):
                            if (feature[35]<=0.0):
                                bin_num[20] = 4
                            else:
                                bin_num[20] = 5
                        else:
                            if (feature[20]<=0.0):
                                bin_num[20] = 6
                            else:
                                bin_num[20] = 7
                else:
                    if (feature[13]<=0.0):
                        if (feature[5]<=16.0):
                            if (feature[22]<=0.0):
                                bin_num[20] = 8
                            else:
                                bin_num[20] = 9
                        else:
                            if (feature[17]<=0.0):
                                bin_num[20] = 10
                            else:
                                bin_num[20] = 11
                    else:
                        if (feature[4]<=2652.0):
                            if (feature[9]<=0.0):
                                bin_num[20] = 12
                            else:
                                bin_num[20] = 13
                        else:
                            if (feature[5]<=16.0):
                                bin_num[20] = 14
                            else:
                                bin_num[20] = 15
            else:
                if (feature[26]<=0.0):
                    if (feature[4]<=2652.0):
                        if (feature[1]<=2.0):
                            if (feature[18]<=0.0):
                                bin_num[20] = 16
                            else:
                                bin_num[20] = 17
                        else:
                            if (feature[33]<=0.0):
                                bin_num[20] = 18
                            else:
                                bin_num[20] = 19
                    else:
                        if (feature[20]<=0.0):
                            if (feature[13]<=0.0):
                                bin_num[20] = 20
                            else:
                                bin_num[20] = 21
                        else:
                            if (feature[21]<=0.0):
                                bin_num[20] = 22
                            else:
                                bin_num[20] = 23
                else:
                    if (feature[13]<=0.0):
                        if (feature[37]<=0.0):
                            if (feature[22]<=0.0):
                                bin_num[20] = 24
                            else:
                                bin_num[20] = 25
                        else:
                            if (feature[23]<=0.0):
                                bin_num[20] = 26
                            else:
                                bin_num[20] = 27
                    else:
                        if (feature[23]<=0.0):
                            if (feature[2]<=3.0):
                                bin_num[20] = 28
                            else:
                                bin_num[20] = 29
                        else:
                            if (feature[22]<=0.0):
                                bin_num[20] = 30
                            else:
                                bin_num[20] = 31
        else:
            if (feature[5]<=16.0):
                if (feature[13]<=0.0):
                    if (feature[17]<=0.0):
                        if (feature[18]<=0.0):
                            if (feature[38]<=0.0):
                                bin_num[20] = 32
                            else:
                                bin_num[20] = 33
                        else:
                            if (feature[19]<=0.0):
                                bin_num[20] = 34
                            else:
                                bin_num[20] = 35
                    else:
                        if (feature[12]<=2.0):
                            if (feature[21]<=0.0):
                                bin_num[20] = 36
                            else:
                                bin_num[20] = 37
                        else:
                            if (feature[2]<=3.0):
                                bin_num[20] = 38
                            else:
                                bin_num[20] = 39
                else:
                    if (feature[10]<=1.0):
                        if (feature[9]<=0.0):
                            if (feature[22]<=0.0):
                                bin_num[20] = 40
                            else:
                                bin_num[20] = 41
                        else:
                            if (feature[12]<=2.0):
                                bin_num[20] = 42
                            else:
                                bin_num[20] = 43
                    else:
                        if (feature[18]<=0.0):
                            if (feature[4]<=2652.0):
                                bin_num[20] = 44
                            else:
                                bin_num[20] = 45
                        else:
                            if (feature[12]<=2.0):
                                bin_num[20] = 46
                            else:
                                bin_num[20] = 47
            else:
                if (feature[10]<=1.0):
                    if (feature[3]<=2.0):
                        if (feature[38]<=0.0):
                            if (feature[18]<=0.0):
                                bin_num[20] = 48
                            else:
                                bin_num[20] = 49
                        else:
                            if (feature[18]<=0.0):
                                bin_num[20] = 50
                            else:
                                bin_num[20] = 51
                    else:
                        if (feature[38]<=0.0):
                            if (feature[20]<=0.0):
                                bin_num[20] = 52
                            else:
                                bin_num[20] = 53
                        else:
                            if (feature[9]<=0.0):
                                bin_num[20] = 54
                            else:
                                bin_num[20] = 55
                else:
                    if (feature[9]<=0.0):
                        if (feature[38]<=0.0):
                            if (feature[29]<=0.0):
                                bin_num[20] = 56
                            else:
                                bin_num[20] = 57
                        else:
                            if (feature[1]<=2.0):
                                bin_num[20] = 58
                            else:
                                bin_num[20] = 59
                    else:
                        if (feature[36]<=0.0):
                            if (feature[29]<=0.0):
                                bin_num[20] = 60
                            else:
                                bin_num[20] = 61
                        else:
                            if (feature[23]<=0.0):
                                bin_num[20] = 62
                            else:
                                bin_num[20] = 63
    else:
        if (feature[10]<=1.0):
            if (feature[5]<=16.0):
                if (feature[8]<=34.0):
                    if (feature[13]<=0.0):
                        if (feature[0]<=0.0):
                            if (feature[26]<=0.0):
                                bin_num[20] = 64
                            else:
                                bin_num[20] = 65
                        else:
                            if (feature[18]<=0.0):
                                bin_num[20] = 66
                            else:
                                bin_num[20] = 67
                    else:
                        if (feature[36]<=0.0):
                            if (feature[34]<=0.0):
                                bin_num[20] = 68
                            else:
                                bin_num[20] = 69
                        else:
                            if (feature[7]<=7.0):
                                bin_num[20] = 70
                            else:
                                bin_num[20] = 71
                else:
                    if (feature[9]<=0.0):
                        if (feature[12]<=2.0):
                            if (feature[27]<=0.0):
                                bin_num[20] = 72
                            else:
                                bin_num[20] = 73
                        else:
                            if (feature[29]<=0.0):
                                bin_num[20] = 74
                            else:
                                bin_num[20] = 75
                    else:
                        if (feature[12]<=2.0):
                            if (feature[34]<=0.0):
                                bin_num[20] = 76
                            else:
                                bin_num[20] = 77
                        else:
                            if (feature[7]<=7.0):
                                bin_num[20] = 78
                            else:
                                bin_num[20] = 79
            else:
                if (feature[8]<=34.0):
                    if (feature[13]<=0.0):
                        if (feature[23]<=0.0):
                            if (feature[25]<=0.0):
                                bin_num[20] = 80
                            else:
                                bin_num[20] = 81
                        else:
                            if (feature[21]<=0.0):
                                bin_num[20] = 82
                            else:
                                bin_num[20] = 83
                    else:
                        if (feature[20]<=0.0):
                            if (feature[9]<=0.0):
                                bin_num[20] = 84
                            else:
                                bin_num[20] = 85
                        else:
                            if (feature[29]<=0.0):
                                bin_num[20] = 86
                            else:
                                bin_num[20] = 87
                else:
                    if (feature[3]<=2.0):
                        if (feature[17]<=0.0):
                            if (feature[20]<=0.0):
                                bin_num[20] = 88
                            else:
                                bin_num[20] = 89
                        else:
                            if (feature[23]<=0.0):
                                bin_num[20] = 90
                            else:
                                bin_num[20] = 91
                    else:
                        if (feature[2]<=3.0):
                            if (feature[26]<=0.0):
                                bin_num[20] = 92
                            else:
                                bin_num[20] = 93
                        else:
                            if (feature[12]<=2.0):
                                bin_num[20] = 94
                            else:
                                bin_num[20] = 95
        else:
            if (feature[36]<=0.0):
                if (feature[38]<=0.0):
                    if (feature[23]<=0.0):
                        if (feature[25]<=0.0):
                            if (feature[35]<=0.0):
                                bin_num[20] = 96
                            else:
                                bin_num[20] = 97
                        else:
                            if (feature[17]<=0.0):
                                bin_num[20] = 98
                            else:
                                bin_num[20] = 99
                    else:
                        if (feature[26]<=0.0):
                            if (feature[29]<=0.0):
                                bin_num[20] = 100
                            else:
                                bin_num[20] = 101
                        else:
                            if (feature[28]<=0.0):
                                bin_num[20] = 102
                            else:
                                bin_num[20] = 103
                else:
                    if (feature[0]<=0.0):
                        if (feature[8]<=34.0):
                            if (feature[5]<=16.0):
                                bin_num[20] = 104
                            else:
                                bin_num[20] = 105
                        else:
                            if (feature[20]<=0.0):
                                bin_num[20] = 106
                            else:
                                bin_num[20] = 107
                    else:
                        if (feature[37]<=0.0):
                            if (feature[8]<=34.0):
                                bin_num[20] = 108
                            else:
                                bin_num[20] = 109
                        else:
                            if (feature[8]<=34.0):
                                bin_num[20] = 110
                            else:
                                bin_num[20] = 111
            else:
                if (feature[8]<=34.0):
                    if (feature[0]<=0.0):
                        if (feature[33]<=0.0):
                            if (feature[28]<=0.0):
                                bin_num[20] = 112
                            else:
                                bin_num[20] = 113
                        else:
                            if (feature[19]<=0.0):
                                bin_num[20] = 114
                            else:
                                bin_num[20] = 115
                    else:
                        if (feature[37]<=0.0):
                            if (feature[12]<=2.0):
                                bin_num[20] = 116
                            else:
                                bin_num[20] = 117
                        else:
                            if (feature[27]<=0.0):
                                bin_num[20] = 118
                            else:
                                bin_num[20] = 119
                else:
                    if (feature[0]<=0.0):
                        if (feature[37]<=0.0):
                            if (feature[2]<=3.0):
                                bin_num[20] = 120
                            else:
                                bin_num[20] = 121
                        else:
                            if (feature[3]<=2.0):
                                bin_num[20] = 122
                            else:
                                bin_num[20] = 123
                    else:
                        if (feature[37]<=0.0):
                            if (feature[2]<=3.0):
                                bin_num[20] = 124
                            else:
                                bin_num[20] = 125
                        else:
                            if (feature[5]<=16.0):
                                bin_num[20] = 126
                            else:
                                bin_num[20] = 127
    # Tree 21
    if (feature[20]<=0.0):
        if (feature[18]<=0.0):
            if (feature[37]<=0.0):
                if (feature[4]<=2646.0):
                    if (feature[1]<=2.0):
                        if (feature[22]<=0.0):
                            if (feature[27]<=0.0):
                                bin_num[21] = 0
                            else:
                                bin_num[21] = 1
                        else:
                            if (feature[26]<=0.0):
                                bin_num[21] = 2
                            else:
                                bin_num[21] = 3
                    else:
                        if (feature[13]<=0.0):
                            if (feature[25]<=0.0):
                                bin_num[21] = 4
                            else:
                                bin_num[21] = 5
                        else:
                            if (feature[5]<=14.0):
                                bin_num[21] = 6
                            else:
                                bin_num[21] = 7
                else:
                    if (feature[25]<=0.0):
                        if (feature[23]<=0.0):
                            if (feature[22]<=0.0):
                                bin_num[21] = 8
                            else:
                                bin_num[21] = 9
                        else:
                            if (feature[6]<=2.0):
                                bin_num[21] = 10
                            else:
                                bin_num[21] = 11
                    else:
                        if (feature[8]<=33.0):
                            if (feature[29]<=0.0):
                                bin_num[21] = 12
                            else:
                                bin_num[21] = 13
                        else:
                            if (feature[19]<=0.0):
                                bin_num[21] = 14
                            else:
                                bin_num[21] = 15
            else:
                if (feature[29]<=0.0):
                    if (feature[27]<=0.0):
                        if (feature[33]<=0.0):
                            if (feature[3]<=2.0):
                                bin_num[21] = 16
                            else:
                                bin_num[21] = 17
                        else:
                            if (feature[9]<=0.0):
                                bin_num[21] = 18
                            else:
                                bin_num[21] = 19
                    else:
                        if (feature[22]<=0.0):
                            if (feature[1]<=2.0):
                                bin_num[21] = 20
                            else:
                                bin_num[21] = 21
                        else:
                            if (feature[28]<=0.0):
                                bin_num[21] = 22
                            else:
                                bin_num[21] = 23
                else:
                    if (feature[22]<=0.0):
                        if (feature[28]<=0.0):
                            if (feature[19]<=0.0):
                                bin_num[21] = 24
                            else:
                                bin_num[21] = 25
                        else:
                            if (feature[33]<=0.0):
                                bin_num[21] = 26
                            else:
                                bin_num[21] = 27
                    else:
                        if (feature[1]<=2.0):
                            if (feature[12]<=2.0):
                                bin_num[21] = 28
                            else:
                                bin_num[21] = 29
                        else:
                            if (feature[19]<=0.0):
                                bin_num[21] = 30
                            else:
                                bin_num[21] = 31
        else:
            if (feature[33]<=0.0):
                if (feature[22]<=0.0):
                    if (feature[27]<=0.0):
                        if (feature[23]<=0.0):
                            if (feature[21]<=0.0):
                                bin_num[21] = 32
                            else:
                                bin_num[21] = 33
                        else:
                            if (feature[11]<=0.0):
                                bin_num[21] = 34
                            else:
                                bin_num[21] = 35
                    else:
                        if (feature[21]<=0.0):
                            if (feature[1]<=2.0):
                                bin_num[21] = 36
                            else:
                                bin_num[21] = 37
                        else:
                            if (feature[34]<=0.0):
                                bin_num[21] = 38
                            else:
                                bin_num[21] = 39
                else:
                    if (feature[1]<=2.0):
                        if (feature[3]<=2.0):
                            if (feature[2]<=3.0):
                                bin_num[21] = 40
                            else:
                                bin_num[21] = 41
                        else:
                            if (feature[2]<=3.0):
                                bin_num[21] = 42
                            else:
                                bin_num[21] = 43
                    else:
                        if (feature[34]<=0.0):
                            if (feature[19]<=0.0):
                                bin_num[21] = 44
                            else:
                                bin_num[21] = 45
                        else:
                            if (feature[21]<=0.0):
                                bin_num[21] = 46
                            else:
                                bin_num[21] = 47
            else:
                if (feature[1]<=2.0):
                    if (feature[24]<=0.0):
                        if (feature[27]<=0.0):
                            if (feature[23]<=0.0):
                                bin_num[21] = 48
                            else:
                                bin_num[21] = 49
                        else:
                            if (feature[23]<=0.0):
                                bin_num[21] = 50
                            else:
                                bin_num[21] = 51
                    else:
                        if (feature[21]<=0.0):
                            if (feature[27]<=0.0):
                                bin_num[21] = 52
                            else:
                                bin_num[21] = 53
                        else:
                            if (feature[29]<=0.0):
                                bin_num[21] = 54
                            else:
                                bin_num[21] = 55
                else:
                    if (feature[26]<=0.0):
                        if (feature[19]<=0.0):
                            if (feature[27]<=0.0):
                                bin_num[21] = 56
                            else:
                                bin_num[21] = 57
                        else:
                            if (feature[5]<=14.0):
                                bin_num[21] = 58
                            else:
                                bin_num[21] = 59
                    else:
                        if (feature[9]<=0.0):
                            if (feature[21]<=0.0):
                                bin_num[21] = 60
                            else:
                                bin_num[21] = 61
                        else:
                            if (feature[34]<=0.0):
                                bin_num[21] = 62
                            else:
                                bin_num[21] = 63
    else:
        if (feature[29]<=0.0):
            if (feature[18]<=0.0):
                if (feature[6]<=2.0):
                    if (feature[35]<=0.0):
                        if (feature[21]<=0.0):
                            if (feature[19]<=0.0):
                                bin_num[21] = 64
                            else:
                                bin_num[21] = 65
                        else:
                            if (feature[28]<=0.0):
                                bin_num[21] = 66
                            else:
                                bin_num[21] = 67
                    else:
                        if (feature[28]<=0.0):
                            if (feature[0]<=0.0):
                                bin_num[21] = 68
                            else:
                                bin_num[21] = 69
                        else:
                            if (feature[23]<=0.0):
                                bin_num[21] = 70
                            else:
                                bin_num[21] = 71
                else:
                    if (feature[19]<=0.0):
                        if (feature[35]<=0.0):
                            if (feature[24]<=0.0):
                                bin_num[21] = 72
                            else:
                                bin_num[21] = 73
                        else:
                            if (feature[24]<=0.0):
                                bin_num[21] = 74
                            else:
                                bin_num[21] = 75
                    else:
                        if (feature[21]<=0.0):
                            if (feature[27]<=0.0):
                                bin_num[21] = 76
                            else:
                                bin_num[21] = 77
                        else:
                            if (feature[2]<=3.0):
                                bin_num[21] = 78
                            else:
                                bin_num[21] = 79
            else:
                if (feature[19]<=0.0):
                    if (feature[24]<=0.0):
                        if (feature[28]<=0.0):
                            if (feature[26]<=0.0):
                                bin_num[21] = 80
                            else:
                                bin_num[21] = 81
                        else:
                            if (feature[26]<=0.0):
                                bin_num[21] = 82
                            else:
                                bin_num[21] = 83
                    else:
                        if (feature[35]<=0.0):
                            if (feature[27]<=0.0):
                                bin_num[21] = 84
                            else:
                                bin_num[21] = 85
                        else:
                            if (feature[2]<=3.0):
                                bin_num[21] = 86
                            else:
                                bin_num[21] = 87
                else:
                    if (feature[27]<=0.0):
                        if (feature[4]<=2646.0):
                            if (feature[26]<=0.0):
                                bin_num[21] = 88
                            else:
                                bin_num[21] = 89
                        else:
                            if (feature[35]<=0.0):
                                bin_num[21] = 90
                            else:
                                bin_num[21] = 91
                    else:
                        if (feature[21]<=0.0):
                            if (feature[5]<=14.0):
                                bin_num[21] = 92
                            else:
                                bin_num[21] = 93
                        else:
                            if (feature[2]<=3.0):
                                bin_num[21] = 94
                            else:
                                bin_num[21] = 95
        else:
            if (feature[23]<=0.0):
                if (feature[35]<=0.0):
                    if (feature[1]<=2.0):
                        if (feature[24]<=0.0):
                            if (feature[21]<=0.0):
                                bin_num[21] = 96
                            else:
                                bin_num[21] = 97
                        else:
                            if (feature[34]<=0.0):
                                bin_num[21] = 98
                            else:
                                bin_num[21] = 99
                    else:
                        if (feature[4]<=2646.0):
                            if (feature[28]<=0.0):
                                bin_num[21] = 100
                            else:
                                bin_num[21] = 101
                        else:
                            if (feature[18]<=0.0):
                                bin_num[21] = 102
                            else:
                                bin_num[21] = 103
                else:
                    if (feature[21]<=0.0):
                        if (feature[2]<=3.0):
                            if (feature[18]<=0.0):
                                bin_num[21] = 104
                            else:
                                bin_num[21] = 105
                        else:
                            if (feature[24]<=0.0):
                                bin_num[21] = 106
                            else:
                                bin_num[21] = 107
                    else:
                        if (feature[34]<=0.0):
                            if (feature[9]<=0.0):
                                bin_num[21] = 108
                            else:
                                bin_num[21] = 109
                        else:
                            if (feature[28]<=0.0):
                                bin_num[21] = 110
                            else:
                                bin_num[21] = 111
            else:
                if (feature[18]<=0.0):
                    if (feature[28]<=0.0):
                        if (feature[1]<=2.0):
                            if (feature[19]<=0.0):
                                bin_num[21] = 112
                            else:
                                bin_num[21] = 113
                        else:
                            if (feature[17]<=0.0):
                                bin_num[21] = 114
                            else:
                                bin_num[21] = 115
                    else:
                        if (feature[25]<=0.0):
                            if (feature[34]<=0.0):
                                bin_num[21] = 116
                            else:
                                bin_num[21] = 117
                        else:
                            if (feature[1]<=2.0):
                                bin_num[21] = 118
                            else:
                                bin_num[21] = 119
                else:
                    if (feature[19]<=0.0):
                        if (feature[24]<=0.0):
                            if (feature[4]<=2646.0):
                                bin_num[21] = 120
                            else:
                                bin_num[21] = 121
                        else:
                            if (feature[21]<=0.0):
                                bin_num[21] = 122
                            else:
                                bin_num[21] = 123
                    else:
                        if (feature[35]<=0.0):
                            if (feature[11]<=0.0):
                                bin_num[21] = 124
                            else:
                                bin_num[21] = 125
                        else:
                            if (feature[3]<=2.0):
                                bin_num[21] = 126
                            else:
                                bin_num[21] = 127
    # Tree 22
    if (feature[17]<=0.0):
        if (feature[2]<=3.0):
            if (feature[26]<=0.0):
                if (feature[34]<=0.0):
                    if (feature[7]<=7.0):
                        if (feature[36]<=0.0):
                            if (feature[0]<=0.0):
                                bin_num[22] = 0
                            else:
                                bin_num[22] = 1
                        else:
                            if (feature[10]<=1.0):
                                bin_num[22] = 2
                            else:
                                bin_num[22] = 3
                    else:
                        if (feature[4]<=2642.0):
                            if (feature[1]<=2.0):
                                bin_num[22] = 4
                            else:
                                bin_num[22] = 5
                        else:
                            if (feature[18]<=0.0):
                                bin_num[22] = 6
                            else:
                                bin_num[22] = 7
                else:
                    if (feature[1]<=2.0):
                        if (feature[21]<=0.0):
                            if (feature[4]<=2642.0):
                                bin_num[22] = 8
                            else:
                                bin_num[22] = 9
                        else:
                            if (feature[18]<=0.0):
                                bin_num[22] = 10
                            else:
                                bin_num[22] = 11
                    else:
                        if (feature[20]<=0.0):
                            if (feature[27]<=0.0):
                                bin_num[22] = 12
                            else:
                                bin_num[22] = 13
                        else:
                            if (feature[21]<=0.0):
                                bin_num[22] = 14
                            else:
                                bin_num[22] = 15
            else:
                if (feature[28]<=0.0):
                    if (feature[19]<=0.0):
                        if (feature[24]<=0.0):
                            if (feature[18]<=0.0):
                                bin_num[22] = 16
                            else:
                                bin_num[22] = 17
                        else:
                            if (feature[21]<=0.0):
                                bin_num[22] = 18
                            else:
                                bin_num[22] = 19
                    else:
                        if (feature[22]<=0.0):
                            if (feature[13]<=0.0):
                                bin_num[22] = 20
                            else:
                                bin_num[22] = 21
                        else:
                            if (feature[21]<=0.0):
                                bin_num[22] = 22
                            else:
                                bin_num[22] = 23
                else:
                    if (feature[21]<=0.0):
                        if (feature[1]<=2.0):
                            if (feature[33]<=0.0):
                                bin_num[22] = 24
                            else:
                                bin_num[22] = 25
                        else:
                            if (feature[25]<=0.0):
                                bin_num[22] = 26
                            else:
                                bin_num[22] = 27
                    else:
                        if (feature[34]<=0.0):
                            if (feature[22]<=0.0):
                                bin_num[22] = 28
                            else:
                                bin_num[22] = 29
                        else:
                            if (feature[36]<=0.0):
                                bin_num[22] = 30
                            else:
                                bin_num[22] = 31
        else:
            if (feature[4]<=2642.0):
                if (feature[13]<=0.0):
                    if (feature[37]<=0.0):
                        if (feature[23]<=0.0):
                            if (feature[18]<=0.0):
                                bin_num[22] = 32
                            else:
                                bin_num[22] = 33
                        else:
                            if (feature[25]<=0.0):
                                bin_num[22] = 34
                            else:
                                bin_num[22] = 35
                    else:
                        if (feature[34]<=0.0):
                            if (feature[33]<=0.0):
                                bin_num[22] = 36
                            else:
                                bin_num[22] = 37
                        else:
                            if (feature[28]<=0.0):
                                bin_num[22] = 38
                            else:
                                bin_num[22] = 39
                else:
                    if (feature[29]<=0.0):
                        if (feature[27]<=0.0):
                            if (feature[26]<=0.0):
                                bin_num[22] = 40
                            else:
                                bin_num[22] = 41
                        else:
                            if (feature[28]<=0.0):
                                bin_num[22] = 42
                            else:
                                bin_num[22] = 43
                    else:
                        if (feature[18]<=0.0):
                            if (feature[23]<=0.0):
                                bin_num[22] = 44
                            else:
                                bin_num[22] = 45
                        else:
                            if (feature[11]<=0.0):
                                bin_num[22] = 46
                            else:
                                bin_num[22] = 47
            else:
                if (feature[20]<=0.0):
                    if (feature[5]<=16.0):
                        if (feature[6]<=2.0):
                            if (feature[36]<=0.0):
                                bin_num[22] = 48
                            else:
                                bin_num[22] = 49
                        else:
                            if (feature[12]<=2.0):
                                bin_num[22] = 50
                            else:
                                bin_num[22] = 51
                    else:
                        if (feature[3]<=2.0):
                            if (feature[29]<=0.0):
                                bin_num[22] = 52
                            else:
                                bin_num[22] = 53
                        else:
                            if (feature[8]<=35.0):
                                bin_num[22] = 54
                            else:
                                bin_num[22] = 55
                else:
                    if (feature[29]<=0.0):
                        if (feature[27]<=0.0):
                            if (feature[18]<=0.0):
                                bin_num[22] = 56
                            else:
                                bin_num[22] = 57
                        else:
                            if (feature[21]<=0.0):
                                bin_num[22] = 58
                            else:
                                bin_num[22] = 59
                    else:
                        if (feature[10]<=1.0):
                            if (feature[1]<=2.0):
                                bin_num[22] = 60
                            else:
                                bin_num[22] = 61
                        else:
                            if (feature[5]<=16.0):
                                bin_num[22] = 62
                            else:
                                bin_num[22] = 63
    else:
        if (feature[11]<=0.0):
            if (feature[35]<=0.0):
                if (feature[4]<=2642.0):
                    if (feature[34]<=0.0):
                        if (feature[1]<=2.0):
                            if (feature[20]<=0.0):
                                bin_num[22] = 64
                            else:
                                bin_num[22] = 65
                        else:
                            if (feature[2]<=3.0):
                                bin_num[22] = 66
                            else:
                                bin_num[22] = 67
                    else:
                        if (feature[26]<=0.0):
                            if (feature[10]<=1.0):
                                bin_num[22] = 68
                            else:
                                bin_num[22] = 69
                        else:
                            if (feature[25]<=0.0):
                                bin_num[22] = 70
                            else:
                                bin_num[22] = 71
                else:
                    if (feature[7]<=7.0):
                        if (feature[2]<=3.0):
                            if (feature[26]<=0.0):
                                bin_num[22] = 72
                            else:
                                bin_num[22] = 73
                        else:
                            if (feature[18]<=0.0):
                                bin_num[22] = 74
                            else:
                                bin_num[22] = 75
                    else:
                        if (feature[12]<=2.0):
                            if (feature[2]<=3.0):
                                bin_num[22] = 76
                            else:
                                bin_num[22] = 77
                        else:
                            if (feature[3]<=2.0):
                                bin_num[22] = 78
                            else:
                                bin_num[22] = 79
            else:
                if (feature[28]<=0.0):
                    if (feature[3]<=2.0):
                        if (feature[27]<=0.0):
                            if (feature[8]<=35.0):
                                bin_num[22] = 80
                            else:
                                bin_num[22] = 81
                        else:
                            if (feature[23]<=0.0):
                                bin_num[22] = 82
                            else:
                                bin_num[22] = 83
                    else:
                        if (feature[10]<=1.0):
                            if (feature[8]<=35.0):
                                bin_num[22] = 84
                            else:
                                bin_num[22] = 85
                        else:
                            if (feature[8]<=35.0):
                                bin_num[22] = 86
                            else:
                                bin_num[22] = 87
                else:
                    if (feature[18]<=0.0):
                        if (feature[6]<=2.0):
                            if (feature[37]<=0.0):
                                bin_num[22] = 88
                            else:
                                bin_num[22] = 89
                        else:
                            if (feature[29]<=0.0):
                                bin_num[22] = 90
                            else:
                                bin_num[22] = 91
                    else:
                        if (feature[21]<=0.0):
                            if (feature[26]<=0.0):
                                bin_num[22] = 92
                            else:
                                bin_num[22] = 93
                        else:
                            if (feature[34]<=0.0):
                                bin_num[22] = 94
                            else:
                                bin_num[22] = 95
        else:
            if (feature[34]<=0.0):
                if (feature[5]<=16.0):
                    if (feature[10]<=1.0):
                        if (feature[18]<=0.0):
                            if (feature[16]<=0.0):
                                bin_num[22] = 96
                            else:
                                bin_num[22] = 97
                        else:
                            if (feature[23]<=0.0):
                                bin_num[22] = 98
                            else:
                                bin_num[22] = 99
                    else:
                        if (feature[23]<=0.0):
                            if (feature[27]<=0.0):
                                bin_num[22] = 100
                            else:
                                bin_num[22] = 101
                        else:
                            if (feature[29]<=0.0):
                                bin_num[22] = 102
                            else:
                                bin_num[22] = 103
                else:
                    if (feature[27]<=0.0):
                        if (feature[7]<=7.0):
                            if (feature[29]<=0.0):
                                bin_num[22] = 104
                            else:
                                bin_num[22] = 105
                        else:
                            if (feature[26]<=0.0):
                                bin_num[22] = 106
                            else:
                                bin_num[22] = 107
                    else:
                        if (feature[18]<=0.0):
                            if (feature[0]<=0.0):
                                bin_num[22] = 108
                            else:
                                bin_num[22] = 109
                        else:
                            if (feature[21]<=0.0):
                                bin_num[22] = 110
                            else:
                                bin_num[22] = 111
            else:
                if (feature[25]<=0.0):
                    if (feature[9]<=0.0):
                        if (feature[21]<=0.0):
                            if (feature[23]<=0.0):
                                bin_num[22] = 112
                            else:
                                bin_num[22] = 113
                        else:
                            if (feature[29]<=0.0):
                                bin_num[22] = 114
                            else:
                                bin_num[22] = 115
                    else:
                        if (feature[32]<=0.0):
                            if (feature[7]<=7.0):
                                bin_num[22] = 116
                            else:
                                bin_num[22] = 117
                        else:
                            if (feature[16]<=0.0):
                                bin_num[22] = 118
                            else:
                                bin_num[22] = 119
                else:
                    if (feature[8]<=35.0):
                        if (feature[12]<=2.0):
                            if (feature[21]<=0.0):
                                bin_num[22] = 120
                            else:
                                bin_num[22] = 121
                        else:
                            if (feature[33]<=0.0):
                                bin_num[22] = 122
                            else:
                                bin_num[22] = 123
                    else:
                        if (feature[2]<=3.0):
                            if (feature[22]<=0.0):
                                bin_num[22] = 124
                            else:
                                bin_num[22] = 125
                        else:
                            if (feature[5]<=16.0):
                                bin_num[22] = 126
                            else:
                                bin_num[22] = 127
    # Tree 23
    if (feature[13]<=0.0):
        if (feature[5]<=15.0):
            if (feature[7]<=7.0):
                if (feature[6]<=2.0):
                    if (feature[27]<=0.0):
                        if (feature[29]<=0.0):
                            if (feature[18]<=0.0):
                                bin_num[23] = 0
                            else:
                                bin_num[23] = 1
                        else:
                            if (feature[8]<=35.0):
                                bin_num[23] = 2
                            else:
                                bin_num[23] = 3
                    else:
                        if (feature[22]<=0.0):
                            if (feature[34]<=0.0):
                                bin_num[23] = 4
                            else:
                                bin_num[23] = 5
                        else:
                            if (feature[28]<=0.0):
                                bin_num[23] = 6
                            else:
                                bin_num[23] = 7
                else:
                    if (feature[0]<=0.0):
                        if (feature[10]<=1.0):
                            if (feature[28]<=0.0):
                                bin_num[23] = 8
                            else:
                                bin_num[23] = 9
                        else:
                            if (feature[8]<=35.0):
                                bin_num[23] = 10
                            else:
                                bin_num[23] = 11
                    else:
                        if (feature[18]<=0.0):
                            if (feature[25]<=0.0):
                                bin_num[23] = 12
                            else:
                                bin_num[23] = 13
                        else:
                            if (feature[22]<=0.0):
                                bin_num[23] = 14
                            else:
                                bin_num[23] = 15
            else:
                if (feature[22]<=0.0):
                    if (feature[27]<=0.0):
                        if (feature[34]<=0.0):
                            if (feature[4]<=2692.0):
                                bin_num[23] = 16
                            else:
                                bin_num[23] = 17
                        else:
                            if (feature[21]<=0.0):
                                bin_num[23] = 18
                            else:
                                bin_num[23] = 19
                    else:
                        if (feature[0]<=0.0):
                            if (feature[20]<=0.0):
                                bin_num[23] = 20
                            else:
                                bin_num[23] = 21
                        else:
                            if (feature[37]<=0.0):
                                bin_num[23] = 22
                            else:
                                bin_num[23] = 23
                else:
                    if (feature[28]<=0.0):
                        if (feature[26]<=0.0):
                            if (feature[1]<=3.0):
                                bin_num[23] = 24
                            else:
                                bin_num[23] = 25
                        else:
                            if (feature[19]<=0.0):
                                bin_num[23] = 26
                            else:
                                bin_num[23] = 27
                    else:
                        if (feature[4]<=2692.0):
                            if (feature[1]<=3.0):
                                bin_num[23] = 28
                            else:
                                bin_num[23] = 29
                        else:
                            if (feature[29]<=0.0):
                                bin_num[23] = 30
                            else:
                                bin_num[23] = 31
        else:
            if (feature[8]<=35.0):
                if (feature[23]<=0.0):
                    if (feature[12]<=2.0):
                        if (feature[29]<=0.0):
                            if (feature[34]<=0.0):
                                bin_num[23] = 32
                            else:
                                bin_num[23] = 33
                        else:
                            if (feature[18]<=0.0):
                                bin_num[23] = 34
                            else:
                                bin_num[23] = 35
                    else:
                        if (feature[17]<=0.0):
                            if (feature[29]<=0.0):
                                bin_num[23] = 36
                            else:
                                bin_num[23] = 37
                        else:
                            if (feature[28]<=0.0):
                                bin_num[23] = 38
                            else:
                                bin_num[23] = 39
                else:
                    if (feature[17]<=0.0):
                        if (feature[18]<=0.0):
                            if (feature[22]<=0.0):
                                bin_num[23] = 40
                            else:
                                bin_num[23] = 41
                        else:
                            if (feature[6]<=2.0):
                                bin_num[23] = 42
                            else:
                                bin_num[23] = 43
                    else:
                        if (feature[26]<=0.0):
                            if (feature[29]<=0.0):
                                bin_num[23] = 44
                            else:
                                bin_num[23] = 45
                        else:
                            if (feature[35]<=0.0):
                                bin_num[23] = 46
                            else:
                                bin_num[23] = 47
            else:
                if (feature[23]<=0.0):
                    if (feature[34]<=0.0):
                        if (feature[21]<=0.0):
                            if (feature[29]<=0.0):
                                bin_num[23] = 48
                            else:
                                bin_num[23] = 49
                        else:
                            if (feature[28]<=0.0):
                                bin_num[23] = 50
                            else:
                                bin_num[23] = 51
                    else:
                        if (feature[26]<=0.0):
                            if (feature[10]<=1.0):
                                bin_num[23] = 52
                            else:
                                bin_num[23] = 53
                        else:
                            if (feature[6]<=2.0):
                                bin_num[23] = 54
                            else:
                                bin_num[23] = 55
                else:
                    if (feature[6]<=2.0):
                        if (feature[17]<=0.0):
                            if (feature[29]<=0.0):
                                bin_num[23] = 56
                            else:
                                bin_num[23] = 57
                        else:
                            if (feature[35]<=0.0):
                                bin_num[23] = 58
                            else:
                                bin_num[23] = 59
                    else:
                        if (feature[7]<=7.0):
                            if (feature[10]<=1.0):
                                bin_num[23] = 60
                            else:
                                bin_num[23] = 61
                        else:
                            if (feature[17]<=0.0):
                                bin_num[23] = 62
                            else:
                                bin_num[23] = 63
    else:
        if (feature[1]<=3.0):
            if (feature[35]<=0.0):
                if (feature[18]<=0.0):
                    if (feature[19]<=0.0):
                        if (feature[28]<=0.0):
                            if (feature[24]<=0.0):
                                bin_num[23] = 64
                            else:
                                bin_num[23] = 65
                        else:
                            if (feature[26]<=0.0):
                                bin_num[23] = 66
                            else:
                                bin_num[23] = 67
                    else:
                        if (feature[12]<=2.0):
                            if (feature[2]<=3.0):
                                bin_num[23] = 68
                            else:
                                bin_num[23] = 69
                        else:
                            if (feature[4]<=2692.0):
                                bin_num[23] = 70
                            else:
                                bin_num[23] = 71
                else:
                    if (feature[24]<=0.0):
                        if (feature[19]<=0.0):
                            if (feature[33]<=0.0):
                                bin_num[23] = 72
                            else:
                                bin_num[23] = 73
                        else:
                            if (feature[3]<=2.0):
                                bin_num[23] = 74
                            else:
                                bin_num[23] = 75
                    else:
                        if (feature[3]<=2.0):
                            if (feature[2]<=3.0):
                                bin_num[23] = 76
                            else:
                                bin_num[23] = 77
                        else:
                            if (feature[22]<=0.0):
                                bin_num[23] = 78
                            else:
                                bin_num[23] = 79
            else:
                if (feature[33]<=0.0):
                    if (feature[37]<=0.0):
                        if (feature[7]<=7.0):
                            if (feature[12]<=2.0):
                                bin_num[23] = 80
                            else:
                                bin_num[23] = 81
                        else:
                            if (feature[11]<=0.0):
                                bin_num[23] = 82
                            else:
                                bin_num[23] = 83
                    else:
                        if (feature[29]<=0.0):
                            if (feature[26]<=0.0):
                                bin_num[23] = 84
                            else:
                                bin_num[23] = 85
                        else:
                            if (feature[22]<=0.0):
                                bin_num[23] = 86
                            else:
                                bin_num[23] = 87
                else:
                    if (feature[23]<=0.0):
                        if (feature[21]<=0.0):
                            if (feature[26]<=0.0):
                                bin_num[23] = 88
                            else:
                                bin_num[23] = 89
                        else:
                            if (feature[29]<=0.0):
                                bin_num[23] = 90
                            else:
                                bin_num[23] = 91
                    else:
                        if (feature[26]<=0.0):
                            if (feature[18]<=0.0):
                                bin_num[23] = 92
                            else:
                                bin_num[23] = 93
                        else:
                            if (feature[12]<=2.0):
                                bin_num[23] = 94
                            else:
                                bin_num[23] = 95
        else:
            if (feature[20]<=0.0):
                if (feature[29]<=0.0):
                    if (feature[8]<=35.0):
                        if (feature[5]<=15.0):
                            if (feature[10]<=1.0):
                                bin_num[23] = 96
                            else:
                                bin_num[23] = 97
                        else:
                            if (feature[26]<=0.0):
                                bin_num[23] = 98
                            else:
                                bin_num[23] = 99
                    else:
                        if (feature[4]<=2692.0):
                            if (feature[38]<=0.0):
                                bin_num[23] = 100
                            else:
                                bin_num[23] = 101
                        else:
                            if (feature[7]<=7.0):
                                bin_num[23] = 102
                            else:
                                bin_num[23] = 103
                else:
                    if (feature[0]<=0.0):
                        if (feature[23]<=0.0):
                            if (feature[19]<=0.0):
                                bin_num[23] = 104
                            else:
                                bin_num[23] = 105
                        else:
                            if (feature[18]<=0.0):
                                bin_num[23] = 106
                            else:
                                bin_num[23] = 107
                    else:
                        if (feature[2]<=3.0):
                            if (feature[37]<=0.0):
                                bin_num[23] = 108
                            else:
                                bin_num[23] = 109
                        else:
                            if (feature[24]<=0.0):
                                bin_num[23] = 110
                            else:
                                bin_num[23] = 111
            else:
                if (feature[4]<=2692.0):
                    if (feature[12]<=2.0):
                        if (feature[3]<=2.0):
                            if (feature[10]<=1.0):
                                bin_num[23] = 112
                            else:
                                bin_num[23] = 113
                        else:
                            if (feature[21]<=0.0):
                                bin_num[23] = 114
                            else:
                                bin_num[23] = 115
                    else:
                        if (feature[37]<=0.0):
                            if (feature[27]<=0.0):
                                bin_num[23] = 116
                            else:
                                bin_num[23] = 117
                        else:
                            if (feature[0]<=0.0):
                                bin_num[23] = 118
                            else:
                                bin_num[23] = 119
                else:
                    if (feature[5]<=15.0):
                        if (feature[23]<=0.0):
                            if (feature[26]<=0.0):
                                bin_num[23] = 120
                            else:
                                bin_num[23] = 121
                        else:
                            if (feature[12]<=2.0):
                                bin_num[23] = 122
                            else:
                                bin_num[23] = 123
                    else:
                        if (feature[8]<=35.0):
                            if (feature[18]<=0.0):
                                bin_num[23] = 124
                            else:
                                bin_num[23] = 125
                        else:
                            if (feature[26]<=0.0):
                                bin_num[23] = 126
                            else:
                                bin_num[23] = 127
    # Tree 24
    if (feature[17]<=0.0):
        if (feature[2]<=3.0):
            if (feature[7]<=7.0):
                if (feature[13]<=0.0):
                    if (feature[29]<=0.0):
                        if (feature[5]<=15.0):
                            if (feature[25]<=0.0):
                                bin_num[24] = 0
                            else:
                                bin_num[24] = 1
                        else:
                            if (feature[8]<=34.0):
                                bin_num[24] = 2
                            else:
                                bin_num[24] = 3
                    else:
                        if (feature[38]<=0.0):
                            if (feature[23]<=0.0):
                                bin_num[24] = 4
                            else:
                                bin_num[24] = 5
                        else:
                            if (feature[4]<=2645.0):
                                bin_num[24] = 6
                            else:
                                bin_num[24] = 7
                else:
                    if (feature[0]<=0.0):
                        if (feature[4]<=2645.0):
                            if (feature[38]<=0.0):
                                bin_num[24] = 8
                            else:
                                bin_num[24] = 9
                        else:
                            if (feature[29]<=0.0):
                                bin_num[24] = 10
                            else:
                                bin_num[24] = 11
                    else:
                        if (feature[10]<=1.0):
                            if (feature[6]<=2.0):
                                bin_num[24] = 12
                            else:
                                bin_num[24] = 13
                        else:
                            if (feature[38]<=0.0):
                                bin_num[24] = 14
                            else:
                                bin_num[24] = 15
            else:
                if (feature[4]<=2645.0):
                    if (feature[1]<=2.0):
                        if (feature[3]<=2.0):
                            if (feature[5]<=15.0):
                                bin_num[24] = 16
                            else:
                                bin_num[24] = 17
                        else:
                            if (feature[23]<=0.0):
                                bin_num[24] = 18
                            else:
                                bin_num[24] = 19
                    else:
                        if (feature[12]<=2.0):
                            if (feature[20]<=0.0):
                                bin_num[24] = 20
                            else:
                                bin_num[24] = 21
                        else:
                            if (feature[3]<=2.0):
                                bin_num[24] = 22
                            else:
                                bin_num[24] = 23
                else:
                    if (feature[26]<=0.0):
                        if (feature[20]<=0.0):
                            if (feature[10]<=1.0):
                                bin_num[24] = 24
                            else:
                                bin_num[24] = 25
                        else:
                            if (feature[34]<=0.0):
                                bin_num[24] = 26
                            else:
                                bin_num[24] = 27
                    else:
                        if (feature[13]<=0.0):
                            if (feature[22]<=0.0):
                                bin_num[24] = 28
                            else:
                                bin_num[24] = 29
                        else:
                            if (feature[10]<=1.0):
                                bin_num[24] = 30
                            else:
                                bin_num[24] = 31
        else:
            if (feature[4]<=2645.0):
                if (feature[13]<=0.0):
                    if (feature[37]<=0.0):
                        if (feature[24]<=0.0):
                            if (feature[18]<=0.0):
                                bin_num[24] = 32
                            else:
                                bin_num[24] = 33
                        else:
                            if (feature[34]<=0.0):
                                bin_num[24] = 34
                            else:
                                bin_num[24] = 35
                    else:
                        if (feature[26]<=0.0):
                            if (feature[7]<=7.0):
                                bin_num[24] = 36
                            else:
                                bin_num[24] = 37
                        else:
                            if (feature[22]<=0.0):
                                bin_num[24] = 38
                            else:
                                bin_num[24] = 39
                else:
                    if (feature[29]<=0.0):
                        if (feature[22]<=0.0):
                            if (feature[27]<=0.0):
                                bin_num[24] = 40
                            else:
                                bin_num[24] = 41
                        else:
                            if (feature[21]<=0.0):
                                bin_num[24] = 42
                            else:
                                bin_num[24] = 43
                    else:
                        if (feature[18]<=0.0):
                            if (feature[23]<=0.0):
                                bin_num[24] = 44
                            else:
                                bin_num[24] = 45
                        else:
                            if (feature[11]<=0.0):
                                bin_num[24] = 46
                            else:
                                bin_num[24] = 47
            else:
                if (feature[5]<=15.0):
                    if (feature[10]<=1.0):
                        if (feature[36]<=0.0):
                            if (feature[23]<=0.0):
                                bin_num[24] = 48
                            else:
                                bin_num[24] = 49
                        else:
                            if (feature[20]<=0.0):
                                bin_num[24] = 50
                            else:
                                bin_num[24] = 51
                    else:
                        if (feature[8]<=34.0):
                            if (feature[12]<=2.0):
                                bin_num[24] = 52
                            else:
                                bin_num[24] = 53
                        else:
                            if (feature[37]<=0.0):
                                bin_num[24] = 54
                            else:
                                bin_num[24] = 55
                else:
                    if (feature[7]<=7.0):
                        if (feature[29]<=0.0):
                            if (feature[22]<=0.0):
                                bin_num[24] = 56
                            else:
                                bin_num[24] = 57
                        else:
                            if (feature[20]<=0.0):
                                bin_num[24] = 58
                            else:
                                bin_num[24] = 59
                    else:
                        if (feature[18]<=0.0):
                            if (feature[35]<=0.0):
                                bin_num[24] = 60
                            else:
                                bin_num[24] = 61
                        else:
                            if (feature[24]<=0.0):
                                bin_num[24] = 62
                            else:
                                bin_num[24] = 63
    else:
        if (feature[11]<=0.0):
            if (feature[10]<=1.0):
                if (feature[8]<=34.0):
                    if (feature[34]<=0.0):
                        if (feature[7]<=7.0):
                            if (feature[35]<=0.0):
                                bin_num[24] = 64
                            else:
                                bin_num[24] = 65
                        else:
                            if (feature[27]<=0.0):
                                bin_num[24] = 66
                            else:
                                bin_num[24] = 67
                    else:
                        if (feature[26]<=0.0):
                            if (feature[13]<=0.0):
                                bin_num[24] = 68
                            else:
                                bin_num[24] = 69
                        else:
                            if (feature[21]<=0.0):
                                bin_num[24] = 70
                            else:
                                bin_num[24] = 71
                else:
                    if (feature[18]<=0.0):
                        if (feature[37]<=0.0):
                            if (feature[22]<=0.0):
                                bin_num[24] = 72
                            else:
                                bin_num[24] = 73
                        else:
                            if (feature[26]<=0.0):
                                bin_num[24] = 74
                            else:
                                bin_num[24] = 75
                    else:
                        if (feature[19]<=0.0):
                            if (feature[24]<=0.0):
                                bin_num[24] = 76
                            else:
                                bin_num[24] = 77
                        else:
                            if (feature[3]<=2.0):
                                bin_num[24] = 78
                            else:
                                bin_num[24] = 79
            else:
                if (feature[28]<=0.0):
                    if (feature[27]<=0.0):
                        if (feature[8]<=34.0):
                            if (feature[5]<=15.0):
                                bin_num[24] = 80
                            else:
                                bin_num[24] = 81
                        else:
                            if (feature[22]<=0.0):
                                bin_num[24] = 82
                            else:
                                bin_num[24] = 83
                    else:
                        if (feature[3]<=2.0):
                            if (feature[5]<=15.0):
                                bin_num[24] = 84
                            else:
                                bin_num[24] = 85
                        else:
                            if (feature[0]<=0.0):
                                bin_num[24] = 86
                            else:
                                bin_num[24] = 87
                else:
                    if (feature[21]<=0.0):
                        if (feature[2]<=3.0):
                            if (feature[26]<=0.0):
                                bin_num[24] = 88
                            else:
                                bin_num[24] = 89
                        else:
                            if (feature[20]<=0.0):
                                bin_num[24] = 90
                            else:
                                bin_num[24] = 91
                    else:
                        if (feature[0]<=0.0):
                            if (feature[7]<=7.0):
                                bin_num[24] = 92
                            else:
                                bin_num[24] = 93
                        else:
                            if (feature[25]<=0.0):
                                bin_num[24] = 94
                            else:
                                bin_num[24] = 95
        else:
            if (feature[34]<=0.0):
                if (feature[5]<=15.0):
                    if (feature[29]<=0.0):
                        if (feature[26]<=0.0):
                            if (feature[27]<=0.0):
                                bin_num[24] = 96
                            else:
                                bin_num[24] = 97
                        else:
                            if (feature[21]<=0.0):
                                bin_num[24] = 98
                            else:
                                bin_num[24] = 99
                    else:
                        if (feature[21]<=0.0):
                            if (feature[6]<=2.0):
                                bin_num[24] = 100
                            else:
                                bin_num[24] = 101
                        else:
                            if (feature[8]<=34.0):
                                bin_num[24] = 102
                            else:
                                bin_num[24] = 103
                else:
                    if (feature[27]<=0.0):
                        if (feature[0]<=0.0):
                            if (feature[12]<=2.0):
                                bin_num[24] = 104
                            else:
                                bin_num[24] = 105
                        else:
                            if (feature[33]<=0.0):
                                bin_num[24] = 106
                            else:
                                bin_num[24] = 107
                    else:
                        if (feature[18]<=0.0):
                            if (feature[0]<=0.0):
                                bin_num[24] = 108
                            else:
                                bin_num[24] = 109
                        else:
                            if (feature[21]<=0.0):
                                bin_num[24] = 110
                            else:
                                bin_num[24] = 111
            else:
                if (feature[25]<=0.0):
                    if (feature[9]<=0.0):
                        if (feature[24]<=0.0):
                            if (feature[21]<=0.0):
                                bin_num[24] = 112
                            else:
                                bin_num[24] = 113
                        else:
                            if (feature[22]<=0.0):
                                bin_num[24] = 114
                            else:
                                bin_num[24] = 115
                    else:
                        if (feature[32]<=0.0):
                            if (feature[15]<=0.0):
                                bin_num[24] = 116
                            else:
                                bin_num[24] = 117
                        else:
                            if (feature[16]<=0.0):
                                bin_num[24] = 118
                            else:
                                bin_num[24] = 119
                else:
                    if (feature[5]<=15.0):
                        if (feature[31]<=0.0):
                            if (feature[15]<=0.0):
                                bin_num[24] = 120
                            else:
                                bin_num[24] = 121
                        else:
                            if (feature[32]<=0.0):
                                bin_num[24] = 122
                            else:
                                bin_num[24] = 123
                    else:
                        if (feature[23]<=0.0):
                            if (feature[6]<=2.0):
                                bin_num[24] = 124
                            else:
                                bin_num[24] = 125
                        else:
                            if (feature[15]<=0.0):
                                bin_num[24] = 126
                            else:
                                bin_num[24] = 127
    # Tree 25
    if (feature[20]<=0.0):
        if (feature[18]<=0.0):
            if (feature[19]<=0.0):
                if (feature[28]<=0.0):
                    if (feature[24]<=0.0):
                        if (feature[21]<=0.0):
                            if (feature[27]<=0.0):
                                bin_num[25] = 0
                            else:
                                bin_num[25] = 1
                        else:
                            if (feature[7]<=7.0):
                                bin_num[25] = 2
                            else:
                                bin_num[25] = 3
                    else:
                        if (feature[23]<=0.0):
                            if (feature[22]<=0.0):
                                bin_num[25] = 4
                            else:
                                bin_num[25] = 5
                        else:
                            if (feature[25]<=0.0):
                                bin_num[25] = 6
                            else:
                                bin_num[25] = 7
                else:
                    if (feature[35]<=0.0):
                        if (feature[21]<=0.0):
                            if (feature[26]<=0.0):
                                bin_num[25] = 8
                            else:
                                bin_num[25] = 9
                        else:
                            if (feature[34]<=0.0):
                                bin_num[25] = 10
                            else:
                                bin_num[25] = 11
                    else:
                        if (feature[34]<=0.0):
                            if (feature[33]<=0.0):
                                bin_num[25] = 12
                            else:
                                bin_num[25] = 13
                        else:
                            if (feature[22]<=0.0):
                                bin_num[25] = 14
                            else:
                                bin_num[25] = 15
            else:
                if (feature[26]<=0.0):
                    if (feature[22]<=0.0):
                        if (feature[23]<=0.0):
                            if (feature[27]<=0.0):
                                bin_num[25] = 16
                            else:
                                bin_num[25] = 17
                        else:
                            if (feature[27]<=0.0):
                                bin_num[25] = 18
                            else:
                                bin_num[25] = 19
                    else:
                        if (feature[23]<=0.0):
                            if (feature[8]<=35.0):
                                bin_num[25] = 20
                            else:
                                bin_num[25] = 21
                        else:
                            if (feature[10]<=1.0):
                                bin_num[25] = 22
                            else:
                                bin_num[25] = 23
                else:
                    if (feature[22]<=0.0):
                        if (feature[33]<=0.0):
                            if (feature[21]<=0.0):
                                bin_num[25] = 24
                            else:
                                bin_num[25] = 25
                        else:
                            if (feature[37]<=0.0):
                                bin_num[25] = 26
                            else:
                                bin_num[25] = 27
                    else:
                        if (feature[21]<=0.0):
                            if (feature[1]<=2.0):
                                bin_num[25] = 28
                            else:
                                bin_num[25] = 29
                        else:
                            if (feature[6]<=2.0):
                                bin_num[25] = 30
                            else:
                                bin_num[25] = 31
        else:
            if (feature[24]<=0.0):
                if (feature[19]<=0.0):
                    if (feature[33]<=0.0):
                        if (feature[26]<=0.0):
                            if (feature[29]<=0.0):
                                bin_num[25] = 32
                            else:
                                bin_num[25] = 33
                        else:
                            if (feature[21]<=0.0):
                                bin_num[25] = 34
                            else:
                                bin_num[25] = 35
                    else:
                        if (feature[1]<=2.0):
                            if (feature[17]<=0.0):
                                bin_num[25] = 36
                            else:
                                bin_num[25] = 37
                        else:
                            if (feature[10]<=1.0):
                                bin_num[25] = 38
                            else:
                                bin_num[25] = 39
                else:
                    if (feature[27]<=0.0):
                        if (feature[11]<=0.0):
                            if (feature[35]<=0.0):
                                bin_num[25] = 40
                            else:
                                bin_num[25] = 41
                        else:
                            if (feature[23]<=0.0):
                                bin_num[25] = 42
                            else:
                                bin_num[25] = 43
                    else:
                        if (feature[21]<=0.0):
                            if (feature[33]<=0.0):
                                bin_num[25] = 44
                            else:
                                bin_num[25] = 45
                        else:
                            if (feature[5]<=15.0):
                                bin_num[25] = 46
                            else:
                                bin_num[25] = 47
            else:
                if (feature[21]<=0.0):
                    if (feature[35]<=0.0):
                        if (feature[29]<=0.0):
                            if (feature[6]<=2.0):
                                bin_num[25] = 48
                            else:
                                bin_num[25] = 49
                        else:
                            if (feature[6]<=2.0):
                                bin_num[25] = 50
                            else:
                                bin_num[25] = 51
                    else:
                        if (feature[23]<=0.0):
                            if (feature[8]<=35.0):
                                bin_num[25] = 52
                            else:
                                bin_num[25] = 53
                        else:
                            if (feature[11]<=0.0):
                                bin_num[25] = 54
                            else:
                                bin_num[25] = 55
                else:
                    if (feature[22]<=0.0):
                        if (feature[33]<=0.0):
                            if (feature[34]<=0.0):
                                bin_num[25] = 56
                            else:
                                bin_num[25] = 57
                        else:
                            if (feature[1]<=2.0):
                                bin_num[25] = 58
                            else:
                                bin_num[25] = 59
                    else:
                        if (feature[34]<=0.0):
                            if (feature[8]<=35.0):
                                bin_num[25] = 60
                            else:
                                bin_num[25] = 61
                        else:
                            if (feature[29]<=0.0):
                                bin_num[25] = 62
                            else:
                                bin_num[25] = 63
    else:
        if (feature[29]<=0.0):
            if (feature[4]<=2700.0):
                if (feature[13]<=0.0):
                    if (feature[21]<=0.0):
                        if (feature[1]<=2.0):
                            if (feature[25]<=0.0):
                                bin_num[25] = 64
                            else:
                                bin_num[25] = 65
                        else:
                            if (feature[18]<=0.0):
                                bin_num[25] = 66
                            else:
                                bin_num[25] = 67
                    else:
                        if (feature[18]<=0.0):
                            if (feature[34]<=0.0):
                                bin_num[25] = 68
                            else:
                                bin_num[25] = 69
                        else:
                            if (feature[34]<=0.0):
                                bin_num[25] = 70
                            else:
                                bin_num[25] = 71
                else:
                    if (feature[37]<=0.0):
                        if (feature[35]<=0.0):
                            if (feature[21]<=0.0):
                                bin_num[25] = 72
                            else:
                                bin_num[25] = 73
                        else:
                            if (feature[7]<=7.0):
                                bin_num[25] = 74
                            else:
                                bin_num[25] = 75
                    else:
                        if (feature[23]<=0.0):
                            if (feature[0]<=0.0):
                                bin_num[25] = 76
                            else:
                                bin_num[25] = 77
                        else:
                            if (feature[21]<=0.0):
                                bin_num[25] = 78
                            else:
                                bin_num[25] = 79
            else:
                if (feature[10]<=1.0):
                    if (feature[18]<=0.0):
                        if (feature[25]<=0.0):
                            if (feature[23]<=0.0):
                                bin_num[25] = 80
                            else:
                                bin_num[25] = 81
                        else:
                            if (feature[27]<=0.0):
                                bin_num[25] = 82
                            else:
                                bin_num[25] = 83
                    else:
                        if (feature[19]<=0.0):
                            if (feature[24]<=0.0):
                                bin_num[25] = 84
                            else:
                                bin_num[25] = 85
                        else:
                            if (feature[5]<=15.0):
                                bin_num[25] = 86
                            else:
                                bin_num[25] = 87
                else:
                    if (feature[7]<=7.0):
                        if (feature[26]<=0.0):
                            if (feature[37]<=0.0):
                                bin_num[25] = 88
                            else:
                                bin_num[25] = 89
                        else:
                            if (feature[2]<=3.0):
                                bin_num[25] = 90
                            else:
                                bin_num[25] = 91
                    else:
                        if (feature[27]<=0.0):
                            if (feature[34]<=0.0):
                                bin_num[25] = 92
                            else:
                                bin_num[25] = 93
                        else:
                            if (feature[21]<=0.0):
                                bin_num[25] = 94
                            else:
                                bin_num[25] = 95
        else:
            if (feature[23]<=0.0):
                if (feature[34]<=0.0):
                    if (feature[2]<=3.0):
                        if (feature[28]<=0.0):
                            if (feature[0]<=0.0):
                                bin_num[25] = 96
                            else:
                                bin_num[25] = 97
                        else:
                            if (feature[18]<=0.0):
                                bin_num[25] = 98
                            else:
                                bin_num[25] = 99
                    else:
                        if (feature[4]<=2700.0):
                            if (feature[5]<=15.0):
                                bin_num[25] = 100
                            else:
                                bin_num[25] = 101
                        else:
                            if (feature[10]<=1.0):
                                bin_num[25] = 102
                            else:
                                bin_num[25] = 103
                else:
                    if (feature[21]<=0.0):
                        if (feature[1]<=2.0):
                            if (feature[18]<=0.0):
                                bin_num[25] = 104
                            else:
                                bin_num[25] = 105
                        else:
                            if (feature[4]<=2700.0):
                                bin_num[25] = 106
                            else:
                                bin_num[25] = 107
                    else:
                        if (feature[24]<=0.0):
                            if (feature[19]<=0.0):
                                bin_num[25] = 108
                            else:
                                bin_num[25] = 109
                        else:
                            if (feature[5]<=15.0):
                                bin_num[25] = 110
                            else:
                                bin_num[25] = 111
            else:
                if (feature[18]<=0.0):
                    if (feature[28]<=0.0):
                        if (feature[1]<=2.0):
                            if (feature[19]<=0.0):
                                bin_num[25] = 112
                            else:
                                bin_num[25] = 113
                        else:
                            if (feature[17]<=0.0):
                                bin_num[25] = 114
                            else:
                                bin_num[25] = 115
                    else:
                        if (feature[25]<=0.0):
                            if (feature[34]<=0.0):
                                bin_num[25] = 116
                            else:
                                bin_num[25] = 117
                        else:
                            if (feature[1]<=2.0):
                                bin_num[25] = 118
                            else:
                                bin_num[25] = 119
                else:
                    if (feature[19]<=0.0):
                        if (feature[24]<=0.0):
                            if (feature[11]<=0.0):
                                bin_num[25] = 120
                            else:
                                bin_num[25] = 121
                        else:
                            if (feature[21]<=0.0):
                                bin_num[25] = 122
                            else:
                                bin_num[25] = 123
                    else:
                        if (feature[2]<=3.0):
                            if (feature[10]<=1.0):
                                bin_num[25] = 124
                            else:
                                bin_num[25] = 125
                        else:
                            if (feature[36]<=0.0):
                                bin_num[25] = 126
                            else:
                                bin_num[25] = 127
    # Tree 26
    if (feature[6]<=3.0):
        if (feature[8]<=36.0):
            if (feature[36]<=0.0):
                if (feature[17]<=0.0):
                    if (feature[38]<=0.0):
                        if (feature[11]<=0.0):
                            if (feature[29]<=0.0):
                                bin_num[26] = 0
                            else:
                                bin_num[26] = 1
                        else:
                            if (feature[23]<=0.0):
                                bin_num[26] = 2
                            else:
                                bin_num[26] = 3
                    else:
                        if (feature[13]<=0.0):
                            if (feature[12]<=2.0):
                                bin_num[26] = 4
                            else:
                                bin_num[26] = 5
                        else:
                            if (feature[9]<=0.0):
                                bin_num[26] = 6
                            else:
                                bin_num[26] = 7
                else:
                    if (feature[5]<=16.0):
                        if (feature[4]<=2705.0):
                            if (feature[10]<=1.0):
                                bin_num[26] = 8
                            else:
                                bin_num[26] = 9
                        else:
                            if (feature[10]<=1.0):
                                bin_num[26] = 10
                            else:
                                bin_num[26] = 11
                    else:
                        if (feature[13]<=0.0):
                            if (feature[23]<=0.0):
                                bin_num[26] = 12
                            else:
                                bin_num[26] = 13
                        else:
                            if (feature[18]<=0.0):
                                bin_num[26] = 14
                            else:
                                bin_num[26] = 15
            else:
                if (feature[7]<=7.0):
                    if (feature[13]<=0.0):
                        if (feature[12]<=2.0):
                            if (feature[29]<=0.0):
                                bin_num[26] = 16
                            else:
                                bin_num[26] = 17
                        else:
                            if (feature[27]<=0.0):
                                bin_num[26] = 18
                            else:
                                bin_num[26] = 19
                    else:
                        if (feature[10]<=1.0):
                            if (feature[5]<=16.0):
                                bin_num[26] = 20
                            else:
                                bin_num[26] = 21
                        else:
                            if (feature[2]<=3.0):
                                bin_num[26] = 22
                            else:
                                bin_num[26] = 23
                else:
                    if (feature[13]<=0.0):
                        if (feature[22]<=0.0):
                            if (feature[34]<=0.0):
                                bin_num[26] = 24
                            else:
                                bin_num[26] = 25
                        else:
                            if (feature[29]<=0.0):
                                bin_num[26] = 26
                            else:
                                bin_num[26] = 27
                    else:
                        if (feature[18]<=0.0):
                            if (feature[25]<=0.0):
                                bin_num[26] = 28
                            else:
                                bin_num[26] = 29
                        else:
                            if (feature[24]<=0.0):
                                bin_num[26] = 30
                            else:
                                bin_num[26] = 31
        else:
            if (feature[5]<=16.0):
                if (feature[29]<=0.0):
                    if (feature[24]<=0.0):
                        if (feature[19]<=0.0):
                            if (feature[18]<=0.0):
                                bin_num[26] = 32
                            else:
                                bin_num[26] = 33
                        else:
                            if (feature[13]<=0.0):
                                bin_num[26] = 34
                            else:
                                bin_num[26] = 35
                    else:
                        if (feature[13]<=0.0):
                            if (feature[4]<=2705.0):
                                bin_num[26] = 36
                            else:
                                bin_num[26] = 37
                        else:
                            if (feature[18]<=0.0):
                                bin_num[26] = 38
                            else:
                                bin_num[26] = 39
                else:
                    if (feature[23]<=0.0):
                        if (feature[13]<=0.0):
                            if (feature[12]<=2.0):
                                bin_num[26] = 40
                            else:
                                bin_num[26] = 41
                        else:
                            if (feature[33]<=0.0):
                                bin_num[26] = 42
                            else:
                                bin_num[26] = 43
                    else:
                        if (feature[21]<=0.0):
                            if (feature[18]<=0.0):
                                bin_num[26] = 44
                            else:
                                bin_num[26] = 45
                        else:
                            if (feature[34]<=0.0):
                                bin_num[26] = 46
                            else:
                                bin_num[26] = 47
            else:
                if (feature[10]<=1.0):
                    if (feature[3]<=2.0):
                        if (feature[38]<=0.0):
                            if (feature[13]<=0.0):
                                bin_num[26] = 48
                            else:
                                bin_num[26] = 49
                        else:
                            if (feature[18]<=0.0):
                                bin_num[26] = 50
                            else:
                                bin_num[26] = 51
                    else:
                        if (feature[38]<=0.0):
                            if (feature[2]<=3.0):
                                bin_num[26] = 52
                            else:
                                bin_num[26] = 53
                        else:
                            if (feature[24]<=0.0):
                                bin_num[26] = 54
                            else:
                                bin_num[26] = 55
                else:
                    if (feature[9]<=0.0):
                        if (feature[36]<=0.0):
                            if (feature[17]<=0.0):
                                bin_num[26] = 56
                            else:
                                bin_num[26] = 57
                        else:
                            if (feature[4]<=2705.0):
                                bin_num[26] = 58
                            else:
                                bin_num[26] = 59
                    else:
                        if (feature[36]<=0.0):
                            if (feature[29]<=0.0):
                                bin_num[26] = 60
                            else:
                                bin_num[26] = 61
                        else:
                            if (feature[23]<=0.0):
                                bin_num[26] = 62
                            else:
                                bin_num[26] = 63
    else:
        if (feature[10]<=1.0):
            if (feature[5]<=16.0):
                if (feature[8]<=36.0):
                    if (feature[12]<=2.0):
                        if (feature[34]<=0.0):
                            if (feature[0]<=0.0):
                                bin_num[26] = 64
                            else:
                                bin_num[26] = 65
                        else:
                            if (feature[3]<=2.0):
                                bin_num[26] = 66
                            else:
                                bin_num[26] = 67
                    else:
                        if (feature[0]<=0.0):
                            if (feature[36]<=0.0):
                                bin_num[26] = 68
                            else:
                                bin_num[26] = 69
                        else:
                            if (feature[17]<=0.0):
                                bin_num[26] = 70
                            else:
                                bin_num[26] = 71
                else:
                    if (feature[9]<=0.0):
                        if (feature[12]<=2.0):
                            if (feature[17]<=0.0):
                                bin_num[26] = 72
                            else:
                                bin_num[26] = 73
                        else:
                            if (feature[4]<=2705.0):
                                bin_num[26] = 74
                            else:
                                bin_num[26] = 75
                    else:
                        if (feature[2]<=3.0):
                            if (feature[12]<=2.0):
                                bin_num[26] = 76
                            else:
                                bin_num[26] = 77
                        else:
                            if (feature[17]<=0.0):
                                bin_num[26] = 78
                            else:
                                bin_num[26] = 79
            else:
                if (feature[7]<=7.0):
                    if (feature[37]<=0.0):
                        if (feature[18]<=0.0):
                            if (feature[25]<=0.0):
                                bin_num[26] = 80
                            else:
                                bin_num[26] = 81
                        else:
                            if (feature[4]<=2705.0):
                                bin_num[26] = 82
                            else:
                                bin_num[26] = 83
                    else:
                        if (feature[21]<=0.0):
                            if (feature[8]<=36.0):
                                bin_num[26] = 84
                            else:
                                bin_num[26] = 85
                        else:
                            if (feature[22]<=0.0):
                                bin_num[26] = 86
                            else:
                                bin_num[26] = 87
                else:
                    if (feature[8]<=36.0):
                        if (feature[9]<=0.0):
                            if (feature[12]<=2.0):
                                bin_num[26] = 88
                            else:
                                bin_num[26] = 89
                        else:
                            if (feature[17]<=0.0):
                                bin_num[26] = 90
                            else:
                                bin_num[26] = 91
                    else:
                        if (feature[3]<=2.0):
                            if (feature[12]<=2.0):
                                bin_num[26] = 92
                            else:
                                bin_num[26] = 93
                        else:
                            if (feature[22]<=0.0):
                                bin_num[26] = 94
                            else:
                                bin_num[26] = 95
        else:
            if (feature[38]<=0.0):
                if (feature[36]<=0.0):
                    if (feature[8]<=36.0):
                        if (feature[5]<=16.0):
                            if (feature[9]<=0.0):
                                bin_num[26] = 96
                            else:
                                bin_num[26] = 97
                        else:
                            if (feature[0]<=0.0):
                                bin_num[26] = 98
                            else:
                                bin_num[26] = 99
                    else:
                        if (feature[5]<=16.0):
                            if (feature[7]<=7.0):
                                bin_num[26] = 100
                            else:
                                bin_num[26] = 101
                        else:
                            if (feature[7]<=7.0):
                                bin_num[26] = 102
                            else:
                                bin_num[26] = 103
                else:
                    if (feature[8]<=36.0):
                        if (feature[0]<=0.0):
                            if (feature[5]<=16.0):
                                bin_num[26] = 104
                            else:
                                bin_num[26] = 105
                        else:
                            if (feature[37]<=0.0):
                                bin_num[26] = 106
                            else:
                                bin_num[26] = 107
                    else:
                        if (feature[0]<=0.0):
                            if (feature[2]<=3.0):
                                bin_num[26] = 108
                            else:
                                bin_num[26] = 109
                        else:
                            if (feature[37]<=0.0):
                                bin_num[26] = 110
                            else:
                                bin_num[26] = 111
            else:
                if (feature[8]<=36.0):
                    if (feature[5]<=16.0):
                        if (feature[37]<=0.0):
                            if (feature[7]<=7.0):
                                bin_num[26] = 112
                            else:
                                bin_num[26] = 113
                        else:
                            if (feature[33]<=0.0):
                                bin_num[26] = 114
                            else:
                                bin_num[26] = 115
                    else:
                        if (feature[7]<=7.0):
                            if (feature[37]<=0.0):
                                bin_num[26] = 116
                            else:
                                bin_num[26] = 117
                        else:
                            if (feature[18]<=0.0):
                                bin_num[26] = 118
                            else:
                                bin_num[26] = 119
                else:
                    if (feature[5]<=16.0):
                        if (feature[37]<=0.0):
                            if (feature[23]<=0.0):
                                bin_num[26] = 120
                            else:
                                bin_num[26] = 121
                        else:
                            if (feature[21]<=0.0):
                                bin_num[26] = 122
                            else:
                                bin_num[26] = 123
                    else:
                        if (feature[37]<=0.0):
                            if (feature[20]<=0.0):
                                bin_num[26] = 124
                            else:
                                bin_num[26] = 125
                        else:
                            if (feature[22]<=0.0):
                                bin_num[26] = 126
                            else:
                                bin_num[26] = 127
    # Tree 27
    if (feature[20]<=0.0):
        if (feature[1]<=3.0):
            if (feature[22]<=0.0):
                if (feature[33]<=0.0):
                    if (feature[27]<=0.0):
                        if (feature[21]<=0.0):
                            if (feature[26]<=0.0):
                                bin_num[27] = 0
                            else:
                                bin_num[27] = 1
                        else:
                            if (feature[26]<=0.0):
                                bin_num[27] = 2
                            else:
                                bin_num[27] = 3
                    else:
                        if (feature[6]<=2.0):
                            if (feature[21]<=0.0):
                                bin_num[27] = 4
                            else:
                                bin_num[27] = 5
                        else:
                            if (feature[23]<=0.0):
                                bin_num[27] = 6
                            else:
                                bin_num[27] = 7
                else:
                    if (feature[25]<=0.0):
                        if (feature[29]<=0.0):
                            if (feature[21]<=0.0):
                                bin_num[27] = 8
                            else:
                                bin_num[27] = 9
                        else:
                            if (feature[21]<=0.0):
                                bin_num[27] = 10
                            else:
                                bin_num[27] = 11
                    else:
                        if (feature[21]<=0.0):
                            if (feature[26]<=0.0):
                                bin_num[27] = 12
                            else:
                                bin_num[27] = 13
                        else:
                            if (feature[19]<=0.0):
                                bin_num[27] = 14
                            else:
                                bin_num[27] = 15
            else:
                if (feature[29]<=0.0):
                    if (feature[37]<=0.0):
                        if (feature[26]<=0.0):
                            if (feature[27]<=0.0):
                                bin_num[27] = 16
                            else:
                                bin_num[27] = 17
                        else:
                            if (feature[21]<=0.0):
                                bin_num[27] = 18
                            else:
                                bin_num[27] = 19
                    else:
                        if (feature[34]<=0.0):
                            if (feature[23]<=0.0):
                                bin_num[27] = 20
                            else:
                                bin_num[27] = 21
                        else:
                            if (feature[21]<=0.0):
                                bin_num[27] = 22
                            else:
                                bin_num[27] = 23
                else:
                    if (feature[18]<=0.0):
                        if (feature[23]<=0.0):
                            if (feature[28]<=0.0):
                                bin_num[27] = 24
                            else:
                                bin_num[27] = 25
                        else:
                            if (feature[12]<=2.0):
                                bin_num[27] = 26
                            else:
                                bin_num[27] = 27
                    else:
                        if (feature[0]<=0.0):
                            if (feature[24]<=0.0):
                                bin_num[27] = 28
                            else:
                                bin_num[27] = 29
                        else:
                            if (feature[11]<=0.0):
                                bin_num[27] = 30
                            else:
                                bin_num[27] = 31
        else:
            if (feature[13]<=0.0):
                if (feature[34]<=0.0):
                    if (feature[5]<=15.0):
                        if (feature[8]<=34.0):
                            if (feature[4]<=2727.0):
                                bin_num[27] = 32
                            else:
                                bin_num[27] = 33
                        else:
                            if (feature[12]<=2.0):
                                bin_num[27] = 34
                            else:
                                bin_num[27] = 35
                    else:
                        if (feature[8]<=34.0):
                            if (feature[29]<=0.0):
                                bin_num[27] = 36
                            else:
                                bin_num[27] = 37
                        else:
                            if (feature[23]<=0.0):
                                bin_num[27] = 38
                            else:
                                bin_num[27] = 39
                else:
                    if (feature[22]<=0.0):
                        if (feature[29]<=0.0):
                            if (feature[21]<=0.0):
                                bin_num[27] = 40
                            else:
                                bin_num[27] = 41
                        else:
                            if (feature[21]<=0.0):
                                bin_num[27] = 42
                            else:
                                bin_num[27] = 43
                    else:
                        if (feature[37]<=0.0):
                            if (feature[4]<=2727.0):
                                bin_num[27] = 44
                            else:
                                bin_num[27] = 45
                        else:
                            if (feature[4]<=2727.0):
                                bin_num[27] = 46
                            else:
                                bin_num[27] = 47
            else:
                if (feature[29]<=0.0):
                    if (feature[22]<=0.0):
                        if (feature[26]<=0.0):
                            if (feature[27]<=0.0):
                                bin_num[27] = 48
                            else:
                                bin_num[27] = 49
                        else:
                            if (feature[33]<=0.0):
                                bin_num[27] = 50
                            else:
                                bin_num[27] = 51
                    else:
                        if (feature[18]<=0.0):
                            if (feature[26]<=0.0):
                                bin_num[27] = 52
                            else:
                                bin_num[27] = 53
                        else:
                            if (feature[21]<=0.0):
                                bin_num[27] = 54
                            else:
                                bin_num[27] = 55
                else:
                    if (feature[0]<=0.0):
                        if (feature[23]<=0.0):
                            if (feature[19]<=0.0):
                                bin_num[27] = 56
                            else:
                                bin_num[27] = 57
                        else:
                            if (feature[5]<=15.0):
                                bin_num[27] = 58
                            else:
                                bin_num[27] = 59
                    else:
                        if (feature[5]<=15.0):
                            if (feature[9]<=0.0):
                                bin_num[27] = 60
                            else:
                                bin_num[27] = 61
                        else:
                            if (feature[12]<=2.0):
                                bin_num[27] = 62
                            else:
                                bin_num[27] = 63
    else:
        if (feature[29]<=0.0):
            if (feature[4]<=2727.0):
                if (feature[13]<=0.0):
                    if (feature[21]<=0.0):
                        if (feature[7]<=7.0):
                            if (feature[25]<=0.0):
                                bin_num[27] = 64
                            else:
                                bin_num[27] = 65
                        else:
                            if (feature[23]<=0.0):
                                bin_num[27] = 66
                            else:
                                bin_num[27] = 67
                    else:
                        if (feature[18]<=0.0):
                            if (feature[34]<=0.0):
                                bin_num[27] = 68
                            else:
                                bin_num[27] = 69
                        else:
                            if (feature[34]<=0.0):
                                bin_num[27] = 70
                            else:
                                bin_num[27] = 71
                else:
                    if (feature[1]<=3.0):
                        if (feature[9]<=0.0):
                            if (feature[12]<=2.0):
                                bin_num[27] = 72
                            else:
                                bin_num[27] = 73
                        else:
                            if (feature[10]<=1.0):
                                bin_num[27] = 74
                            else:
                                bin_num[27] = 75
                    else:
                        if (feature[12]<=2.0):
                            if (feature[2]<=3.0):
                                bin_num[27] = 76
                            else:
                                bin_num[27] = 77
                        else:
                            if (feature[3]<=2.0):
                                bin_num[27] = 78
                            else:
                                bin_num[27] = 79
            else:
                if (feature[5]<=15.0):
                    if (feature[27]<=0.0):
                        if (feature[7]<=7.0):
                            if (feature[18]<=0.0):
                                bin_num[27] = 80
                            else:
                                bin_num[27] = 81
                        else:
                            if (feature[12]<=2.0):
                                bin_num[27] = 82
                            else:
                                bin_num[27] = 83
                    else:
                        if (feature[21]<=0.0):
                            if (feature[6]<=2.0):
                                bin_num[27] = 84
                            else:
                                bin_num[27] = 85
                        else:
                            if (feature[34]<=0.0):
                                bin_num[27] = 86
                            else:
                                bin_num[27] = 87
                else:
                    if (feature[8]<=34.0):
                        if (feature[27]<=0.0):
                            if (feature[10]<=1.0):
                                bin_num[27] = 88
                            else:
                                bin_num[27] = 89
                        else:
                            if (feature[21]<=0.0):
                                bin_num[27] = 90
                            else:
                                bin_num[27] = 91
                    else:
                        if (feature[26]<=0.0):
                            if (feature[34]<=0.0):
                                bin_num[27] = 92
                            else:
                                bin_num[27] = 93
                        else:
                            if (feature[2]<=3.0):
                                bin_num[27] = 94
                            else:
                                bin_num[27] = 95
        else:
            if (feature[1]<=3.0):
                if (feature[21]<=0.0):
                    if (feature[2]<=3.0):
                        if (feature[18]<=0.0):
                            if (feature[23]<=0.0):
                                bin_num[27] = 96
                            else:
                                bin_num[27] = 97
                        else:
                            if (feature[5]<=15.0):
                                bin_num[27] = 98
                            else:
                                bin_num[27] = 99
                    else:
                        if (feature[35]<=0.0):
                            if (feature[24]<=0.0):
                                bin_num[27] = 100
                            else:
                                bin_num[27] = 101
                        else:
                            if (feature[25]<=0.0):
                                bin_num[27] = 102
                            else:
                                bin_num[27] = 103
                else:
                    if (feature[34]<=0.0):
                        if (feature[23]<=0.0):
                            if (feature[12]<=2.0):
                                bin_num[27] = 104
                            else:
                                bin_num[27] = 105
                        else:
                            if (feature[6]<=2.0):
                                bin_num[27] = 106
                            else:
                                bin_num[27] = 107
                    else:
                        if (feature[18]<=0.0):
                            if (feature[12]<=2.0):
                                bin_num[27] = 108
                            else:
                                bin_num[27] = 109
                        else:
                            if (feature[19]<=0.0):
                                bin_num[27] = 110
                            else:
                                bin_num[27] = 111
            else:
                if (feature[28]<=0.0):
                    if (feature[24]<=0.0):
                        if (feature[18]<=0.0):
                            if (feature[17]<=0.0):
                                bin_num[27] = 112
                            else:
                                bin_num[27] = 113
                        else:
                            if (feature[19]<=0.0):
                                bin_num[27] = 114
                            else:
                                bin_num[27] = 115
                    else:
                        if (feature[6]<=2.0):
                            if (feature[0]<=0.0):
                                bin_num[27] = 116
                            else:
                                bin_num[27] = 117
                        else:
                            if (feature[21]<=0.0):
                                bin_num[27] = 118
                            else:
                                bin_num[27] = 119
                else:
                    if (feature[34]<=0.0):
                        if (feature[21]<=0.0):
                            if (feature[10]<=1.0):
                                bin_num[27] = 120
                            else:
                                bin_num[27] = 121
                        else:
                            if (feature[4]<=2727.0):
                                bin_num[27] = 122
                            else:
                                bin_num[27] = 123
                    else:
                        if (feature[21]<=0.0):
                            if (feature[25]<=0.0):
                                bin_num[27] = 124
                            else:
                                bin_num[27] = 125
                        else:
                            if (feature[7]<=7.0):
                                bin_num[27] = 126
                            else:
                                bin_num[27] = 127
    # Tree 28
    if (feature[17]<=0.0):
        if (feature[2]<=3.0):
            if (feature[7]<=7.0):
                if (feature[0]<=0.0):
                    if (feature[13]<=0.0):
                        if (feature[29]<=0.0):
                            if (feature[35]<=0.0):
                                bin_num[28] = 0
                            else:
                                bin_num[28] = 1
                        else:
                            if (feature[38]<=0.0):
                                bin_num[28] = 2
                            else:
                                bin_num[28] = 3
                    else:
                        if (feature[4]<=2700.0):
                            if (feature[38]<=0.0):
                                bin_num[28] = 4
                            else:
                                bin_num[28] = 5
                        else:
                            if (feature[29]<=0.0):
                                bin_num[28] = 6
                            else:
                                bin_num[28] = 7
                else:
                    if (feature[19]<=0.0):
                        if (feature[29]<=0.0):
                            if (feature[1]<=2.0):
                                bin_num[28] = 8
                            else:
                                bin_num[28] = 9
                        else:
                            if (feature[36]<=0.0):
                                bin_num[28] = 10
                            else:
                                bin_num[28] = 11
                    else:
                        if (feature[25]<=0.0):
                            if (feature[6]<=2.0):
                                bin_num[28] = 12
                            else:
                                bin_num[28] = 13
                        else:
                            if (feature[23]<=0.0):
                                bin_num[28] = 14
                            else:
                                bin_num[28] = 15
            else:
                if (feature[4]<=2700.0):
                    if (feature[18]<=0.0):
                        if (feature[9]<=0.0):
                            if (feature[13]<=0.0):
                                bin_num[28] = 16
                            else:
                                bin_num[28] = 17
                        else:
                            if (feature[38]<=0.0):
                                bin_num[28] = 18
                            else:
                                bin_num[28] = 19
                    else:
                        if (feature[23]<=0.0):
                            if (feature[3]<=2.0):
                                bin_num[28] = 20
                            else:
                                bin_num[28] = 21
                        else:
                            if (feature[11]<=0.0):
                                bin_num[28] = 22
                            else:
                                bin_num[28] = 23
                else:
                    if (feature[26]<=0.0):
                        if (feature[1]<=2.0):
                            if (feature[22]<=0.0):
                                bin_num[28] = 24
                            else:
                                bin_num[28] = 25
                        else:
                            if (feature[12]<=2.0):
                                bin_num[28] = 26
                            else:
                                bin_num[28] = 27
                    else:
                        if (feature[10]<=1.0):
                            if (feature[12]<=2.0):
                                bin_num[28] = 28
                            else:
                                bin_num[28] = 29
                        else:
                            if (feature[20]<=0.0):
                                bin_num[28] = 30
                            else:
                                bin_num[28] = 31
        else:
            if (feature[4]<=2700.0):
                if (feature[13]<=0.0):
                    if (feature[37]<=0.0):
                        if (feature[24]<=0.0):
                            if (feature[18]<=0.0):
                                bin_num[28] = 32
                            else:
                                bin_num[28] = 33
                        else:
                            if (feature[34]<=0.0):
                                bin_num[28] = 34
                            else:
                                bin_num[28] = 35
                    else:
                        if (feature[26]<=0.0):
                            if (feature[33]<=0.0):
                                bin_num[28] = 36
                            else:
                                bin_num[28] = 37
                        else:
                            if (feature[28]<=0.0):
                                bin_num[28] = 38
                            else:
                                bin_num[28] = 39
                else:
                    if (feature[36]<=0.0):
                        if (feature[11]<=0.0):
                            if (feature[37]<=0.0):
                                bin_num[28] = 40
                            else:
                                bin_num[28] = 41
                        else:
                            if (feature[23]<=0.0):
                                bin_num[28] = 42
                            else:
                                bin_num[28] = 43
                    else:
                        if (feature[7]<=7.0):
                            if (feature[10]<=1.0):
                                bin_num[28] = 44
                            else:
                                bin_num[28] = 45
                        else:
                            if (feature[18]<=0.0):
                                bin_num[28] = 46
                            else:
                                bin_num[28] = 47
            else:
                if (feature[5]<=16.0):
                    if (feature[10]<=1.0):
                        if (feature[34]<=0.0):
                            if (feature[23]<=0.0):
                                bin_num[28] = 48
                            else:
                                bin_num[28] = 49
                        else:
                            if (feature[26]<=0.0):
                                bin_num[28] = 50
                            else:
                                bin_num[28] = 51
                    else:
                        if (feature[8]<=35.0):
                            if (feature[12]<=2.0):
                                bin_num[28] = 52
                            else:
                                bin_num[28] = 53
                        else:
                            if (feature[37]<=0.0):
                                bin_num[28] = 54
                            else:
                                bin_num[28] = 55
                else:
                    if (feature[7]<=7.0):
                        if (feature[37]<=0.0):
                            if (feature[29]<=0.0):
                                bin_num[28] = 56
                            else:
                                bin_num[28] = 57
                        else:
                            if (feature[3]<=2.0):
                                bin_num[28] = 58
                            else:
                                bin_num[28] = 59
                    else:
                        if (feature[29]<=0.0):
                            if (feature[27]<=0.0):
                                bin_num[28] = 60
                            else:
                                bin_num[28] = 61
                        else:
                            if (feature[35]<=0.0):
                                bin_num[28] = 62
                            else:
                                bin_num[28] = 63
    else:
        if (feature[11]<=0.0):
            if (feature[4]<=2700.0):
                if (feature[34]<=0.0):
                    if (feature[9]<=0.0):
                        if (feature[29]<=0.0):
                            if (feature[7]<=7.0):
                                bin_num[28] = 64
                            else:
                                bin_num[28] = 65
                        else:
                            if (feature[28]<=0.0):
                                bin_num[28] = 66
                            else:
                                bin_num[28] = 67
                    else:
                        if (feature[5]<=16.0):
                            if (feature[7]<=7.0):
                                bin_num[28] = 68
                            else:
                                bin_num[28] = 69
                        else:
                            if (feature[7]<=7.0):
                                bin_num[28] = 70
                            else:
                                bin_num[28] = 71
                else:
                    if (feature[22]<=0.0):
                        if (feature[20]<=0.0):
                            if (feature[21]<=0.0):
                                bin_num[28] = 72
                            else:
                                bin_num[28] = 73
                        else:
                            if (feature[21]<=0.0):
                                bin_num[28] = 74
                            else:
                                bin_num[28] = 75
                    else:
                        if (feature[21]<=0.0):
                            if (feature[19]<=0.0):
                                bin_num[28] = 76
                            else:
                                bin_num[28] = 77
                        else:
                            if (feature[18]<=0.0):
                                bin_num[28] = 78
                            else:
                                bin_num[28] = 79
            else:
                if (feature[7]<=7.0):
                    if (feature[35]<=0.0):
                        if (feature[2]<=3.0):
                            if (feature[26]<=0.0):
                                bin_num[28] = 80
                            else:
                                bin_num[28] = 81
                        else:
                            if (feature[18]<=0.0):
                                bin_num[28] = 82
                            else:
                                bin_num[28] = 83
                    else:
                        if (feature[28]<=0.0):
                            if (feature[18]<=0.0):
                                bin_num[28] = 84
                            else:
                                bin_num[28] = 85
                        else:
                            if (feature[6]<=2.0):
                                bin_num[28] = 86
                            else:
                                bin_num[28] = 87
                else:
                    if (feature[12]<=2.0):
                        if (feature[2]<=3.0):
                            if (feature[26]<=0.0):
                                bin_num[28] = 88
                            else:
                                bin_num[28] = 89
                        else:
                            if (feature[22]<=0.0):
                                bin_num[28] = 90
                            else:
                                bin_num[28] = 91
                    else:
                        if (feature[3]<=2.0):
                            if (feature[13]<=0.0):
                                bin_num[28] = 92
                            else:
                                bin_num[28] = 93
                        else:
                            if (feature[1]<=2.0):
                                bin_num[28] = 94
                            else:
                                bin_num[28] = 95
        else:
            if (feature[34]<=0.0):
                if (feature[5]<=16.0):
                    if (feature[10]<=1.0):
                        if (feature[18]<=0.0):
                            if (feature[16]<=0.0):
                                bin_num[28] = 96
                            else:
                                bin_num[28] = 97
                        else:
                            if (feature[26]<=0.0):
                                bin_num[28] = 98
                            else:
                                bin_num[28] = 99
                    else:
                        if (feature[26]<=0.0):
                            if (feature[29]<=0.0):
                                bin_num[28] = 100
                            else:
                                bin_num[28] = 101
                        else:
                            if (feature[21]<=0.0):
                                bin_num[28] = 102
                            else:
                                bin_num[28] = 103
                else:
                    if (feature[27]<=0.0):
                        if (feature[29]<=0.0):
                            if (feature[26]<=0.0):
                                bin_num[28] = 104
                            else:
                                bin_num[28] = 105
                        else:
                            if (feature[19]<=0.0):
                                bin_num[28] = 106
                            else:
                                bin_num[28] = 107
                    else:
                        if (feature[33]<=0.0):
                            if (feature[18]<=0.0):
                                bin_num[28] = 108
                            else:
                                bin_num[28] = 109
                        else:
                            if (feature[10]<=1.0):
                                bin_num[28] = 110
                            else:
                                bin_num[28] = 111
            else:
                if (feature[25]<=0.0):
                    if (feature[9]<=0.0):
                        if (feature[33]<=0.0):
                            if (feature[28]<=0.0):
                                bin_num[28] = 112
                            else:
                                bin_num[28] = 113
                        else:
                            if (feature[8]<=35.0):
                                bin_num[28] = 114
                            else:
                                bin_num[28] = 115
                    else:
                        if (feature[32]<=0.0):
                            if (feature[28]<=0.0):
                                bin_num[28] = 116
                            else:
                                bin_num[28] = 117
                        else:
                            if (feature[35]<=0.0):
                                bin_num[28] = 118
                            else:
                                bin_num[28] = 119
                else:
                    if (feature[8]<=35.0):
                        if (feature[24]<=0.0):
                            if (feature[12]<=2.0):
                                bin_num[28] = 120
                            else:
                                bin_num[28] = 121
                        else:
                            if (feature[35]<=0.0):
                                bin_num[28] = 122
                            else:
                                bin_num[28] = 123
                    else:
                        if (feature[12]<=2.0):
                            if (feature[7]<=7.0):
                                bin_num[28] = 124
                            else:
                                bin_num[28] = 125
                        else:
                            if (feature[7]<=7.0):
                                bin_num[28] = 126
                            else:
                                bin_num[28] = 127
    # Tree 29
    if (feature[20]<=0.0):
        if (feature[35]<=0.0):
            if (feature[18]<=0.0):
                if (feature[19]<=0.0):
                    if (feature[24]<=0.0):
                        if (feature[28]<=0.0):
                            if (feature[21]<=0.0):
                                bin_num[29] = 0
                            else:
                                bin_num[29] = 1
                        else:
                            if (feature[21]<=0.0):
                                bin_num[29] = 2
                            else:
                                bin_num[29] = 3
                    else:
                        if (feature[23]<=0.0):
                            if (feature[22]<=0.0):
                                bin_num[29] = 4
                            else:
                                bin_num[29] = 5
                        else:
                            if (feature[25]<=0.0):
                                bin_num[29] = 6
                            else:
                                bin_num[29] = 7
                else:
                    if (feature[26]<=0.0):
                        if (feature[22]<=0.0):
                            if (feature[23]<=0.0):
                                bin_num[29] = 8
                            else:
                                bin_num[29] = 9
                        else:
                            if (feature[23]<=0.0):
                                bin_num[29] = 10
                            else:
                                bin_num[29] = 11
                    else:
                        if (feature[2]<=3.0):
                            if (feature[22]<=0.0):
                                bin_num[29] = 12
                            else:
                                bin_num[29] = 13
                        else:
                            if (feature[1]<=2.0):
                                bin_num[29] = 14
                            else:
                                bin_num[29] = 15
            else:
                if (feature[19]<=0.0):
                    if (feature[24]<=0.0):
                        if (feature[33]<=0.0):
                            if (feature[26]<=0.0):
                                bin_num[29] = 16
                            else:
                                bin_num[29] = 17
                        else:
                            if (feature[1]<=2.0):
                                bin_num[29] = 18
                            else:
                                bin_num[29] = 19
                    else:
                        if (feature[13]<=0.0):
                            if (feature[4]<=2692.0):
                                bin_num[29] = 20
                            else:
                                bin_num[29] = 21
                        else:
                            if (feature[7]<=7.0):
                                bin_num[29] = 22
                            else:
                                bin_num[29] = 23
                else:
                    if (feature[27]<=0.0):
                        if (feature[22]<=0.0):
                            if (feature[33]<=0.0):
                                bin_num[29] = 24
                            else:
                                bin_num[29] = 25
                        else:
                            if (feature[26]<=0.0):
                                bin_num[29] = 26
                            else:
                                bin_num[29] = 27
                    else:
                        if (feature[33]<=0.0):
                            if (feature[22]<=0.0):
                                bin_num[29] = 28
                            else:
                                bin_num[29] = 29
                        else:
                            if (feature[12]<=2.0):
                                bin_num[29] = 30
                            else:
                                bin_num[29] = 31
        else:
            if (feature[33]<=0.0):
                if (feature[34]<=0.0):
                    if (feature[8]<=36.0):
                        if (feature[5]<=16.0):
                            if (feature[38]<=0.0):
                                bin_num[29] = 32
                            else:
                                bin_num[29] = 33
                        else:
                            if (feature[37]<=0.0):
                                bin_num[29] = 34
                            else:
                                bin_num[29] = 35
                    else:
                        if (feature[28]<=0.0):
                            if (feature[27]<=0.0):
                                bin_num[29] = 36
                            else:
                                bin_num[29] = 37
                        else:
                            if (feature[18]<=0.0):
                                bin_num[29] = 38
                            else:
                                bin_num[29] = 39
                else:
                    if (feature[13]<=0.0):
                        if (feature[4]<=2692.0):
                            if (feature[18]<=0.0):
                                bin_num[29] = 40
                            else:
                                bin_num[29] = 41
                        else:
                            if (feature[18]<=0.0):
                                bin_num[29] = 42
                            else:
                                bin_num[29] = 43
                    else:
                        if (feature[23]<=0.0):
                            if (feature[21]<=0.0):
                                bin_num[29] = 44
                            else:
                                bin_num[29] = 45
                        else:
                            if (feature[25]<=0.0):
                                bin_num[29] = 46
                            else:
                                bin_num[29] = 47
            else:
                if (feature[24]<=0.0):
                    if (feature[23]<=0.0):
                        if (feature[18]<=0.0):
                            if (feature[37]<=0.0):
                                bin_num[29] = 48
                            else:
                                bin_num[29] = 49
                        else:
                            if (feature[34]<=0.0):
                                bin_num[29] = 50
                            else:
                                bin_num[29] = 51
                    else:
                        if (feature[13]<=0.0):
                            if (feature[18]<=0.0):
                                bin_num[29] = 52
                            else:
                                bin_num[29] = 53
                        else:
                            if (feature[1]<=2.0):
                                bin_num[29] = 54
                            else:
                                bin_num[29] = 55
                else:
                    if (feature[1]<=2.0):
                        if (feature[21]<=0.0):
                            if (feature[12]<=2.0):
                                bin_num[29] = 56
                            else:
                                bin_num[29] = 57
                        else:
                            if (feature[0]<=0.0):
                                bin_num[29] = 58
                            else:
                                bin_num[29] = 59
                    else:
                        if (feature[27]<=0.0):
                            if (feature[5]<=16.0):
                                bin_num[29] = 60
                            else:
                                bin_num[29] = 61
                        else:
                            if (feature[5]<=16.0):
                                bin_num[29] = 62
                            else:
                                bin_num[29] = 63
    else:
        if (feature[18]<=0.0):
            if (feature[34]<=0.0):
                if (feature[6]<=2.0):
                    if (feature[12]<=2.0):
                        if (feature[3]<=2.0):
                            if (feature[0]<=0.0):
                                bin_num[29] = 64
                            else:
                                bin_num[29] = 65
                        else:
                            if (feature[23]<=0.0):
                                bin_num[29] = 66
                            else:
                                bin_num[29] = 67
                    else:
                        if (feature[25]<=0.0):
                            if (feature[23]<=0.0):
                                bin_num[29] = 68
                            else:
                                bin_num[29] = 69
                        else:
                            if (feature[35]<=0.0):
                                bin_num[29] = 70
                            else:
                                bin_num[29] = 71
                else:
                    if (feature[3]<=2.0):
                        if (feature[26]<=0.0):
                            if (feature[19]<=0.0):
                                bin_num[29] = 72
                            else:
                                bin_num[29] = 73
                        else:
                            if (feature[2]<=3.0):
                                bin_num[29] = 74
                            else:
                                bin_num[29] = 75
                    else:
                        if (feature[1]<=2.0):
                            if (feature[2]<=3.0):
                                bin_num[29] = 76
                            else:
                                bin_num[29] = 77
                        else:
                            if (feature[17]<=0.0):
                                bin_num[29] = 78
                            else:
                                bin_num[29] = 79
            else:
                if (feature[28]<=0.0):
                    if (feature[19]<=0.0):
                        if (feature[24]<=0.0):
                            if (feature[12]<=2.0):
                                bin_num[29] = 80
                            else:
                                bin_num[29] = 81
                        else:
                            if (feature[26]<=0.0):
                                bin_num[29] = 82
                            else:
                                bin_num[29] = 83
                    else:
                        if (feature[26]<=0.0):
                            if (feature[21]<=0.0):
                                bin_num[29] = 84
                            else:
                                bin_num[29] = 85
                        else:
                            if (feature[23]<=0.0):
                                bin_num[29] = 86
                            else:
                                bin_num[29] = 87
                else:
                    if (feature[1]<=2.0):
                        if (feature[23]<=0.0):
                            if (feature[26]<=0.0):
                                bin_num[29] = 88
                            else:
                                bin_num[29] = 89
                        else:
                            if (feature[11]<=0.0):
                                bin_num[29] = 90
                            else:
                                bin_num[29] = 91
                    else:
                        if (feature[10]<=1.0):
                            if (feature[25]<=0.0):
                                bin_num[29] = 92
                            else:
                                bin_num[29] = 93
                        else:
                            if (feature[29]<=0.0):
                                bin_num[29] = 94
                            else:
                                bin_num[29] = 95
        else:
            if (feature[29]<=0.0):
                if (feature[19]<=0.0):
                    if (feature[24]<=0.0):
                        if (feature[28]<=0.0):
                            if (feature[26]<=0.0):
                                bin_num[29] = 96
                            else:
                                bin_num[29] = 97
                        else:
                            if (feature[26]<=0.0):
                                bin_num[29] = 98
                            else:
                                bin_num[29] = 99
                    else:
                        if (feature[10]<=1.0):
                            if (feature[35]<=0.0):
                                bin_num[29] = 100
                            else:
                                bin_num[29] = 101
                        else:
                            if (feature[35]<=0.0):
                                bin_num[29] = 102
                            else:
                                bin_num[29] = 103
                else:
                    if (feature[35]<=0.0):
                        if (feature[0]<=0.0):
                            if (feature[27]<=0.0):
                                bin_num[29] = 104
                            else:
                                bin_num[29] = 105
                        else:
                            if (feature[26]<=0.0):
                                bin_num[29] = 106
                            else:
                                bin_num[29] = 107
                    else:
                        if (feature[11]<=0.0):
                            if (feature[3]<=2.0):
                                bin_num[29] = 108
                            else:
                                bin_num[29] = 109
                        else:
                            if (feature[23]<=0.0):
                                bin_num[29] = 110
                            else:
                                bin_num[29] = 111
            else:
                if (feature[10]<=1.0):
                    if (feature[1]<=2.0):
                        if (feature[24]<=0.0):
                            if (feature[19]<=0.0):
                                bin_num[29] = 112
                            else:
                                bin_num[29] = 113
                        else:
                            if (feature[35]<=0.0):
                                bin_num[29] = 114
                            else:
                                bin_num[29] = 115
                    else:
                        if (feature[24]<=0.0):
                            if (feature[19]<=0.0):
                                bin_num[29] = 116
                            else:
                                bin_num[29] = 117
                        else:
                            if (feature[0]<=0.0):
                                bin_num[29] = 118
                            else:
                                bin_num[29] = 119
                else:
                    if (feature[7]<=7.0):
                        if (feature[5]<=16.0):
                            if (feature[9]<=0.0):
                                bin_num[29] = 120
                            else:
                                bin_num[29] = 121
                        else:
                            if (feature[12]<=2.0):
                                bin_num[29] = 122
                            else:
                                bin_num[29] = 123
                    else:
                        if (feature[34]<=0.0):
                            if (feature[21]<=0.0):
                                bin_num[29] = 124
                            else:
                                bin_num[29] = 125
                        else:
                            if (feature[21]<=0.0):
                                bin_num[29] = 126
                            else:
                                bin_num[29] = 127
    
    final_features = []
    for i in range(30):
        string = str(i+1) + ":" + str(int(bin_num[i]))
        hashed_bin = int(int(hashlib.md5(string.encode('utf8')).hexdigest(), 16)%numHashBuckets)
        final_features.append(hashed_bin)
    
    #now handle integer, #first 13 items in feature vector is an integer
    for i in range(14):
        #create text like "I1-3"
        key = "I" + str(i)
        featureValue = feature[i]
        #if len(featureValue) == 0: #empty value will be treated as zero
        #    featureValue = 0
        
        if int(featureValue) > 2:
            featureValue = int(math.log(float(featureValue))**2)
        else: 
            featureValue = 'SP'+str(featureValue)
        final_features.append(hashLike3Idiots(key+"-" + str(featureValue),numHashBuckets))
        #final_features.append(key+"-" + str(featureValue))

    #now handle cateogry
    for index, featureValue in enumerate(point[1][1][1]):
        key = "C" + str(index)

        #create text like "C16_913ff151"
        keyValueString = key + "_" + featureValue

        #print keyValueString
        if not keyValueString in frequentCategories: #did this cat happen more than 10 times? 
            keyValueString = key + 'less' #per 3 idiots' source code

        #final_features.append(keyValueString)
        final_features.append(hashLike3Idiots(keyValueString,numHashBuckets))

    label = point[0]

    #print final_features
    
#    new_point = LabeledPoint(point.label, final_features)
    return getFinalLabeledPoint(label, final_features,numHashBuckets)

def parsePoint(point):
    ##exclude the first 13 features always as they are numerical
    return ([(i,j)for i,j in enumerate(point.split(',')[14:])])

def createOneHotDict(inputData):
    sampleDistinctFeats = (inputData #.flatMap(filterNumbers)
                         .flatMap(lambda x: x)
                      .distinct())
    return (sampleDistinctFeats
                           .zipWithIndex()
                             .collectAsMap())  

# TODO: Replace <FILL IN> with appropriate code
def oneHotEncoding(rawFeats, OHEDict, numOHEFeats,first13, last26):
    
    rawFeats=sorted(rawFeats)
    num13=[]
    arr13=[]
    for j,i in enumerate(first13):
        if i != '':
            num13.append(j)
            arr13.append(i)
    num26=[]
    arr26=[]
    for j,i in enumerate(last26):
        if i != '':
            num26.append(j + 39)
            arr26.append(i)
    OHEFeats=[]
    for i in rawFeats:
        if i in OHEDict.keys():
            OHEFeats.append(i)

    return (SparseVector(13+26, \
                        sorted(num13+[OHEDict[i]+13 for i in OHEFeats]),\
                        arr13+[1.0 for i in range(len(OHEFeats))]),
                        (num26,arr26))
            
#    return SparseVector(13+26+26,sorted(num13+\
#                            [OHEDict[i]+13 for i in OHEFeats]+num26),\
#                        arr13+[1.0 for i in range(len(OHEFeats))]+arr26)


def parseOHEPoint(point, OHEDict, numOHEFeats):
    #input
    #(u'0,1,1,5,0,1382,9727dd16, so on... ')
    featurelist=point.strip().split(',')

    new_point = (featurelist[0],oneHotEncoding([(i,j) for i,j in enumerate(featurelist[14:]) ],\
                                                      OHEDict, 13+26+26,[i for i in featurelist[1:14]], \
                                                                        [i for i in featurelist[14:]]))

    return new_point

def maaro(z):
    if z[1]=='':
        return (-1,0)
    else:
        return(z,1)

"""
def parseNonGBDTFeatures(point, frequentCategories,numHashBuckets):
    #format
    #(u'0,1,1,5,0,1382,9727dd16, so on... ', 0) 

    indexCount = 0
    catCount = 0
    features = point[0].split(',')

    modFeatures = []
    
    #print features
    
    for index, featureValue in enumerate(features):
        if index != 0: #ignore first one (label)
            if index <14: #integer
                #create text like "I1-3"
                key = "I" + str(index)
                #print featureValue
                #print index
                if len(featureValue) == 0: #empty value will be treated as zero
                    featureValue = 0
                    
                if int(featureValue) > 2:
                    featureValue = int(math.log(float(featureValue))**2)
                else: 
                    featureValue = 'SP'+str(featureValue)
                modFeatures.append(hashLike3Idiots(key+"-" + str(featureValue),numHashBuckets))
                indexCount +=1
            else:

                key = "C" + str(catCount)
                
                #create text like "C16_913ff151"
                keyValueString = key + "_" + featureValue
                
                #print keyValueString
                
                if not keyValueString in frequentCategories: #did this cat happen more than 10 times? 
                    keyValueString = key + 'less' #per 3 idiots' source code
                    
                modFeatures.append(hashLike3Idiots(keyValueString,numHashBuckets))
                
                catCount +=1
    
    #print indexCount
    #print catCount
    #output format (rowindex, label, features)
    
    #print modFeatures
    label = int(features[0])
    rowIndex = point[1]
    return (rowIndex,(label,modFeatures))
"""

#get Labeled Point based on my arr
def getFinalLabeledPoint(label, myarr,numBuckets):
    
    #remove duplicates
    myarr = sorted(list(set(myarr)))

    keyArray = []
    countArray = []

    for item in myarr:
        keyArray.append(item)
        countArray.append(1)
    #print numBuckets
    #print keyArray
    #print countArray
    #return SparseVector(numBuckets,keyArray,countArray)
    return LabeledPoint(label,SparseVector(numBuckets,keyArray,countArray))

def processFinalJoin(point,numBuckets):
    
    #(x[1][0][0],x[1][0][1] + x[1][1][1]))
    label = point[1][0][0]
    features = point[1][0][1] + point[1][1][1]  
    return getFinalLabeledPoint(label, features,numBuckets)

def run_bins(input_file,output_file, numHashBuckets, frequentCategories_file):
    #repeat of before to generate OHETrainDataBins
    dataRDD=sc.textFile(input_file).map(lambda x: x.replace('\t',','))  #.zipWithIndex()
    #format
    #last integer is an index of the record, we will use it to join result of GBDT with additional Preprocessing B result
    #(u'0,1,1,5,0,1382,9727dd16, so on... ', 0) 
    dataRDD.cache()

#############################    
##### Begin Preprocessing B for integer and categories
#     frequentCategoriesRDD = sc.textFile(frequentCategories_file).collect() #format-- array of text like C14_23425
    
#     freqCategories = sc.broadcast(frequentCategoriesRDD)
#     modifiedIntAndCat = dataRDD.map(lambda x: parseNonGBDTFeatures(x,freqCategories.value, numHashBuckets))
#     #print modifiedIntAndCat.take(1)
#     #format (HASHED of below)
#     #[(rowIndex, (label, ['I1-SP1', 'I2-SP1', 'I3-2', 'I4-SP0', 'I5-52', 'I6-1', 'I7-7', 'I8-SP2', 'I9-27', 'I10-SP1', 'I11-SP2', 'I12-SP0', 'I13-SP2', u'C0_68fd1e64', u'C1_80e26c9b', 'C2less', 'C3less', u'C4_25c83c98', u'C5_7e0ccccf', u'C6_de7995b8', u'C7_1f89b562', u'C8_a73ee510', u'C9_a8cd5504', u'C10_b2cb9c98', 'C11less', u'C12_2824a5f6', u'C13_1adce6ef', u'C14_8ba8b39a', 'C15less', u'C16_e5ba7672', u'C17_f54016b9', u'C18_21ddcdc9', u'C19_b1252a9d', 'C20less', u'C21_', u'C22_3a171ecb', u'C23_c5c50484', u'C24_e8b83407', 'C25less']))]  
##### END Preprocessing B for integer and categories
#############################    

    frequentCategories = sc.textFile(frequentCategories_file).collect() #format-- array of text like C14_23425
#     freqCategories = sc.broadcast(frequentCategoriesRDD)
    
    
############################    
##### Begin GBDT processing

    dataRDDParsed=dataRDD.map(parsePoint).cache()
    #format
    #([....(24, u'e8b83407'), (25, u'9727dd16')], 0)
    
    #print dataRDDParsed.take(1)
    featSet=dataRDDParsed.flatMap(lambda x: x).map(maaro) \
        .reduceByKey(lambda a,b: a+b).takeOrdered(26,lambda (k,v): -v)
        
    OHEdict={}
    for i,x in enumerate(featSet):
        OHEdict[x[0]]=i

    OHETrainData = dataRDD.map(lambda point: parseOHEPoint(point, OHEdict, 13+26+26))
    
    #print OHETrainData.take(1)
    #return 
    #OHETrainData should now be in the format:
    #(SparseVector(65, [0, ..., 64], [I0, I1, ..., I12, OHE0, OHE1, ..., OHE25, C0, C1, ..., C25]))
    #print "OHETrain"
    #print OHETrainData.take(1)
        
    #apply the new decision tree
#     OHETrainDataDense = OHETrainData.map(lambda x: SparseVector.toArray(x.features))
#     OHETrainDataBins = OHETrainDataDense.map(lambda x: get_bins(x))
#     OHETrainDataBins.coalesce(1).saveAsTextFile(output_file)


#     OHETrainDataBins = OHETrainData.map(lambda point: get_hashed_bins(point, numHashBuckets,freqCategories.value))
    OHETrainDataBins = OHETrainData.map(lambda point: get_hashed_bins(point, numHashBuckets,frequentCategories))



#   OHETrainDataBins.saveAsTextFile(output_file)   
    #OHETrainDataBins format:
    #(rowindex, (label, [hashed GBDT assignment 232, 384, 576, 952, 528, 960, 984, 600, 552, 640, 576, 296, 144, 344, 744, 480, 832, 96, 536, 256, 304, 264, 160, 632, 960, 312, 440, 400, 264, 304]))]
##### End GBDT processing    
############################    
    
    
############Now merge set of two features
    #joined = OHETrainDataBins.join(modifiedIntAndCat)
    #after join
    #[(0, ((u'0', [232, 384, 576, 952, 528, 960, 984, 600, 552, 640, 576, 296, 144, 344, 744, 480, 832, 96, 536, 256, 304, 264, 160, 632, 960, 312, 440, 400, 264, 304]),
     #     (0, [480, 720, 688, 856, 392, 24, 184, 480, 432, 696, 16, 368, 352, 368, 368, 160, 608, 392, 680, 768, 936, 432, 424, 112, 840, 264, 536, 152, 80, 440, 360, 640, 600, 520, 304, 128, 592, 952, 536])))]

    #joinedProcessed = joined.map(lambda x: (x[1][0][0],x[1][0][1] + x[1][1][1]))
    #joinedProcessed.cache()
    #print joinedProcessed.take(1)

    #print joinedProcessed.map(lambda x: getFinalLabeledPoint(x[0], x[1], numHashBuckets)).take(1)

    #return 
#     FinalLabeledPoint =  OHETrainDataBins.join(modifiedIntAndCat).map(lambda x: processFinalJoin(x,numHashBuckets))

    #freqCategories.unpersist()
    MLUtils.saveAsLibSVMFile(OHETrainDataBins, output_file) 
    

if __name__== '__main__':
    
    if len(sys.argv) < 4:
        print >> sys.stderr, "Usage: <input file> <output file> <number of hash buckets>  <frequentCategories>"
        exit(-1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    numHashBuckets = float(sys.argv[3])
    freqCats = sys.argv[4]
    
    sc = SparkContext(appName="GBDT2")
    run_bins(input_file,output_file, numHashBuckets,freqCats)
    sc.stop()
