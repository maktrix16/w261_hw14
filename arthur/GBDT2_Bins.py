#!/usr/bin/env python
import sys
from pyspark import SparkContext
from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.linalg import SparseVector
from pyspark.mllib.util import MLUtils
from types import *

def get_bins(feature):
    bin_num = {} 
    
#NEW_RULES_HERE
    # Tree 0
    if (feature[0]<=0.0):
        if (feature[10]<=1.0):
            if (feature[12]<=3.0):
                if (feature[19]<=0.0):
                    if (feature[18]<=0.0):
                        if (feature[3]<=3.0):
                            if (feature[13]<=0.0):
                                bin_num[0] = 0
                            else:
                                bin_num[0] = 1
                        else:
                            if (feature[25]<=0.0):
                                bin_num[0] = 2
                            else:
                                bin_num[0] = 3
                    else:
                        if (feature[35]<=0.0):
                            if (feature[20]<=0.0):
                                bin_num[0] = 4
                            else:
                                bin_num[0] = 5
                        else:
                            if (feature[17]<=0.0):
                                bin_num[0] = 6
                            else:
                                bin_num[0] = 7
                else:
                    if (feature[8]<=37.0):
                        if (feature[2]<=4.0):
                            if (feature[7]<=7.0):
                                bin_num[0] = 8
                            else:
                                bin_num[0] = 9
                        else:
                            if (feature[13]<=0.0):
                                bin_num[0] = 10
                            else:
                                bin_num[0] = 11
                    else:
                        if (feature[3]<=3.0):
                            if (feature[35]<=0.0):
                                bin_num[0] = 12
                            else:
                                bin_num[0] = 13
                        else:
                            if (feature[7]<=7.0):
                                bin_num[0] = 14
                            else:
                                bin_num[0] = 15
            else:
                if (feature[6]<=2.0):
                    if (feature[35]<=0.0):
                        if (feature[23]<=0.0):
                            if (feature[2]<=4.0):
                                bin_num[0] = 16
                            else:
                                bin_num[0] = 17
                        else:
                            if (feature[19]<=0.0):
                                bin_num[0] = 18
                            else:
                                bin_num[0] = 19
                    else:
                        if (feature[18]<=0.0):
                            if (feature[11]<=0.0):
                                bin_num[0] = 20
                            else:
                                bin_num[0] = 21
                        else:
                            if (feature[17]<=0.0):
                                bin_num[0] = 22
                            else:
                                bin_num[0] = 23
                else:
                    if (feature[5]<=16.0):
                        if (feature[26]<=0.0):
                            if (feature[38]<=0.0):
                                bin_num[0] = 24
                            else:
                                bin_num[0] = 25
                        else:
                            if (feature[24]<=0.0):
                                bin_num[0] = 26
                            else:
                                bin_num[0] = 27
                    else:
                        if (feature[7]<=7.0):
                            if (feature[8]<=37.0):
                                bin_num[0] = 28
                            else:
                                bin_num[0] = 29
                        else:
                            if (feature[18]<=0.0):
                                bin_num[0] = 30
                            else:
                                bin_num[0] = 31
        else:
            if (feature[5]<=16.0):
                if (feature[12]<=3.0):
                    if (feature[20]<=0.0):
                        if (feature[19]<=0.0):
                            if (feature[38]<=0.0):
                                bin_num[0] = 32
                            else:
                                bin_num[0] = 33
                        else:
                            if (feature[16]<=0.0):
                                bin_num[0] = 34
                            else:
                                bin_num[0] = 35
                    else:
                        if (feature[35]<=0.0):
                            if (feature[8]<=37.0):
                                bin_num[0] = 36
                            else:
                                bin_num[0] = 37
                        else:
                            if (feature[7]<=7.0):
                                bin_num[0] = 38
                            else:
                                bin_num[0] = 39
                else:
                    if (feature[27]<=0.0):
                        if (feature[8]<=37.0):
                            if (feature[14]<=0.0):
                                bin_num[0] = 40
                            else:
                                bin_num[0] = 41
                        else:
                            if (feature[7]<=7.0):
                                bin_num[0] = 42
                            else:
                                bin_num[0] = 43
                    else:
                        if (feature[6]<=2.0):
                            bin_num[0] = 44
                        else:
                            if (feature[11]<=0.0):
                                bin_num[0] = 45
                            else:
                                bin_num[0] = 46
            else:
                if (feature[7]<=7.0):
                    if (feature[2]<=4.0):
                        if (feature[20]<=0.0):
                            if (feature[25]<=0.0):
                                bin_num[0] = 47
                            else:
                                bin_num[0] = 48
                        else:
                            if (feature[27]<=0.0):
                                bin_num[0] = 49
                            else:
                                bin_num[0] = 50
                    else:
                        if (feature[20]<=0.0):
                            if (feature[28]<=0.0):
                                bin_num[0] = 51
                            else:
                                bin_num[0] = 52
                        else:
                            if (feature[12]<=3.0):
                                bin_num[0] = 53
                            else:
                                bin_num[0] = 54
                else:
                    if (feature[12]<=3.0):
                        if (feature[19]<=0.0):
                            if (feature[22]<=0.0):
                                bin_num[0] = 55
                            else:
                                bin_num[0] = 56
                        else:
                            if (feature[21]<=0.0):
                                bin_num[0] = 57
                            else:
                                bin_num[0] = 58
                    else:
                        if (feature[22]<=0.0):
                            if (feature[29]<=0.0):
                                bin_num[0] = 59
                            else:
                                bin_num[0] = 60
                        else:
                            if (feature[2]<=4.0):
                                bin_num[0] = 61
                            else:
                                bin_num[0] = 62
    else:
        if (feature[12]<=3.0):
            if (feature[3]<=3.0):
                if (feature[6]<=2.0):
                    if (feature[5]<=16.0):
                        if (feature[24]<=0.0):
                            if (feature[21]<=0.0):
                                bin_num[0] = 63
                            else:
                                bin_num[0] = 64
                        else:
                            if (feature[38]<=0.0):
                                bin_num[0] = 65
                            else:
                                bin_num[0] = 66
                    else:
                        if (feature[27]<=0.0):
                            if (feature[13]<=0.0):
                                bin_num[0] = 67
                            else:
                                bin_num[0] = 68
                        else:
                            if (feature[19]<=0.0):
                                bin_num[0] = 69
                            else:
                                bin_num[0] = 70
                else:
                    if (feature[5]<=16.0):
                        if (feature[28]<=0.0):
                            if (feature[10]<=1.0):
                                bin_num[0] = 71
                            else:
                                bin_num[0] = 72
                        else:
                            if (feature[10]<=1.0):
                                bin_num[0] = 73
                            else:
                                bin_num[0] = 74
                    else:
                        if (feature[24]<=0.0):
                            if (feature[15]<=0.0):
                                bin_num[0] = 75
                            else:
                                bin_num[0] = 76
                        else:
                            if (feature[38]<=0.0):
                                bin_num[0] = 77
                            else:
                                bin_num[0] = 78
            else:
                if (feature[6]<=2.0):
                    if (feature[5]<=16.0):
                        if (feature[2]<=4.0):
                            if (feature[35]<=0.0):
                                bin_num[0] = 79
                            else:
                                bin_num[0] = 80
                        else:
                            if (feature[10]<=1.0):
                                bin_num[0] = 81
                            else:
                                bin_num[0] = 82
                    else:
                        if (feature[35]<=0.0):
                            if (feature[31]<=0.0):
                                bin_num[0] = 83
                            else:
                                bin_num[0] = 84
                        else:
                            if (feature[1]<=2.0):
                                bin_num[0] = 85
                            else:
                                bin_num[0] = 86
                else:
                    if (feature[21]<=0.0):
                        if (feature[28]<=0.0):
                            if (feature[19]<=0.0):
                                bin_num[0] = 87
                            else:
                                bin_num[0] = 88
                        else:
                            if (feature[29]<=0.0):
                                bin_num[0] = 89
                            else:
                                bin_num[0] = 90
                    else:
                        if (feature[22]<=0.0):
                            if (feature[25]<=0.0):
                                bin_num[0] = 91
                            else:
                                bin_num[0] = 92
                        else:
                            if (feature[16]<=0.0):
                                bin_num[0] = 93
                            else:
                                bin_num[0] = 94
        else:
            if (feature[5]<=16.0):
                if (feature[10]<=1.0):
                    if (feature[6]<=2.0):
                        if (feature[20]<=0.0):
                            if (feature[22]<=0.0):
                                bin_num[0] = 95
                            else:
                                bin_num[0] = 96
                        else:
                            if (feature[2]<=4.0):
                                bin_num[0] = 97
                            else:
                                bin_num[0] = 98
                    else:
                        if (feature[25]<=0.0):
                            if (feature[37]<=0.0):
                                bin_num[0] = 99
                            else:
                                bin_num[0] = 100
                        else:
                            if (feature[21]<=0.0):
                                bin_num[0] = 101
                            else:
                                bin_num[0] = 102
                else:
                    if (feature[24]<=0.0):
                        if (feature[27]<=0.0):
                            if (feature[21]<=0.0):
                                bin_num[0] = 103
                            else:
                                bin_num[0] = 104
                        else:
                            if (feature[6]<=2.0):
                                bin_num[0] = 105
                            else:
                                bin_num[0] = 106
                    else:
                        if (feature[1]<=2.0):
                            if (feature[21]<=0.0):
                                bin_num[0] = 107
                            else:
                                bin_num[0] = 108
                        else:
                            if (feature[7]<=7.0):
                                bin_num[0] = 109
                            else:
                                bin_num[0] = 110
            else:
                if (feature[10]<=1.0):
                    if (feature[24]<=0.0):
                        if (feature[2]<=4.0):
                            if (feature[21]<=0.0):
                                bin_num[0] = 111
                            else:
                                bin_num[0] = 112
                        else:
                            if (feature[28]<=0.0):
                                bin_num[0] = 113
                            else:
                                bin_num[0] = 114
                    else:
                        if (feature[36]<=0.0):
                            if (feature[8]<=37.0):
                                bin_num[0] = 115
                            else:
                                bin_num[0] = 116
                        else:
                            if (feature[15]<=0.0):
                                bin_num[0] = 117
                            else:
                                bin_num[0] = 118
                else:
                    if (feature[2]<=4.0):
                        if (feature[21]<=0.0):
                            if (feature[29]<=0.0):
                                bin_num[0] = 119
                            else:
                                bin_num[0] = 120
                        else:
                            if (feature[28]<=0.0):
                                bin_num[0] = 121
                            else:
                                bin_num[0] = 122
                    else:
                        if (feature[24]<=0.0):
                            if (feature[21]<=0.0):
                                bin_num[0] = 123
                            else:
                                bin_num[0] = 124
                        else:
                            if (feature[19]<=0.0):
                                bin_num[0] = 125
                            else:
                                bin_num[0] = 126
    # Tree 1
    if (feature[6]<=2.0):
        if (feature[7]<=7.0):
            if (feature[13]<=0.0):
                if (feature[35]<=0.0):
                    if (feature[5]<=15.0):
                        if (feature[21]<=0.0):
                            if (feature[18]<=0.0):
                                bin_num[1] = 0
                            else:
                                bin_num[1] = 1
                        else:
                            if (feature[17]<=0.0):
                                bin_num[1] = 2
                            else:
                                bin_num[1] = 3
                    else:
                        if (feature[8]<=36.0):
                            if (feature[14]<=0.0):
                                bin_num[1] = 4
                            else:
                                bin_num[1] = 5
                        else:
                            if (feature[2]<=4.0):
                                bin_num[1] = 6
                            else:
                                bin_num[1] = 7
                else:
                    if (feature[2]<=4.0):
                        if (feature[34]<=0.0):
                            if (feature[25]<=0.0):
                                bin_num[1] = 8
                            else:
                                bin_num[1] = 9
                        else:
                            if (feature[30]<=0.0):
                                bin_num[1] = 10
                            else:
                                bin_num[1] = 11
                    else:
                        if (feature[17]<=0.0):
                            if (feature[19]<=0.0):
                                bin_num[1] = 12
                            else:
                                bin_num[1] = 13
                        else:
                            if (feature[20]<=0.0):
                                bin_num[1] = 14
                            else:
                                bin_num[1] = 15
            else:
                if (feature[2]<=4.0):
                    if (feature[8]<=36.0):
                        if (feature[23]<=0.0):
                            if (feature[18]<=0.0):
                                bin_num[1] = 16
                            else:
                                bin_num[1] = 17
                        else:
                            if (feature[25]<=0.0):
                                bin_num[1] = 18
                            else:
                                bin_num[1] = 19
                    else:
                        if (feature[19]<=0.0):
                            if (feature[5]<=15.0):
                                bin_num[1] = 20
                            else:
                                bin_num[1] = 21
                        else:
                            if (feature[14]<=0.0):
                                bin_num[1] = 22
                            else:
                                bin_num[1] = 23
                else:
                    if (feature[23]<=0.0):
                        if (feature[4]<=1912.0):
                            if (feature[28]<=0.0):
                                bin_num[1] = 24
                            else:
                                bin_num[1] = 25
                        else:
                            if (feature[19]<=0.0):
                                bin_num[1] = 26
                            else:
                                bin_num[1] = 27
                    else:
                        if (feature[35]<=0.0):
                            if (feature[3]<=3.0):
                                bin_num[1] = 28
                            else:
                                bin_num[1] = 29
                        else:
                            if (feature[0]<=0.0):
                                bin_num[1] = 30
                            else:
                                bin_num[1] = 31
        else:
            if (feature[4]<=1912.0):
                if (feature[19]<=0.0):
                    if (feature[20]<=0.0):
                        if (feature[29]<=0.0):
                            if (feature[28]<=0.0):
                                bin_num[1] = 32
                            else:
                                bin_num[1] = 33
                        else:
                            if (feature[18]<=0.0):
                                bin_num[1] = 34
                            else:
                                bin_num[1] = 35
                    else:
                        if (feature[15]<=0.0):
                            if (feature[35]<=0.0):
                                bin_num[1] = 36
                            else:
                                bin_num[1] = 37
                        else:
                            if (feature[11]<=0.0):
                                bin_num[1] = 38
                            else:
                                bin_num[1] = 39
                else:
                    if (feature[2]<=4.0):
                        if (feature[21]<=0.0):
                            if (feature[23]<=0.0):
                                bin_num[1] = 40
                            else:
                                bin_num[1] = 41
                        else:
                            if (feature[12]<=3.0):
                                bin_num[1] = 42
                            else:
                                bin_num[1] = 43
                    else:
                        if (feature[35]<=0.0):
                            if (feature[18]<=0.0):
                                bin_num[1] = 44
                            else:
                                bin_num[1] = 45
                        else:
                            if (feature[20]<=0.0):
                                bin_num[1] = 46
                            else:
                                bin_num[1] = 47
            else:
                if (feature[21]<=0.0):
                    if (feature[5]<=15.0):
                        if (feature[19]<=0.0):
                            if (feature[12]<=3.0):
                                bin_num[1] = 48
                            else:
                                bin_num[1] = 49
                        else:
                            if (feature[8]<=36.0):
                                bin_num[1] = 50
                            else:
                                bin_num[1] = 51
                    else:
                        if (feature[8]<=36.0):
                            if (feature[2]<=4.0):
                                bin_num[1] = 52
                            else:
                                bin_num[1] = 53
                        else:
                            if (feature[36]<=0.0):
                                bin_num[1] = 54
                            else:
                                bin_num[1] = 55
                else:
                    if (feature[17]<=0.0):
                        if (feature[26]<=0.0):
                            if (feature[18]<=0.0):
                                bin_num[1] = 56
                            else:
                                bin_num[1] = 57
                        else:
                            if (feature[19]<=0.0):
                                bin_num[1] = 58
                            else:
                                bin_num[1] = 59
                    else:
                        if (feature[2]<=4.0):
                            if (feature[10]<=1.0):
                                bin_num[1] = 60
                            else:
                                bin_num[1] = 61
                        else:
                            if (feature[30]<=0.0):
                                bin_num[1] = 62
                            else:
                                bin_num[1] = 63
    else:
        if (feature[5]<=15.0):
            if (feature[22]<=0.0):
                if (feature[25]<=0.0):
                    if (feature[20]<=0.0):
                        if (feature[24]<=0.0):
                            if (feature[35]<=0.0):
                                bin_num[1] = 64
                            else:
                                bin_num[1] = 65
                        else:
                            if (feature[12]<=3.0):
                                bin_num[1] = 66
                            else:
                                bin_num[1] = 67
                    else:
                        if (feature[27]<=0.0):
                            if (feature[24]<=0.0):
                                bin_num[1] = 68
                            else:
                                bin_num[1] = 69
                        else:
                            if (feature[38]<=0.0):
                                bin_num[1] = 70
                            else:
                                bin_num[1] = 71
                else:
                    if (feature[17]<=0.0):
                        if (feature[1]<=2.0):
                            if (feature[4]<=1912.0):
                                bin_num[1] = 72
                            else:
                                bin_num[1] = 73
                        else:
                            if (feature[9]<=0.0):
                                bin_num[1] = 74
                            else:
                                bin_num[1] = 75
                    else:
                        if (feature[27]<=0.0):
                            if (feature[23]<=0.0):
                                bin_num[1] = 76
                            else:
                                bin_num[1] = 77
                        else:
                            if (feature[1]<=2.0):
                                bin_num[1] = 78
                            else:
                                bin_num[1] = 79
            else:
                if (feature[34]<=0.0):
                    if (feature[8]<=36.0):
                        if (feature[38]<=0.0):
                            if (feature[12]<=3.0):
                                bin_num[1] = 80
                            else:
                                bin_num[1] = 81
                        else:
                            if (feature[20]<=0.0):
                                bin_num[1] = 82
                            else:
                                bin_num[1] = 83
                    else:
                        if (feature[12]<=3.0):
                            if (feature[24]<=0.0):
                                bin_num[1] = 84
                            else:
                                bin_num[1] = 85
                        else:
                            if (feature[2]<=4.0):
                                bin_num[1] = 86
                            else:
                                bin_num[1] = 87
                else:
                    if (feature[1]<=2.0):
                        if (feature[8]<=36.0):
                            if (feature[10]<=1.0):
                                bin_num[1] = 88
                            else:
                                bin_num[1] = 89
                        else:
                            if (feature[30]<=0.0):
                                bin_num[1] = 90
                            else:
                                bin_num[1] = 91
                    else:
                        if (feature[18]<=0.0):
                            if (feature[25]<=0.0):
                                bin_num[1] = 92
                            else:
                                bin_num[1] = 93
                        else:
                            if (feature[3]<=3.0):
                                bin_num[1] = 94
                            else:
                                bin_num[1] = 95
        else:
            if (feature[35]<=0.0):
                if (feature[21]<=0.0):
                    if (feature[2]<=4.0):
                        if (feature[29]<=0.0):
                            if (feature[1]<=2.0):
                                bin_num[1] = 96
                            else:
                                bin_num[1] = 97
                        else:
                            if (feature[22]<=0.0):
                                bin_num[1] = 98
                            else:
                                bin_num[1] = 99
                    else:
                        if (feature[10]<=1.0):
                            if (feature[22]<=0.0):
                                bin_num[1] = 100
                            else:
                                bin_num[1] = 101
                        else:
                            if (feature[24]<=0.0):
                                bin_num[1] = 102
                            else:
                                bin_num[1] = 103
                else:
                    if (feature[18]<=0.0):
                        if (feature[27]<=0.0):
                            if (feature[37]<=0.0):
                                bin_num[1] = 104
                            else:
                                bin_num[1] = 105
                        else:
                            if (feature[12]<=3.0):
                                bin_num[1] = 106
                            else:
                                bin_num[1] = 107
                    else:
                        if (feature[17]<=0.0):
                            if (feature[31]<=0.0):
                                bin_num[1] = 108
                            else:
                                bin_num[1] = 109
                        else:
                            if (feature[4]<=1912.0):
                                bin_num[1] = 110
                            else:
                                bin_num[1] = 111
            else:
                if (feature[2]<=4.0):
                    if (feature[11]<=0.0):
                        if (feature[21]<=0.0):
                            if (feature[18]<=0.0):
                                bin_num[1] = 112
                            else:
                                bin_num[1] = 113
                        else:
                            if (feature[16]<=0.0):
                                bin_num[1] = 114
                            else:
                                bin_num[1] = 115
                    else:
                        if (feature[4]<=1912.0):
                            if (feature[31]<=0.0):
                                bin_num[1] = 116
                            else:
                                bin_num[1] = 117
                        else:
                            if (feature[17]<=0.0):
                                bin_num[1] = 118
                            else:
                                bin_num[1] = 119
                else:
                    if (feature[10]<=1.0):
                        if (feature[23]<=0.0):
                            if (feature[14]<=0.0):
                                bin_num[1] = 120
                            else:
                                bin_num[1] = 121
                        else:
                            if (feature[32]<=0.0):
                                bin_num[1] = 122
                            else:
                                bin_num[1] = 123
                    else:
                        if (feature[1]<=2.0):
                            if (feature[3]<=3.0):
                                bin_num[1] = 124
                            else:
                                bin_num[1] = 125
                        else:
                            if (feature[8]<=36.0):
                                bin_num[1] = 126
                            else:
                                bin_num[1] = 127
    # Tree 0
    if (feature[0]<=0.0):
        if (feature[10]<=1.0):
            if (feature[12]<=3.0):
                if (feature[19]<=0.0):
                    if (feature[18]<=0.0):
                        if (feature[13]<=0.0):
                            if (feature[35]<=0.0):
                                bin_num[0] = 0
                            else:
                                bin_num[0] = 1
                        else:
                            if (feature[8]<=34.0):
                                bin_num[0] = 2
                            else:
                                bin_num[0] = 3
                    else:
                        if (feature[35]<=0.0):
                            if (feature[20]<=0.0):
                                bin_num[0] = 4
                            else:
                                bin_num[0] = 5
                        else:
                            if (feature[17]<=0.0):
                                bin_num[0] = 6
                            else:
                                bin_num[0] = 7
                else:
                    if (feature[8]<=34.0):
                        if (feature[2]<=4.0):
                            if (feature[7]<=7.0):
                                bin_num[0] = 8
                            else:
                                bin_num[0] = 9
                        else:
                            if (feature[13]<=0.0):
                                bin_num[0] = 10
                            else:
                                bin_num[0] = 11
                    else:
                        if (feature[35]<=0.0):
                            if (feature[5]<=15.0):
                                bin_num[0] = 12
                            else:
                                bin_num[0] = 13
                        else:
                            if (feature[6]<=2.0):
                                bin_num[0] = 14
                            else:
                                bin_num[0] = 15
            else:
                if (feature[6]<=2.0):
                    if (feature[35]<=0.0):
                        if (feature[23]<=0.0):
                            if (feature[2]<=4.0):
                                bin_num[0] = 16
                            else:
                                bin_num[0] = 17
                        else:
                            if (feature[19]<=0.0):
                                bin_num[0] = 18
                            else:
                                bin_num[0] = 19
                    else:
                        if (feature[18]<=0.0):
                            if (feature[11]<=0.0):
                                bin_num[0] = 20
                            else:
                                bin_num[0] = 21
                        else:
                            if (feature[17]<=0.0):
                                bin_num[0] = 22
                            else:
                                bin_num[0] = 23
                else:
                    if (feature[5]<=15.0):
                        if (feature[18]<=0.0):
                            if (feature[36]<=0.0):
                                bin_num[0] = 24
                            else:
                                bin_num[0] = 25
                        else:
                            if (feature[3]<=2.0):
                                bin_num[0] = 26
                            else:
                                bin_num[0] = 27
                    else:
                        if (feature[7]<=7.0):
                            if (feature[8]<=34.0):
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
                if (feature[12]<=3.0):
                    if (feature[20]<=0.0):
                        if (feature[28]<=0.0):
                            if (feature[19]<=0.0):
                                bin_num[0] = 32
                            else:
                                bin_num[0] = 33
                        else:
                            if (feature[16]<=0.0):
                                bin_num[0] = 34
                            else:
                                bin_num[0] = 35
                    else:
                        if (feature[35]<=0.0):
                            if (feature[34]<=0.0):
                                bin_num[0] = 36
                            else:
                                bin_num[0] = 37
                        else:
                            if (feature[17]<=0.0):
                                bin_num[0] = 38
                            else:
                                bin_num[0] = 39
                else:
                    if (feature[6]<=2.0):
                        if (feature[27]<=0.0):
                            if (feature[1]<=2.0):
                                bin_num[0] = 40
                            else:
                                bin_num[0] = 41
                        else:
                            bin_num[0] = 42
                    else:
                        if (feature[27]<=0.0):
                            if (feature[1]<=2.0):
                                bin_num[0] = 43
                            else:
                                bin_num[0] = 44
                        else:
                            if (feature[25]<=0.0):
                                bin_num[0] = 45
                            else:
                                bin_num[0] = 46
            else:
                if (feature[7]<=7.0):
                    if (feature[2]<=4.0):
                        if (feature[21]<=0.0):
                            if (feature[25]<=0.0):
                                bin_num[0] = 47
                            else:
                                bin_num[0] = 48
                        else:
                            if (feature[29]<=0.0):
                                bin_num[0] = 49
                            else:
                                bin_num[0] = 50
                    else:
                        if (feature[20]<=0.0):
                            if (feature[28]<=0.0):
                                bin_num[0] = 51
                            else:
                                bin_num[0] = 52
                        else:
                            if (feature[12]<=3.0):
                                bin_num[0] = 53
                            else:
                                bin_num[0] = 54
                else:
                    if (feature[12]<=3.0):
                        if (feature[19]<=0.0):
                            if (feature[22]<=0.0):
                                bin_num[0] = 55
                            else:
                                bin_num[0] = 56
                        else:
                            if (feature[21]<=0.0):
                                bin_num[0] = 57
                            else:
                                bin_num[0] = 58
                    else:
                        if (feature[22]<=0.0):
                            if (feature[29]<=0.0):
                                bin_num[0] = 59
                            else:
                                bin_num[0] = 60
                        else:
                            if (feature[2]<=4.0):
                                bin_num[0] = 61
                            else:
                                bin_num[0] = 62
    else:
        if (feature[5]<=15.0):
            if (feature[12]<=3.0):
                if (feature[6]<=2.0):
                    if (feature[24]<=0.0):
                        if (feature[18]<=0.0):
                            if (feature[27]<=0.0):
                                bin_num[0] = 63
                            else:
                                bin_num[0] = 64
                        else:
                            if (feature[36]<=0.0):
                                bin_num[0] = 65
                            else:
                                bin_num[0] = 66
                    else:
                        if (feature[38]<=0.0):
                            if (feature[9]<=0.0):
                                bin_num[0] = 67
                            else:
                                bin_num[0] = 68
                        else:
                            if (feature[11]<=0.0):
                                bin_num[0] = 69
                            else:
                                bin_num[0] = 70
                else:
                    if (feature[3]<=2.0):
                        if (feature[10]<=1.0):
                            if (feature[28]<=0.0):
                                bin_num[0] = 71
                            else:
                                bin_num[0] = 72
                        else:
                            if (feature[28]<=0.0):
                                bin_num[0] = 73
                            else:
                                bin_num[0] = 74
                    else:
                        if (feature[28]<=0.0):
                            if (feature[21]<=0.0):
                                bin_num[0] = 75
                            else:
                                bin_num[0] = 76
                        else:
                            if (feature[23]<=0.0):
                                bin_num[0] = 77
                            else:
                                bin_num[0] = 78
            else:
                if (feature[10]<=1.0):
                    if (feature[6]<=2.0):
                        if (feature[20]<=0.0):
                            if (feature[22]<=0.0):
                                bin_num[0] = 79
                            else:
                                bin_num[0] = 80
                        else:
                            if (feature[8]<=34.0):
                                bin_num[0] = 81
                            else:
                                bin_num[0] = 82
                    else:
                        if (feature[25]<=0.0):
                            if (feature[37]<=0.0):
                                bin_num[0] = 83
                            else:
                                bin_num[0] = 84
                        else:
                            if (feature[21]<=0.0):
                                bin_num[0] = 85
                            else:
                                bin_num[0] = 86
                else:
                    if (feature[24]<=0.0):
                        if (feature[27]<=0.0):
                            if (feature[20]<=0.0):
                                bin_num[0] = 87
                            else:
                                bin_num[0] = 88
                        else:
                            if (feature[8]<=34.0):
                                bin_num[0] = 89
                            else:
                                bin_num[0] = 90
                    else:
                        if (feature[34]<=0.0):
                            if (feature[1]<=2.0):
                                bin_num[0] = 91
                            else:
                                bin_num[0] = 92
                        else:
                            if (feature[20]<=0.0):
                                bin_num[0] = 93
                            else:
                                bin_num[0] = 94
        else:
            if (feature[10]<=1.0):
                if (feature[2]<=4.0):
                    if (feature[19]<=0.0):
                        if (feature[21]<=0.0):
                            if (feature[7]<=7.0):
                                bin_num[0] = 95
                            else:
                                bin_num[0] = 96
                        else:
                            if (feature[38]<=0.0):
                                bin_num[0] = 97
                            else:
                                bin_num[0] = 98
                    else:
                        if (feature[22]<=0.0):
                            if (feature[12]<=3.0):
                                bin_num[0] = 99
                            else:
                                bin_num[0] = 100
                        else:
                            if (feature[32]<=0.0):
                                bin_num[0] = 101
                            else:
                                bin_num[0] = 102
                else:
                    if (feature[28]<=0.0):
                        if (feature[19]<=0.0):
                            if (feature[22]<=0.0):
                                bin_num[0] = 103
                            else:
                                bin_num[0] = 104
                        else:
                            if (feature[12]<=3.0):
                                bin_num[0] = 105
                            else:
                                bin_num[0] = 106
                    else:
                        if (feature[12]<=3.0):
                            if (feature[6]<=2.0):
                                bin_num[0] = 107
                            else:
                                bin_num[0] = 108
                        else:
                            if (feature[20]<=0.0):
                                bin_num[0] = 109
                            else:
                                bin_num[0] = 110
            else:
                if (feature[2]<=4.0):
                    if (feature[21]<=0.0):
                        if (feature[29]<=0.0):
                            if (feature[35]<=0.0):
                                bin_num[0] = 111
                            else:
                                bin_num[0] = 112
                        else:
                            if (feature[9]<=0.0):
                                bin_num[0] = 113
                            else:
                                bin_num[0] = 114
                    else:
                        if (feature[12]<=3.0):
                            if (feature[22]<=0.0):
                                bin_num[0] = 115
                            else:
                                bin_num[0] = 116
                        else:
                            if (feature[38]<=0.0):
                                bin_num[0] = 117
                            else:
                                bin_num[0] = 118
                else:
                    if (feature[12]<=3.0):
                        if (feature[35]<=0.0):
                            if (feature[25]<=0.0):
                                bin_num[0] = 119
                            else:
                                bin_num[0] = 120
                        else:
                            if (feature[23]<=0.0):
                                bin_num[0] = 121
                            else:
                                bin_num[0] = 122
                    else:
                        if (feature[24]<=0.0):
                            if (feature[21]<=0.0):
                                bin_num[0] = 123
                            else:
                                bin_num[0] = 124
                        else:
                            if (feature[31]<=0.0):
                                bin_num[0] = 125
                            else:
                                bin_num[0] = 126
    # Tree 1
    if (feature[6]<=2.0):
        if (feature[7]<=7.0):
            if (feature[13]<=0.0):
                if (feature[35]<=0.0):
                    if (feature[21]<=0.0):
                        if (feature[0]<=0.0):
                            if (feature[8]<=35.0):
                                bin_num[1] = 0
                            else:
                                bin_num[1] = 1
                        else:
                            if (feature[5]<=16.0):
                                bin_num[1] = 2
                            else:
                                bin_num[1] = 3
                    else:
                        if (feature[5]<=16.0):
                            if (feature[17]<=0.0):
                                bin_num[1] = 4
                            else:
                                bin_num[1] = 5
                        else:
                            if (feature[2]<=4.0):
                                bin_num[1] = 6
                            else:
                                bin_num[1] = 7
                else:
                    if (feature[2]<=4.0):
                        if (feature[34]<=0.0):
                            if (feature[0]<=0.0):
                                bin_num[1] = 8
                            else:
                                bin_num[1] = 9
                        else:
                            if (feature[3]<=2.0):
                                bin_num[1] = 10
                            else:
                                bin_num[1] = 11
                    else:
                        if (feature[37]<=0.0):
                            if (feature[26]<=0.0):
                                bin_num[1] = 12
                            else:
                                bin_num[1] = 13
                        else:
                            if (feature[31]<=0.0):
                                bin_num[1] = 14
                            else:
                                bin_num[1] = 15
            else:
                if (feature[23]<=0.0):
                    if (feature[8]<=35.0):
                        if (feature[2]<=4.0):
                            if (feature[21]<=0.0):
                                bin_num[1] = 16
                            else:
                                bin_num[1] = 17
                        else:
                            if (feature[4]<=1941.0):
                                bin_num[1] = 18
                            else:
                                bin_num[1] = 19
                    else:
                        if (feature[19]<=0.0):
                            if (feature[11]<=0.0):
                                bin_num[1] = 20
                            else:
                                bin_num[1] = 21
                        else:
                            if (feature[33]<=0.0):
                                bin_num[1] = 22
                            else:
                                bin_num[1] = 23
                else:
                    if (feature[25]<=0.0):
                        if (feature[18]<=0.0):
                            if (feature[28]<=0.0):
                                bin_num[1] = 24
                            else:
                                bin_num[1] = 25
                        else:
                            if (feature[2]<=4.0):
                                bin_num[1] = 26
                            else:
                                bin_num[1] = 27
                    else:
                        if (feature[35]<=0.0):
                            if (feature[21]<=0.0):
                                bin_num[1] = 28
                            else:
                                bin_num[1] = 29
                        else:
                            if (feature[12]<=3.0):
                                bin_num[1] = 30
                            else:
                                bin_num[1] = 31
        else:
            if (feature[4]<=1941.0):
                if (feature[19]<=0.0):
                    if (feature[20]<=0.0):
                        if (feature[32]<=0.0):
                            if (feature[13]<=0.0):
                                bin_num[1] = 32
                            else:
                                bin_num[1] = 33
                        else:
                            if (feature[36]<=0.0):
                                bin_num[1] = 34
                            else:
                                bin_num[1] = 35
                    else:
                        if (feature[15]<=0.0):
                            if (feature[35]<=0.0):
                                bin_num[1] = 36
                            else:
                                bin_num[1] = 37
                        else:
                            if (feature[28]<=0.0):
                                bin_num[1] = 38
                            else:
                                bin_num[1] = 39
                else:
                    if (feature[35]<=0.0):
                        if (feature[2]<=4.0):
                            if (feature[21]<=0.0):
                                bin_num[1] = 40
                            else:
                                bin_num[1] = 41
                        else:
                            if (feature[38]<=0.0):
                                bin_num[1] = 42
                            else:
                                bin_num[1] = 43
                    else:
                        if (feature[21]<=0.0):
                            if (feature[1]<=2.0):
                                bin_num[1] = 44
                            else:
                                bin_num[1] = 45
                        else:
                            if (feature[9]<=0.0):
                                bin_num[1] = 46
                            else:
                                bin_num[1] = 47
            else:
                if (feature[21]<=0.0):
                    if (feature[5]<=16.0):
                        if (feature[19]<=0.0):
                            if (feature[12]<=3.0):
                                bin_num[1] = 48
                            else:
                                bin_num[1] = 49
                        else:
                            if (feature[13]<=0.0):
                                bin_num[1] = 50
                            else:
                                bin_num[1] = 51
                    else:
                        if (feature[8]<=35.0):
                            if (feature[2]<=4.0):
                                bin_num[1] = 52
                            else:
                                bin_num[1] = 53
                        else:
                            if (feature[36]<=0.0):
                                bin_num[1] = 54
                            else:
                                bin_num[1] = 55
                else:
                    if (feature[17]<=0.0):
                        if (feature[26]<=0.0):
                            if (feature[18]<=0.0):
                                bin_num[1] = 56
                            else:
                                bin_num[1] = 57
                        else:
                            if (feature[29]<=0.0):
                                bin_num[1] = 58
                            else:
                                bin_num[1] = 59
                    else:
                        if (feature[2]<=4.0):
                            if (feature[10]<=1.0):
                                bin_num[1] = 60
                            else:
                                bin_num[1] = 61
                        else:
                            if (feature[30]<=0.0):
                                bin_num[1] = 62
                            else:
                                bin_num[1] = 63
    else:
        if (feature[5]<=16.0):
            if (feature[25]<=0.0):
                if (feature[22]<=0.0):
                    if (feature[8]<=35.0):
                        if (feature[35]<=0.0):
                            if (feature[29]<=0.0):
                                bin_num[1] = 64
                            else:
                                bin_num[1] = 65
                        else:
                            if (feature[31]<=0.0):
                                bin_num[1] = 66
                            else:
                                bin_num[1] = 67
                    else:
                        if (feature[34]<=0.0):
                            if (feature[4]<=1941.0):
                                bin_num[1] = 68
                            else:
                                bin_num[1] = 69
                        else:
                            if (feature[31]<=0.0):
                                bin_num[1] = 70
                            else:
                                bin_num[1] = 71
                else:
                    if (feature[19]<=0.0):
                        if (feature[2]<=4.0):
                            if (feature[21]<=0.0):
                                bin_num[1] = 72
                            else:
                                bin_num[1] = 73
                        else:
                            if (feature[12]<=3.0):
                                bin_num[1] = 74
                            else:
                                bin_num[1] = 75
                    else:
                        if (feature[9]<=0.0):
                            if (feature[0]<=0.0):
                                bin_num[1] = 76
                            else:
                                bin_num[1] = 77
                        else:
                            if (feature[21]<=0.0):
                                bin_num[1] = 78
                            else:
                                bin_num[1] = 79
            else:
                if (feature[23]<=0.0):
                    if (feature[3]<=2.0):
                        if (feature[9]<=0.0):
                            if (feature[37]<=0.0):
                                bin_num[1] = 80
                            else:
                                bin_num[1] = 81
                        else:
                            if (feature[21]<=0.0):
                                bin_num[1] = 82
                            else:
                                bin_num[1] = 83
                    else:
                        if (feature[12]<=3.0):
                            if (feature[17]<=0.0):
                                bin_num[1] = 84
                            else:
                                bin_num[1] = 85
                        else:
                            if (feature[29]<=0.0):
                                bin_num[1] = 86
                            else:
                                bin_num[1] = 87
                else:
                    if (feature[29]<=0.0):
                        if (feature[21]<=0.0):
                            if (feature[27]<=0.0):
                                bin_num[1] = 88
                            else:
                                bin_num[1] = 89
                        else:
                            if (feature[7]<=7.0):
                                bin_num[1] = 90
                            else:
                                bin_num[1] = 91
                    else:
                        if (feature[10]<=1.0):
                            if (feature[7]<=7.0):
                                bin_num[1] = 92
                            else:
                                bin_num[1] = 93
                        else:
                            if (feature[38]<=0.0):
                                bin_num[1] = 94
                            else:
                                bin_num[1] = 95
        else:
            if (feature[12]<=3.0):
                if (feature[35]<=0.0):
                    if (feature[21]<=0.0):
                        if (feature[29]<=0.0):
                            if (feature[1]<=2.0):
                                bin_num[1] = 96
                            else:
                                bin_num[1] = 97
                        else:
                            if (feature[2]<=4.0):
                                bin_num[1] = 98
                            else:
                                bin_num[1] = 99
                    else:
                        if (feature[18]<=0.0):
                            if (feature[24]<=0.0):
                                bin_num[1] = 100
                            else:
                                bin_num[1] = 101
                        else:
                            if (feature[17]<=0.0):
                                bin_num[1] = 102
                            else:
                                bin_num[1] = 103
                else:
                    if (feature[3]<=2.0):
                        if (feature[7]<=7.0):
                            if (feature[13]<=0.0):
                                bin_num[1] = 104
                            else:
                                bin_num[1] = 105
                        else:
                            if (feature[10]<=1.0):
                                bin_num[1] = 106
                            else:
                                bin_num[1] = 107
                    else:
                        if (feature[25]<=0.0):
                            if (feature[15]<=0.0):
                                bin_num[1] = 108
                            else:
                                bin_num[1] = 109
                        else:
                            if (feature[33]<=0.0):
                                bin_num[1] = 110
                            else:
                                bin_num[1] = 111
            else:
                if (feature[18]<=0.0):
                    if (feature[22]<=0.0):
                        if (feature[4]<=1941.0):
                            if (feature[27]<=0.0):
                                bin_num[1] = 112
                            else:
                                bin_num[1] = 113
                        else:
                            if (feature[37]<=0.0):
                                bin_num[1] = 114
                            else:
                                bin_num[1] = 115
                    else:
                        if (feature[21]<=0.0):
                            if (feature[2]<=4.0):
                                bin_num[1] = 116
                            else:
                                bin_num[1] = 117
                        else:
                            if (feature[14]<=0.0):
                                bin_num[1] = 118
                            else:
                                bin_num[1] = 119
                else:
                    if (feature[35]<=0.0):
                        if (feature[17]<=0.0):
                            if (feature[37]<=0.0):
                                bin_num[1] = 120
                            else:
                                bin_num[1] = 121
                        else:
                            if (feature[4]<=1941.0):
                                bin_num[1] = 122
                            else:
                                bin_num[1] = 123
                    else:
                        if (feature[10]<=1.0):
                            if (feature[1]<=2.0):
                                bin_num[1] = 124
                            else:
                                bin_num[1] = 125
                        else:
                            if (feature[8]<=35.0):
                                bin_num[1] = 126
                            else:
                                bin_num[1] = 127
    # Tree 0
    if (feature[0]<=0.0):
        if (feature[10]<=1.0):
            if (feature[12]<=3.0):
                if (feature[19]<=0.0):
                    if (feature[18]<=0.0):
                        if (feature[13]<=0.0):
                            if (feature[35]<=0.0):
                                bin_num[0] = 0
                            else:
                                bin_num[0] = 1
                        else:
                            if (feature[8]<=34.0):
                                bin_num[0] = 2
                            else:
                                bin_num[0] = 3
                    else:
                        if (feature[35]<=0.0):
                            if (feature[20]<=0.0):
                                bin_num[0] = 4
                            else:
                                bin_num[0] = 5
                        else:
                            if (feature[17]<=0.0):
                                bin_num[0] = 6
                            else:
                                bin_num[0] = 7
                else:
                    if (feature[8]<=34.0):
                        if (feature[2]<=4.0):
                            if (feature[7]<=7.0):
                                bin_num[0] = 8
                            else:
                                bin_num[0] = 9
                        else:
                            if (feature[13]<=0.0):
                                bin_num[0] = 10
                            else:
                                bin_num[0] = 11
                    else:
                        if (feature[35]<=0.0):
                            if (feature[5]<=15.0):
                                bin_num[0] = 12
                            else:
                                bin_num[0] = 13
                        else:
                            if (feature[6]<=2.0):
                                bin_num[0] = 14
                            else:
                                bin_num[0] = 15
            else:
                if (feature[6]<=2.0):
                    if (feature[35]<=0.0):
                        if (feature[23]<=0.0):
                            if (feature[2]<=4.0):
                                bin_num[0] = 16
                            else:
                                bin_num[0] = 17
                        else:
                            if (feature[19]<=0.0):
                                bin_num[0] = 18
                            else:
                                bin_num[0] = 19
                    else:
                        if (feature[18]<=0.0):
                            if (feature[11]<=0.0):
                                bin_num[0] = 20
                            else:
                                bin_num[0] = 21
                        else:
                            if (feature[17]<=0.0):
                                bin_num[0] = 22
                            else:
                                bin_num[0] = 23
                else:
                    if (feature[5]<=15.0):
                        if (feature[18]<=0.0):
                            if (feature[36]<=0.0):
                                bin_num[0] = 24
                            else:
                                bin_num[0] = 25
                        else:
                            if (feature[3]<=2.0):
                                bin_num[0] = 26
                            else:
                                bin_num[0] = 27
                    else:
                        if (feature[7]<=7.0):
                            if (feature[8]<=34.0):
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
                if (feature[12]<=3.0):
                    if (feature[20]<=0.0):
                        if (feature[28]<=0.0):
                            if (feature[19]<=0.0):
                                bin_num[0] = 32
                            else:
                                bin_num[0] = 33
                        else:
                            if (feature[16]<=0.0):
                                bin_num[0] = 34
                            else:
                                bin_num[0] = 35
                    else:
                        if (feature[35]<=0.0):
                            if (feature[34]<=0.0):
                                bin_num[0] = 36
                            else:
                                bin_num[0] = 37
                        else:
                            if (feature[17]<=0.0):
                                bin_num[0] = 38
                            else:
                                bin_num[0] = 39
                else:
                    if (feature[6]<=2.0):
                        if (feature[27]<=0.0):
                            if (feature[1]<=2.0):
                                bin_num[0] = 40
                            else:
                                bin_num[0] = 41
                        else:
                            bin_num[0] = 42
                    else:
                        if (feature[27]<=0.0):
                            if (feature[1]<=2.0):
                                bin_num[0] = 43
                            else:
                                bin_num[0] = 44
                        else:
                            if (feature[25]<=0.0):
                                bin_num[0] = 45
                            else:
                                bin_num[0] = 46
            else:
                if (feature[7]<=7.0):
                    if (feature[2]<=4.0):
                        if (feature[21]<=0.0):
                            if (feature[25]<=0.0):
                                bin_num[0] = 47
                            else:
                                bin_num[0] = 48
                        else:
                            if (feature[29]<=0.0):
                                bin_num[0] = 49
                            else:
                                bin_num[0] = 50
                    else:
                        if (feature[20]<=0.0):
                            if (feature[28]<=0.0):
                                bin_num[0] = 51
                            else:
                                bin_num[0] = 52
                        else:
                            if (feature[12]<=3.0):
                                bin_num[0] = 53
                            else:
                                bin_num[0] = 54
                else:
                    if (feature[12]<=3.0):
                        if (feature[19]<=0.0):
                            if (feature[22]<=0.0):
                                bin_num[0] = 55
                            else:
                                bin_num[0] = 56
                        else:
                            if (feature[21]<=0.0):
                                bin_num[0] = 57
                            else:
                                bin_num[0] = 58
                    else:
                        if (feature[22]<=0.0):
                            if (feature[29]<=0.0):
                                bin_num[0] = 59
                            else:
                                bin_num[0] = 60
                        else:
                            if (feature[2]<=4.0):
                                bin_num[0] = 61
                            else:
                                bin_num[0] = 62
    else:
        if (feature[5]<=15.0):
            if (feature[12]<=3.0):
                if (feature[6]<=2.0):
                    if (feature[24]<=0.0):
                        if (feature[18]<=0.0):
                            if (feature[27]<=0.0):
                                bin_num[0] = 63
                            else:
                                bin_num[0] = 64
                        else:
                            if (feature[36]<=0.0):
                                bin_num[0] = 65
                            else:
                                bin_num[0] = 66
                    else:
                        if (feature[38]<=0.0):
                            if (feature[9]<=0.0):
                                bin_num[0] = 67
                            else:
                                bin_num[0] = 68
                        else:
                            if (feature[11]<=0.0):
                                bin_num[0] = 69
                            else:
                                bin_num[0] = 70
                else:
                    if (feature[3]<=2.0):
                        if (feature[10]<=1.0):
                            if (feature[28]<=0.0):
                                bin_num[0] = 71
                            else:
                                bin_num[0] = 72
                        else:
                            if (feature[28]<=0.0):
                                bin_num[0] = 73
                            else:
                                bin_num[0] = 74
                    else:
                        if (feature[28]<=0.0):
                            if (feature[21]<=0.0):
                                bin_num[0] = 75
                            else:
                                bin_num[0] = 76
                        else:
                            if (feature[23]<=0.0):
                                bin_num[0] = 77
                            else:
                                bin_num[0] = 78
            else:
                if (feature[10]<=1.0):
                    if (feature[6]<=2.0):
                        if (feature[20]<=0.0):
                            if (feature[22]<=0.0):
                                bin_num[0] = 79
                            else:
                                bin_num[0] = 80
                        else:
                            if (feature[8]<=34.0):
                                bin_num[0] = 81
                            else:
                                bin_num[0] = 82
                    else:
                        if (feature[25]<=0.0):
                            if (feature[37]<=0.0):
                                bin_num[0] = 83
                            else:
                                bin_num[0] = 84
                        else:
                            if (feature[21]<=0.0):
                                bin_num[0] = 85
                            else:
                                bin_num[0] = 86
                else:
                    if (feature[24]<=0.0):
                        if (feature[27]<=0.0):
                            if (feature[20]<=0.0):
                                bin_num[0] = 87
                            else:
                                bin_num[0] = 88
                        else:
                            if (feature[8]<=34.0):
                                bin_num[0] = 89
                            else:
                                bin_num[0] = 90
                    else:
                        if (feature[34]<=0.0):
                            if (feature[1]<=2.0):
                                bin_num[0] = 91
                            else:
                                bin_num[0] = 92
                        else:
                            if (feature[20]<=0.0):
                                bin_num[0] = 93
                            else:
                                bin_num[0] = 94
        else:
            if (feature[10]<=1.0):
                if (feature[2]<=4.0):
                    if (feature[19]<=0.0):
                        if (feature[21]<=0.0):
                            if (feature[7]<=7.0):
                                bin_num[0] = 95
                            else:
                                bin_num[0] = 96
                        else:
                            if (feature[38]<=0.0):
                                bin_num[0] = 97
                            else:
                                bin_num[0] = 98
                    else:
                        if (feature[22]<=0.0):
                            if (feature[12]<=3.0):
                                bin_num[0] = 99
                            else:
                                bin_num[0] = 100
                        else:
                            if (feature[32]<=0.0):
                                bin_num[0] = 101
                            else:
                                bin_num[0] = 102
                else:
                    if (feature[28]<=0.0):
                        if (feature[19]<=0.0):
                            if (feature[22]<=0.0):
                                bin_num[0] = 103
                            else:
                                bin_num[0] = 104
                        else:
                            if (feature[12]<=3.0):
                                bin_num[0] = 105
                            else:
                                bin_num[0] = 106
                    else:
                        if (feature[12]<=3.0):
                            if (feature[6]<=2.0):
                                bin_num[0] = 107
                            else:
                                bin_num[0] = 108
                        else:
                            if (feature[20]<=0.0):
                                bin_num[0] = 109
                            else:
                                bin_num[0] = 110
            else:
                if (feature[2]<=4.0):
                    if (feature[21]<=0.0):
                        if (feature[29]<=0.0):
                            if (feature[35]<=0.0):
                                bin_num[0] = 111
                            else:
                                bin_num[0] = 112
                        else:
                            if (feature[9]<=0.0):
                                bin_num[0] = 113
                            else:
                                bin_num[0] = 114
                    else:
                        if (feature[12]<=3.0):
                            if (feature[22]<=0.0):
                                bin_num[0] = 115
                            else:
                                bin_num[0] = 116
                        else:
                            if (feature[38]<=0.0):
                                bin_num[0] = 117
                            else:
                                bin_num[0] = 118
                else:
                    if (feature[12]<=3.0):
                        if (feature[35]<=0.0):
                            if (feature[25]<=0.0):
                                bin_num[0] = 119
                            else:
                                bin_num[0] = 120
                        else:
                            if (feature[23]<=0.0):
                                bin_num[0] = 121
                            else:
                                bin_num[0] = 122
                    else:
                        if (feature[24]<=0.0):
                            if (feature[21]<=0.0):
                                bin_num[0] = 123
                            else:
                                bin_num[0] = 124
                        else:
                            if (feature[31]<=0.0):
                                bin_num[0] = 125
                            else:
                                bin_num[0] = 126
    # Tree 1
    if (feature[6]<=2.0):
        if (feature[7]<=7.0):
            if (feature[13]<=0.0):
                if (feature[35]<=0.0):
                    if (feature[21]<=0.0):
                        if (feature[0]<=0.0):
                            if (feature[8]<=35.0):
                                bin_num[1] = 0
                            else:
                                bin_num[1] = 1
                        else:
                            if (feature[5]<=16.0):
                                bin_num[1] = 2
                            else:
                                bin_num[1] = 3
                    else:
                        if (feature[5]<=16.0):
                            if (feature[17]<=0.0):
                                bin_num[1] = 4
                            else:
                                bin_num[1] = 5
                        else:
                            if (feature[2]<=4.0):
                                bin_num[1] = 6
                            else:
                                bin_num[1] = 7
                else:
                    if (feature[2]<=4.0):
                        if (feature[34]<=0.0):
                            if (feature[0]<=0.0):
                                bin_num[1] = 8
                            else:
                                bin_num[1] = 9
                        else:
                            if (feature[3]<=2.0):
                                bin_num[1] = 10
                            else:
                                bin_num[1] = 11
                    else:
                        if (feature[37]<=0.0):
                            if (feature[26]<=0.0):
                                bin_num[1] = 12
                            else:
                                bin_num[1] = 13
                        else:
                            if (feature[31]<=0.0):
                                bin_num[1] = 14
                            else:
                                bin_num[1] = 15
            else:
                if (feature[23]<=0.0):
                    if (feature[8]<=35.0):
                        if (feature[2]<=4.0):
                            if (feature[21]<=0.0):
                                bin_num[1] = 16
                            else:
                                bin_num[1] = 17
                        else:
                            if (feature[4]<=1941.0):
                                bin_num[1] = 18
                            else:
                                bin_num[1] = 19
                    else:
                        if (feature[19]<=0.0):
                            if (feature[11]<=0.0):
                                bin_num[1] = 20
                            else:
                                bin_num[1] = 21
                        else:
                            if (feature[33]<=0.0):
                                bin_num[1] = 22
                            else:
                                bin_num[1] = 23
                else:
                    if (feature[25]<=0.0):
                        if (feature[18]<=0.0):
                            if (feature[28]<=0.0):
                                bin_num[1] = 24
                            else:
                                bin_num[1] = 25
                        else:
                            if (feature[2]<=4.0):
                                bin_num[1] = 26
                            else:
                                bin_num[1] = 27
                    else:
                        if (feature[35]<=0.0):
                            if (feature[21]<=0.0):
                                bin_num[1] = 28
                            else:
                                bin_num[1] = 29
                        else:
                            if (feature[12]<=3.0):
                                bin_num[1] = 30
                            else:
                                bin_num[1] = 31
        else:
            if (feature[4]<=1941.0):
                if (feature[19]<=0.0):
                    if (feature[20]<=0.0):
                        if (feature[32]<=0.0):
                            if (feature[13]<=0.0):
                                bin_num[1] = 32
                            else:
                                bin_num[1] = 33
                        else:
                            if (feature[36]<=0.0):
                                bin_num[1] = 34
                            else:
                                bin_num[1] = 35
                    else:
                        if (feature[15]<=0.0):
                            if (feature[35]<=0.0):
                                bin_num[1] = 36
                            else:
                                bin_num[1] = 37
                        else:
                            if (feature[28]<=0.0):
                                bin_num[1] = 38
                            else:
                                bin_num[1] = 39
                else:
                    if (feature[35]<=0.0):
                        if (feature[2]<=4.0):
                            if (feature[21]<=0.0):
                                bin_num[1] = 40
                            else:
                                bin_num[1] = 41
                        else:
                            if (feature[38]<=0.0):
                                bin_num[1] = 42
                            else:
                                bin_num[1] = 43
                    else:
                        if (feature[21]<=0.0):
                            if (feature[1]<=2.0):
                                bin_num[1] = 44
                            else:
                                bin_num[1] = 45
                        else:
                            if (feature[9]<=0.0):
                                bin_num[1] = 46
                            else:
                                bin_num[1] = 47
            else:
                if (feature[21]<=0.0):
                    if (feature[5]<=16.0):
                        if (feature[19]<=0.0):
                            if (feature[12]<=3.0):
                                bin_num[1] = 48
                            else:
                                bin_num[1] = 49
                        else:
                            if (feature[13]<=0.0):
                                bin_num[1] = 50
                            else:
                                bin_num[1] = 51
                    else:
                        if (feature[8]<=35.0):
                            if (feature[2]<=4.0):
                                bin_num[1] = 52
                            else:
                                bin_num[1] = 53
                        else:
                            if (feature[36]<=0.0):
                                bin_num[1] = 54
                            else:
                                bin_num[1] = 55
                else:
                    if (feature[17]<=0.0):
                        if (feature[26]<=0.0):
                            if (feature[18]<=0.0):
                                bin_num[1] = 56
                            else:
                                bin_num[1] = 57
                        else:
                            if (feature[29]<=0.0):
                                bin_num[1] = 58
                            else:
                                bin_num[1] = 59
                    else:
                        if (feature[2]<=4.0):
                            if (feature[10]<=1.0):
                                bin_num[1] = 60
                            else:
                                bin_num[1] = 61
                        else:
                            if (feature[30]<=0.0):
                                bin_num[1] = 62
                            else:
                                bin_num[1] = 63
    else:
        if (feature[5]<=16.0):
            if (feature[25]<=0.0):
                if (feature[22]<=0.0):
                    if (feature[8]<=35.0):
                        if (feature[35]<=0.0):
                            if (feature[29]<=0.0):
                                bin_num[1] = 64
                            else:
                                bin_num[1] = 65
                        else:
                            if (feature[31]<=0.0):
                                bin_num[1] = 66
                            else:
                                bin_num[1] = 67
                    else:
                        if (feature[34]<=0.0):
                            if (feature[4]<=1941.0):
                                bin_num[1] = 68
                            else:
                                bin_num[1] = 69
                        else:
                            if (feature[31]<=0.0):
                                bin_num[1] = 70
                            else:
                                bin_num[1] = 71
                else:
                    if (feature[19]<=0.0):
                        if (feature[2]<=4.0):
                            if (feature[21]<=0.0):
                                bin_num[1] = 72
                            else:
                                bin_num[1] = 73
                        else:
                            if (feature[12]<=3.0):
                                bin_num[1] = 74
                            else:
                                bin_num[1] = 75
                    else:
                        if (feature[9]<=0.0):
                            if (feature[0]<=0.0):
                                bin_num[1] = 76
                            else:
                                bin_num[1] = 77
                        else:
                            if (feature[21]<=0.0):
                                bin_num[1] = 78
                            else:
                                bin_num[1] = 79
            else:
                if (feature[23]<=0.0):
                    if (feature[3]<=2.0):
                        if (feature[9]<=0.0):
                            if (feature[37]<=0.0):
                                bin_num[1] = 80
                            else:
                                bin_num[1] = 81
                        else:
                            if (feature[21]<=0.0):
                                bin_num[1] = 82
                            else:
                                bin_num[1] = 83
                    else:
                        if (feature[12]<=3.0):
                            if (feature[17]<=0.0):
                                bin_num[1] = 84
                            else:
                                bin_num[1] = 85
                        else:
                            if (feature[29]<=0.0):
                                bin_num[1] = 86
                            else:
                                bin_num[1] = 87
                else:
                    if (feature[29]<=0.0):
                        if (feature[21]<=0.0):
                            if (feature[27]<=0.0):
                                bin_num[1] = 88
                            else:
                                bin_num[1] = 89
                        else:
                            if (feature[7]<=7.0):
                                bin_num[1] = 90
                            else:
                                bin_num[1] = 91
                    else:
                        if (feature[10]<=1.0):
                            if (feature[7]<=7.0):
                                bin_num[1] = 92
                            else:
                                bin_num[1] = 93
                        else:
                            if (feature[38]<=0.0):
                                bin_num[1] = 94
                            else:
                                bin_num[1] = 95
        else:
            if (feature[12]<=3.0):
                if (feature[35]<=0.0):
                    if (feature[21]<=0.0):
                        if (feature[29]<=0.0):
                            if (feature[1]<=2.0):
                                bin_num[1] = 96
                            else:
                                bin_num[1] = 97
                        else:
                            if (feature[2]<=4.0):
                                bin_num[1] = 98
                            else:
                                bin_num[1] = 99
                    else:
                        if (feature[18]<=0.0):
                            if (feature[24]<=0.0):
                                bin_num[1] = 100
                            else:
                                bin_num[1] = 101
                        else:
                            if (feature[17]<=0.0):
                                bin_num[1] = 102
                            else:
                                bin_num[1] = 103
                else:
                    if (feature[3]<=2.0):
                        if (feature[7]<=7.0):
                            if (feature[13]<=0.0):
                                bin_num[1] = 104
                            else:
                                bin_num[1] = 105
                        else:
                            if (feature[10]<=1.0):
                                bin_num[1] = 106
                            else:
                                bin_num[1] = 107
                    else:
                        if (feature[25]<=0.0):
                            if (feature[15]<=0.0):
                                bin_num[1] = 108
                            else:
                                bin_num[1] = 109
                        else:
                            if (feature[33]<=0.0):
                                bin_num[1] = 110
                            else:
                                bin_num[1] = 111
            else:
                if (feature[18]<=0.0):
                    if (feature[22]<=0.0):
                        if (feature[4]<=1941.0):
                            if (feature[27]<=0.0):
                                bin_num[1] = 112
                            else:
                                bin_num[1] = 113
                        else:
                            if (feature[37]<=0.0):
                                bin_num[1] = 114
                            else:
                                bin_num[1] = 115
                    else:
                        if (feature[21]<=0.0):
                            if (feature[2]<=4.0):
                                bin_num[1] = 116
                            else:
                                bin_num[1] = 117
                        else:
                            if (feature[14]<=0.0):
                                bin_num[1] = 118
                            else:
                                bin_num[1] = 119
                else:
                    if (feature[35]<=0.0):
                        if (feature[17]<=0.0):
                            if (feature[37]<=0.0):
                                bin_num[1] = 120
                            else:
                                bin_num[1] = 121
                        else:
                            if (feature[4]<=1941.0):
                                bin_num[1] = 122
                            else:
                                bin_num[1] = 123
                    else:
                        if (feature[10]<=1.0):
                            if (feature[1]<=2.0):
                                bin_num[1] = 124
                            else:
                                bin_num[1] = 125
                        else:
                            if (feature[8]<=35.0):
                                bin_num[1] = 126
                            else:
                                bin_num[1] = 127
    # Tree 0
    if (feature[0]<=0.0):
        if (feature[10]<=1.0):
            if (feature[12]<=3.0):
                if (feature[19]<=0.0):
                    if (feature[18]<=0.0):
                        if (feature[13]<=0.0):
                            if (feature[35]<=0.0):
                                bin_num[0] = 0
                            else:
                                bin_num[0] = 1
                        else:
                            if (feature[8]<=34.0):
                                bin_num[0] = 2
                            else:
                                bin_num[0] = 3
                    else:
                        if (feature[35]<=0.0):
                            if (feature[20]<=0.0):
                                bin_num[0] = 4
                            else:
                                bin_num[0] = 5
                        else:
                            if (feature[17]<=0.0):
                                bin_num[0] = 6
                            else:
                                bin_num[0] = 7
                else:
                    if (feature[8]<=34.0):
                        if (feature[2]<=4.0):
                            if (feature[7]<=7.0):
                                bin_num[0] = 8
                            else:
                                bin_num[0] = 9
                        else:
                            if (feature[13]<=0.0):
                                bin_num[0] = 10
                            else:
                                bin_num[0] = 11
                    else:
                        if (feature[35]<=0.0):
                            if (feature[5]<=15.0):
                                bin_num[0] = 12
                            else:
                                bin_num[0] = 13
                        else:
                            if (feature[6]<=2.0):
                                bin_num[0] = 14
                            else:
                                bin_num[0] = 15
            else:
                if (feature[6]<=2.0):
                    if (feature[35]<=0.0):
                        if (feature[23]<=0.0):
                            if (feature[2]<=4.0):
                                bin_num[0] = 16
                            else:
                                bin_num[0] = 17
                        else:
                            if (feature[19]<=0.0):
                                bin_num[0] = 18
                            else:
                                bin_num[0] = 19
                    else:
                        if (feature[18]<=0.0):
                            if (feature[11]<=0.0):
                                bin_num[0] = 20
                            else:
                                bin_num[0] = 21
                        else:
                            if (feature[17]<=0.0):
                                bin_num[0] = 22
                            else:
                                bin_num[0] = 23
                else:
                    if (feature[5]<=15.0):
                        if (feature[18]<=0.0):
                            if (feature[36]<=0.0):
                                bin_num[0] = 24
                            else:
                                bin_num[0] = 25
                        else:
                            if (feature[3]<=2.0):
                                bin_num[0] = 26
                            else:
                                bin_num[0] = 27
                    else:
                        if (feature[7]<=7.0):
                            if (feature[8]<=34.0):
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
                if (feature[12]<=3.0):
                    if (feature[20]<=0.0):
                        if (feature[28]<=0.0):
                            if (feature[19]<=0.0):
                                bin_num[0] = 32
                            else:
                                bin_num[0] = 33
                        else:
                            if (feature[16]<=0.0):
                                bin_num[0] = 34
                            else:
                                bin_num[0] = 35
                    else:
                        if (feature[35]<=0.0):
                            if (feature[34]<=0.0):
                                bin_num[0] = 36
                            else:
                                bin_num[0] = 37
                        else:
                            if (feature[17]<=0.0):
                                bin_num[0] = 38
                            else:
                                bin_num[0] = 39
                else:
                    if (feature[6]<=2.0):
                        if (feature[27]<=0.0):
                            if (feature[1]<=2.0):
                                bin_num[0] = 40
                            else:
                                bin_num[0] = 41
                        else:
                            bin_num[0] = 42
                    else:
                        if (feature[27]<=0.0):
                            if (feature[1]<=2.0):
                                bin_num[0] = 43
                            else:
                                bin_num[0] = 44
                        else:
                            if (feature[25]<=0.0):
                                bin_num[0] = 45
                            else:
                                bin_num[0] = 46
            else:
                if (feature[7]<=7.0):
                    if (feature[2]<=4.0):
                        if (feature[21]<=0.0):
                            if (feature[25]<=0.0):
                                bin_num[0] = 47
                            else:
                                bin_num[0] = 48
                        else:
                            if (feature[29]<=0.0):
                                bin_num[0] = 49
                            else:
                                bin_num[0] = 50
                    else:
                        if (feature[20]<=0.0):
                            if (feature[28]<=0.0):
                                bin_num[0] = 51
                            else:
                                bin_num[0] = 52
                        else:
                            if (feature[12]<=3.0):
                                bin_num[0] = 53
                            else:
                                bin_num[0] = 54
                else:
                    if (feature[12]<=3.0):
                        if (feature[19]<=0.0):
                            if (feature[22]<=0.0):
                                bin_num[0] = 55
                            else:
                                bin_num[0] = 56
                        else:
                            if (feature[21]<=0.0):
                                bin_num[0] = 57
                            else:
                                bin_num[0] = 58
                    else:
                        if (feature[22]<=0.0):
                            if (feature[29]<=0.0):
                                bin_num[0] = 59
                            else:
                                bin_num[0] = 60
                        else:
                            if (feature[2]<=4.0):
                                bin_num[0] = 61
                            else:
                                bin_num[0] = 62
    else:
        if (feature[5]<=15.0):
            if (feature[12]<=3.0):
                if (feature[6]<=2.0):
                    if (feature[24]<=0.0):
                        if (feature[18]<=0.0):
                            if (feature[27]<=0.0):
                                bin_num[0] = 63
                            else:
                                bin_num[0] = 64
                        else:
                            if (feature[36]<=0.0):
                                bin_num[0] = 65
                            else:
                                bin_num[0] = 66
                    else:
                        if (feature[38]<=0.0):
                            if (feature[9]<=0.0):
                                bin_num[0] = 67
                            else:
                                bin_num[0] = 68
                        else:
                            if (feature[11]<=0.0):
                                bin_num[0] = 69
                            else:
                                bin_num[0] = 70
                else:
                    if (feature[3]<=2.0):
                        if (feature[10]<=1.0):
                            if (feature[28]<=0.0):
                                bin_num[0] = 71
                            else:
                                bin_num[0] = 72
                        else:
                            if (feature[28]<=0.0):
                                bin_num[0] = 73
                            else:
                                bin_num[0] = 74
                    else:
                        if (feature[28]<=0.0):
                            if (feature[21]<=0.0):
                                bin_num[0] = 75
                            else:
                                bin_num[0] = 76
                        else:
                            if (feature[23]<=0.0):
                                bin_num[0] = 77
                            else:
                                bin_num[0] = 78
            else:
                if (feature[10]<=1.0):
                    if (feature[6]<=2.0):
                        if (feature[20]<=0.0):
                            if (feature[22]<=0.0):
                                bin_num[0] = 79
                            else:
                                bin_num[0] = 80
                        else:
                            if (feature[8]<=34.0):
                                bin_num[0] = 81
                            else:
                                bin_num[0] = 82
                    else:
                        if (feature[25]<=0.0):
                            if (feature[37]<=0.0):
                                bin_num[0] = 83
                            else:
                                bin_num[0] = 84
                        else:
                            if (feature[21]<=0.0):
                                bin_num[0] = 85
                            else:
                                bin_num[0] = 86
                else:
                    if (feature[24]<=0.0):
                        if (feature[27]<=0.0):
                            if (feature[20]<=0.0):
                                bin_num[0] = 87
                            else:
                                bin_num[0] = 88
                        else:
                            if (feature[8]<=34.0):
                                bin_num[0] = 89
                            else:
                                bin_num[0] = 90
                    else:
                        if (feature[34]<=0.0):
                            if (feature[1]<=2.0):
                                bin_num[0] = 91
                            else:
                                bin_num[0] = 92
                        else:
                            if (feature[20]<=0.0):
                                bin_num[0] = 93
                            else:
                                bin_num[0] = 94
        else:
            if (feature[10]<=1.0):
                if (feature[2]<=4.0):
                    if (feature[19]<=0.0):
                        if (feature[21]<=0.0):
                            if (feature[7]<=7.0):
                                bin_num[0] = 95
                            else:
                                bin_num[0] = 96
                        else:
                            if (feature[38]<=0.0):
                                bin_num[0] = 97
                            else:
                                bin_num[0] = 98
                    else:
                        if (feature[22]<=0.0):
                            if (feature[12]<=3.0):
                                bin_num[0] = 99
                            else:
                                bin_num[0] = 100
                        else:
                            if (feature[32]<=0.0):
                                bin_num[0] = 101
                            else:
                                bin_num[0] = 102
                else:
                    if (feature[28]<=0.0):
                        if (feature[19]<=0.0):
                            if (feature[22]<=0.0):
                                bin_num[0] = 103
                            else:
                                bin_num[0] = 104
                        else:
                            if (feature[12]<=3.0):
                                bin_num[0] = 105
                            else:
                                bin_num[0] = 106
                    else:
                        if (feature[12]<=3.0):
                            if (feature[6]<=2.0):
                                bin_num[0] = 107
                            else:
                                bin_num[0] = 108
                        else:
                            if (feature[20]<=0.0):
                                bin_num[0] = 109
                            else:
                                bin_num[0] = 110
            else:
                if (feature[2]<=4.0):
                    if (feature[21]<=0.0):
                        if (feature[29]<=0.0):
                            if (feature[35]<=0.0):
                                bin_num[0] = 111
                            else:
                                bin_num[0] = 112
                        else:
                            if (feature[9]<=0.0):
                                bin_num[0] = 113
                            else:
                                bin_num[0] = 114
                    else:
                        if (feature[12]<=3.0):
                            if (feature[22]<=0.0):
                                bin_num[0] = 115
                            else:
                                bin_num[0] = 116
                        else:
                            if (feature[38]<=0.0):
                                bin_num[0] = 117
                            else:
                                bin_num[0] = 118
                else:
                    if (feature[12]<=3.0):
                        if (feature[35]<=0.0):
                            if (feature[25]<=0.0):
                                bin_num[0] = 119
                            else:
                                bin_num[0] = 120
                        else:
                            if (feature[23]<=0.0):
                                bin_num[0] = 121
                            else:
                                bin_num[0] = 122
                    else:
                        if (feature[24]<=0.0):
                            if (feature[21]<=0.0):
                                bin_num[0] = 123
                            else:
                                bin_num[0] = 124
                        else:
                            if (feature[31]<=0.0):
                                bin_num[0] = 125
                            else:
                                bin_num[0] = 126
    # Tree 1
    if (feature[6]<=2.0):
        if (feature[7]<=7.0):
            if (feature[13]<=0.0):
                if (feature[35]<=0.0):
                    if (feature[21]<=0.0):
                        if (feature[0]<=0.0):
                            if (feature[8]<=35.0):
                                bin_num[1] = 0
                            else:
                                bin_num[1] = 1
                        else:
                            if (feature[5]<=16.0):
                                bin_num[1] = 2
                            else:
                                bin_num[1] = 3
                    else:
                        if (feature[5]<=16.0):
                            if (feature[17]<=0.0):
                                bin_num[1] = 4
                            else:
                                bin_num[1] = 5
                        else:
                            if (feature[2]<=4.0):
                                bin_num[1] = 6
                            else:
                                bin_num[1] = 7
                else:
                    if (feature[2]<=4.0):
                        if (feature[34]<=0.0):
                            if (feature[0]<=0.0):
                                bin_num[1] = 8
                            else:
                                bin_num[1] = 9
                        else:
                            if (feature[3]<=2.0):
                                bin_num[1] = 10
                            else:
                                bin_num[1] = 11
                    else:
                        if (feature[37]<=0.0):
                            if (feature[26]<=0.0):
                                bin_num[1] = 12
                            else:
                                bin_num[1] = 13
                        else:
                            if (feature[31]<=0.0):
                                bin_num[1] = 14
                            else:
                                bin_num[1] = 15
            else:
                if (feature[23]<=0.0):
                    if (feature[8]<=35.0):
                        if (feature[2]<=4.0):
                            if (feature[21]<=0.0):
                                bin_num[1] = 16
                            else:
                                bin_num[1] = 17
                        else:
                            if (feature[4]<=1941.0):
                                bin_num[1] = 18
                            else:
                                bin_num[1] = 19
                    else:
                        if (feature[19]<=0.0):
                            if (feature[11]<=0.0):
                                bin_num[1] = 20
                            else:
                                bin_num[1] = 21
                        else:
                            if (feature[33]<=0.0):
                                bin_num[1] = 22
                            else:
                                bin_num[1] = 23
                else:
                    if (feature[25]<=0.0):
                        if (feature[18]<=0.0):
                            if (feature[28]<=0.0):
                                bin_num[1] = 24
                            else:
                                bin_num[1] = 25
                        else:
                            if (feature[2]<=4.0):
                                bin_num[1] = 26
                            else:
                                bin_num[1] = 27
                    else:
                        if (feature[35]<=0.0):
                            if (feature[21]<=0.0):
                                bin_num[1] = 28
                            else:
                                bin_num[1] = 29
                        else:
                            if (feature[12]<=3.0):
                                bin_num[1] = 30
                            else:
                                bin_num[1] = 31
        else:
            if (feature[4]<=1941.0):
                if (feature[19]<=0.0):
                    if (feature[20]<=0.0):
                        if (feature[32]<=0.0):
                            if (feature[13]<=0.0):
                                bin_num[1] = 32
                            else:
                                bin_num[1] = 33
                        else:
                            if (feature[36]<=0.0):
                                bin_num[1] = 34
                            else:
                                bin_num[1] = 35
                    else:
                        if (feature[15]<=0.0):
                            if (feature[35]<=0.0):
                                bin_num[1] = 36
                            else:
                                bin_num[1] = 37
                        else:
                            if (feature[28]<=0.0):
                                bin_num[1] = 38
                            else:
                                bin_num[1] = 39
                else:
                    if (feature[35]<=0.0):
                        if (feature[2]<=4.0):
                            if (feature[21]<=0.0):
                                bin_num[1] = 40
                            else:
                                bin_num[1] = 41
                        else:
                            if (feature[38]<=0.0):
                                bin_num[1] = 42
                            else:
                                bin_num[1] = 43
                    else:
                        if (feature[21]<=0.0):
                            if (feature[1]<=2.0):
                                bin_num[1] = 44
                            else:
                                bin_num[1] = 45
                        else:
                            if (feature[9]<=0.0):
                                bin_num[1] = 46
                            else:
                                bin_num[1] = 47
            else:
                if (feature[21]<=0.0):
                    if (feature[5]<=16.0):
                        if (feature[19]<=0.0):
                            if (feature[12]<=3.0):
                                bin_num[1] = 48
                            else:
                                bin_num[1] = 49
                        else:
                            if (feature[13]<=0.0):
                                bin_num[1] = 50
                            else:
                                bin_num[1] = 51
                    else:
                        if (feature[8]<=35.0):
                            if (feature[2]<=4.0):
                                bin_num[1] = 52
                            else:
                                bin_num[1] = 53
                        else:
                            if (feature[36]<=0.0):
                                bin_num[1] = 54
                            else:
                                bin_num[1] = 55
                else:
                    if (feature[17]<=0.0):
                        if (feature[26]<=0.0):
                            if (feature[18]<=0.0):
                                bin_num[1] = 56
                            else:
                                bin_num[1] = 57
                        else:
                            if (feature[29]<=0.0):
                                bin_num[1] = 58
                            else:
                                bin_num[1] = 59
                    else:
                        if (feature[2]<=4.0):
                            if (feature[10]<=1.0):
                                bin_num[1] = 60
                            else:
                                bin_num[1] = 61
                        else:
                            if (feature[30]<=0.0):
                                bin_num[1] = 62
                            else:
                                bin_num[1] = 63
    else:
        if (feature[5]<=16.0):
            if (feature[25]<=0.0):
                if (feature[22]<=0.0):
                    if (feature[8]<=35.0):
                        if (feature[35]<=0.0):
                            if (feature[29]<=0.0):
                                bin_num[1] = 64
                            else:
                                bin_num[1] = 65
                        else:
                            if (feature[31]<=0.0):
                                bin_num[1] = 66
                            else:
                                bin_num[1] = 67
                    else:
                        if (feature[34]<=0.0):
                            if (feature[4]<=1941.0):
                                bin_num[1] = 68
                            else:
                                bin_num[1] = 69
                        else:
                            if (feature[31]<=0.0):
                                bin_num[1] = 70
                            else:
                                bin_num[1] = 71
                else:
                    if (feature[19]<=0.0):
                        if (feature[2]<=4.0):
                            if (feature[21]<=0.0):
                                bin_num[1] = 72
                            else:
                                bin_num[1] = 73
                        else:
                            if (feature[12]<=3.0):
                                bin_num[1] = 74
                            else:
                                bin_num[1] = 75
                    else:
                        if (feature[9]<=0.0):
                            if (feature[0]<=0.0):
                                bin_num[1] = 76
                            else:
                                bin_num[1] = 77
                        else:
                            if (feature[21]<=0.0):
                                bin_num[1] = 78
                            else:
                                bin_num[1] = 79
            else:
                if (feature[23]<=0.0):
                    if (feature[3]<=2.0):
                        if (feature[9]<=0.0):
                            if (feature[37]<=0.0):
                                bin_num[1] = 80
                            else:
                                bin_num[1] = 81
                        else:
                            if (feature[21]<=0.0):
                                bin_num[1] = 82
                            else:
                                bin_num[1] = 83
                    else:
                        if (feature[12]<=3.0):
                            if (feature[17]<=0.0):
                                bin_num[1] = 84
                            else:
                                bin_num[1] = 85
                        else:
                            if (feature[29]<=0.0):
                                bin_num[1] = 86
                            else:
                                bin_num[1] = 87
                else:
                    if (feature[29]<=0.0):
                        if (feature[21]<=0.0):
                            if (feature[27]<=0.0):
                                bin_num[1] = 88
                            else:
                                bin_num[1] = 89
                        else:
                            if (feature[7]<=7.0):
                                bin_num[1] = 90
                            else:
                                bin_num[1] = 91
                    else:
                        if (feature[10]<=1.0):
                            if (feature[7]<=7.0):
                                bin_num[1] = 92
                            else:
                                bin_num[1] = 93
                        else:
                            if (feature[38]<=0.0):
                                bin_num[1] = 94
                            else:
                                bin_num[1] = 95
        else:
            if (feature[12]<=3.0):
                if (feature[35]<=0.0):
                    if (feature[21]<=0.0):
                        if (feature[29]<=0.0):
                            if (feature[1]<=2.0):
                                bin_num[1] = 96
                            else:
                                bin_num[1] = 97
                        else:
                            if (feature[2]<=4.0):
                                bin_num[1] = 98
                            else:
                                bin_num[1] = 99
                    else:
                        if (feature[18]<=0.0):
                            if (feature[24]<=0.0):
                                bin_num[1] = 100
                            else:
                                bin_num[1] = 101
                        else:
                            if (feature[17]<=0.0):
                                bin_num[1] = 102
                            else:
                                bin_num[1] = 103
                else:
                    if (feature[3]<=2.0):
                        if (feature[7]<=7.0):
                            if (feature[13]<=0.0):
                                bin_num[1] = 104
                            else:
                                bin_num[1] = 105
                        else:
                            if (feature[10]<=1.0):
                                bin_num[1] = 106
                            else:
                                bin_num[1] = 107
                    else:
                        if (feature[25]<=0.0):
                            if (feature[15]<=0.0):
                                bin_num[1] = 108
                            else:
                                bin_num[1] = 109
                        else:
                            if (feature[33]<=0.0):
                                bin_num[1] = 110
                            else:
                                bin_num[1] = 111
            else:
                if (feature[18]<=0.0):
                    if (feature[22]<=0.0):
                        if (feature[4]<=1941.0):
                            if (feature[27]<=0.0):
                                bin_num[1] = 112
                            else:
                                bin_num[1] = 113
                        else:
                            if (feature[37]<=0.0):
                                bin_num[1] = 114
                            else:
                                bin_num[1] = 115
                    else:
                        if (feature[21]<=0.0):
                            if (feature[2]<=4.0):
                                bin_num[1] = 116
                            else:
                                bin_num[1] = 117
                        else:
                            if (feature[14]<=0.0):
                                bin_num[1] = 118
                            else:
                                bin_num[1] = 119
                else:
                    if (feature[35]<=0.0):
                        if (feature[17]<=0.0):
                            if (feature[37]<=0.0):
                                bin_num[1] = 120
                            else:
                                bin_num[1] = 121
                        else:
                            if (feature[4]<=1941.0):
                                bin_num[1] = 122
                            else:
                                bin_num[1] = 123
                    else:
                        if (feature[10]<=1.0):
                            if (feature[1]<=2.0):
                                bin_num[1] = 124
                            else:
                                bin_num[1] = 125
                        else:
                            if (feature[8]<=35.0):
                                bin_num[1] = 126
                            else:
                                bin_num[1] = 127
    # Tree 0
    if (feature[0]<=0.0):
        if (feature[10]<=1.0):
            if (feature[12]<=3.0):
                if (feature[19]<=0.0):
                    if (feature[18]<=0.0):
                        if (feature[13]<=0.0):
                            if (feature[35]<=0.0):
                                bin_num[0] = 0
                            else:
                                bin_num[0] = 1
                        else:
                            if (feature[8]<=36.0):
                                bin_num[0] = 2
                            else:
                                bin_num[0] = 3
                    else:
                        if (feature[35]<=0.0):
                            if (feature[20]<=0.0):
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
                        if (feature[2]<=4.0):
                            if (feature[7]<=7.0):
                                bin_num[0] = 8
                            else:
                                bin_num[0] = 9
                        else:
                            if (feature[13]<=0.0):
                                bin_num[0] = 10
                            else:
                                bin_num[0] = 11
                    else:
                        if (feature[35]<=0.0):
                            if (feature[5]<=14.0):
                                bin_num[0] = 12
                            else:
                                bin_num[0] = 13
                        else:
                            if (feature[6]<=2.0):
                                bin_num[0] = 14
                            else:
                                bin_num[0] = 15
            else:
                if (feature[6]<=2.0):
                    if (feature[35]<=0.0):
                        if (feature[23]<=0.0):
                            if (feature[2]<=4.0):
                                bin_num[0] = 16
                            else:
                                bin_num[0] = 17
                        else:
                            if (feature[19]<=0.0):
                                bin_num[0] = 18
                            else:
                                bin_num[0] = 19
                    else:
                        if (feature[18]<=0.0):
                            if (feature[11]<=0.0):
                                bin_num[0] = 20
                            else:
                                bin_num[0] = 21
                        else:
                            if (feature[17]<=0.0):
                                bin_num[0] = 22
                            else:
                                bin_num[0] = 23
                else:
                    if (feature[5]<=14.0):
                        if (feature[18]<=0.0):
                            if (feature[36]<=0.0):
                                bin_num[0] = 24
                            else:
                                bin_num[0] = 25
                        else:
                            if (feature[3]<=2.0):
                                bin_num[0] = 26
                            else:
                                bin_num[0] = 27
                    else:
                        if (feature[7]<=7.0):
                            if (feature[8]<=36.0):
                                bin_num[0] = 28
                            else:
                                bin_num[0] = 29
                        else:
                            if (feature[18]<=0.0):
                                bin_num[0] = 30
                            else:
                                bin_num[0] = 31
        else:
            if (feature[5]<=14.0):
                if (feature[12]<=3.0):
                    if (feature[20]<=0.0):
                        if (feature[19]<=0.0):
                            if (feature[38]<=0.0):
                                bin_num[0] = 32
                            else:
                                bin_num[0] = 33
                        else:
                            if (feature[28]<=0.0):
                                bin_num[0] = 34
                            else:
                                bin_num[0] = 35
                    else:
                        if (feature[35]<=0.0):
                            if (feature[34]<=0.0):
                                bin_num[0] = 36
                            else:
                                bin_num[0] = 37
                        else:
                            if (feature[17]<=0.0):
                                bin_num[0] = 38
                            else:
                                bin_num[0] = 39
                else:
                    if (feature[6]<=2.0):
                        if (feature[8]<=36.0):
                            if (feature[35]<=0.0):
                                bin_num[0] = 40
                            else:
                                bin_num[0] = 41
                        else:
                            if (feature[22]<=0.0):
                                bin_num[0] = 42
                            else:
                                bin_num[0] = 43
                    else:
                        if (feature[27]<=0.0):
                            if (feature[8]<=36.0):
                                bin_num[0] = 44
                            else:
                                bin_num[0] = 45
                        else:
                            if (feature[18]<=0.0):
                                bin_num[0] = 46
                            else:
                                bin_num[0] = 47
            else:
                if (feature[7]<=7.0):
                    if (feature[2]<=4.0):
                        if (feature[20]<=0.0):
                            if (feature[25]<=0.0):
                                bin_num[0] = 48
                            else:
                                bin_num[0] = 49
                        else:
                            if (feature[35]<=0.0):
                                bin_num[0] = 50
                            else:
                                bin_num[0] = 51
                    else:
                        if (feature[20]<=0.0):
                            if (feature[28]<=0.0):
                                bin_num[0] = 52
                            else:
                                bin_num[0] = 53
                        else:
                            if (feature[12]<=3.0):
                                bin_num[0] = 54
                            else:
                                bin_num[0] = 55
                else:
                    if (feature[12]<=3.0):
                        if (feature[19]<=0.0):
                            if (feature[22]<=0.0):
                                bin_num[0] = 56
                            else:
                                bin_num[0] = 57
                        else:
                            if (feature[21]<=0.0):
                                bin_num[0] = 58
                            else:
                                bin_num[0] = 59
                    else:
                        if (feature[22]<=0.0):
                            if (feature[29]<=0.0):
                                bin_num[0] = 60
                            else:
                                bin_num[0] = 61
                        else:
                            if (feature[2]<=4.0):
                                bin_num[0] = 62
                            else:
                                bin_num[0] = 63
    else:
        if (feature[5]<=14.0):
            if (feature[12]<=3.0):
                if (feature[6]<=2.0):
                    if (feature[24]<=0.0):
                        if (feature[18]<=0.0):
                            if (feature[27]<=0.0):
                                bin_num[0] = 64
                            else:
                                bin_num[0] = 65
                        else:
                            if (feature[36]<=0.0):
                                bin_num[0] = 66
                            else:
                                bin_num[0] = 67
                    else:
                        if (feature[9]<=0.0):
                            if (feature[32]<=0.0):
                                bin_num[0] = 68
                            else:
                                bin_num[0] = 69
                        else:
                            if (feature[38]<=0.0):
                                bin_num[0] = 70
                            else:
                                bin_num[0] = 71
                else:
                    if (feature[3]<=2.0):
                        if (feature[10]<=1.0):
                            if (feature[28]<=0.0):
                                bin_num[0] = 72
                            else:
                                bin_num[0] = 73
                        else:
                            if (feature[28]<=0.0):
                                bin_num[0] = 74
                            else:
                                bin_num[0] = 75
                    else:
                        if (feature[28]<=0.0):
                            if (feature[21]<=0.0):
                                bin_num[0] = 76
                            else:
                                bin_num[0] = 77
                        else:
                            if (feature[23]<=0.0):
                                bin_num[0] = 78
                            else:
                                bin_num[0] = 79
            else:
                if (feature[10]<=1.0):
                    if (feature[22]<=0.0):
                        if (feature[38]<=0.0):
                            if (feature[15]<=0.0):
                                bin_num[0] = 80
                            else:
                                bin_num[0] = 81
                        else:
                            if (feature[9]<=0.0):
                                bin_num[0] = 82
                            else:
                                bin_num[0] = 83
                    else:
                        if (feature[20]<=0.0):
                            if (feature[9]<=0.0):
                                bin_num[0] = 84
                            else:
                                bin_num[0] = 85
                        else:
                            if (feature[28]<=0.0):
                                bin_num[0] = 86
                            else:
                                bin_num[0] = 87
                else:
                    if (feature[24]<=0.0):
                        if (feature[27]<=0.0):
                            if (feature[20]<=0.0):
                                bin_num[0] = 88
                            else:
                                bin_num[0] = 89
                        else:
                            if (feature[6]<=2.0):
                                bin_num[0] = 90
                            else:
                                bin_num[0] = 91
                    else:
                        if (feature[1]<=2.0):
                            if (feature[21]<=0.0):
                                bin_num[0] = 92
                            else:
                                bin_num[0] = 93
                        else:
                            if (feature[7]<=7.0):
                                bin_num[0] = 94
                            else:
                                bin_num[0] = 95
        else:
            if (feature[10]<=1.0):
                if (feature[2]<=4.0):
                    if (feature[19]<=0.0):
                        if (feature[7]<=7.0):
                            if (feature[21]<=0.0):
                                bin_num[0] = 96
                            else:
                                bin_num[0] = 97
                        else:
                            if (feature[37]<=0.0):
                                bin_num[0] = 98
                            else:
                                bin_num[0] = 99
                    else:
                        if (feature[22]<=0.0):
                            if (feature[12]<=3.0):
                                bin_num[0] = 100
                            else:
                                bin_num[0] = 101
                        else:
                            if (feature[32]<=0.0):
                                bin_num[0] = 102
                            else:
                                bin_num[0] = 103
                else:
                    if (feature[19]<=0.0):
                        if (feature[20]<=0.0):
                            if (feature[27]<=0.0):
                                bin_num[0] = 104
                            else:
                                bin_num[0] = 105
                        else:
                            if (feature[18]<=0.0):
                                bin_num[0] = 106
                            else:
                                bin_num[0] = 107
                    else:
                        if (feature[12]<=3.0):
                            if (feature[6]<=2.0):
                                bin_num[0] = 108
                            else:
                                bin_num[0] = 109
                        else:
                            if (feature[28]<=0.0):
                                bin_num[0] = 110
                            else:
                                bin_num[0] = 111
            else:
                if (feature[2]<=4.0):
                    if (feature[21]<=0.0):
                        if (feature[29]<=0.0):
                            if (feature[35]<=0.0):
                                bin_num[0] = 112
                            else:
                                bin_num[0] = 113
                        else:
                            if (feature[9]<=0.0):
                                bin_num[0] = 114
                            else:
                                bin_num[0] = 115
                    else:
                        if (feature[38]<=0.0):
                            if (feature[12]<=3.0):
                                bin_num[0] = 116
                            else:
                                bin_num[0] = 117
                        else:
                            if (feature[30]<=0.0):
                                bin_num[0] = 118
                            else:
                                bin_num[0] = 119
                else:
                    if (feature[24]<=0.0):
                        if (feature[12]<=3.0):
                            if (feature[35]<=0.0):
                                bin_num[0] = 120
                            else:
                                bin_num[0] = 121
                        else:
                            if (feature[21]<=0.0):
                                bin_num[0] = 122
                            else:
                                bin_num[0] = 123
                    else:
                        if (feature[31]<=0.0):
                            if (feature[6]<=2.0):
                                bin_num[0] = 124
                            else:
                                bin_num[0] = 125
                        else:
                            if (feature[21]<=0.0):
                                bin_num[0] = 126
                            else:
                                bin_num[0] = 127
    # Tree 1
    if (feature[6]<=2.0):
        if (feature[7]<=7.0):
            if (feature[13]<=0.0):
                if (feature[35]<=0.0):
                    if (feature[21]<=0.0):
                        if (feature[0]<=0.0):
                            if (feature[8]<=36.0):
                                bin_num[1] = 0
                            else:
                                bin_num[1] = 1
                        else:
                            if (feature[5]<=16.0):
                                bin_num[1] = 2
                            else:
                                bin_num[1] = 3
                    else:
                        if (feature[5]<=16.0):
                            if (feature[17]<=0.0):
                                bin_num[1] = 4
                            else:
                                bin_num[1] = 5
                        else:
                            if (feature[2]<=4.0):
                                bin_num[1] = 6
                            else:
                                bin_num[1] = 7
                else:
                    if (feature[2]<=4.0):
                        if (feature[0]<=0.0):
                            if (feature[34]<=0.0):
                                bin_num[1] = 8
                            else:
                                bin_num[1] = 9
                        else:
                            bin_num[1] = 10
                    else:
                        if (feature[37]<=0.0):
                            if (feature[26]<=0.0):
                                bin_num[1] = 11
                            else:
                                bin_num[1] = 12
                        else:
                            if (feature[31]<=0.0):
                                bin_num[1] = 13
                            else:
                                bin_num[1] = 14
            else:
                if (feature[2]<=4.0):
                    if (feature[21]<=0.0):
                        if (feature[8]<=36.0):
                            if (feature[23]<=0.0):
                                bin_num[1] = 15
                            else:
                                bin_num[1] = 16
                        else:
                            if (feature[19]<=0.0):
                                bin_num[1] = 17
                            else:
                                bin_num[1] = 18
                    else:
                        if (feature[18]<=0.0):
                            if (feature[25]<=0.0):
                                bin_num[1] = 19
                            else:
                                bin_num[1] = 20
                        else:
                            if (feature[16]<=0.0):
                                bin_num[1] = 21
                            else:
                                bin_num[1] = 22
                else:
                    if (feature[23]<=0.0):
                        if (feature[4]<=1974.0):
                            if (feature[28]<=0.0):
                                bin_num[1] = 23
                            else:
                                bin_num[1] = 24
                        else:
                            if (feature[19]<=0.0):
                                bin_num[1] = 25
                            else:
                                bin_num[1] = 26
                    else:
                        if (feature[35]<=0.0):
                            if (feature[17]<=0.0):
                                bin_num[1] = 27
                            else:
                                bin_num[1] = 28
                        else:
                            if (feature[25]<=0.0):
                                bin_num[1] = 29
                            else:
                                bin_num[1] = 30
        else:
            if (feature[4]<=1974.0):
                if (feature[19]<=0.0):
                    if (feature[20]<=0.0):
                        if (feature[32]<=0.0):
                            if (feature[13]<=0.0):
                                bin_num[1] = 31
                            else:
                                bin_num[1] = 32
                        else:
                            if (feature[36]<=0.0):
                                bin_num[1] = 33
                            else:
                                bin_num[1] = 34
                    else:
                        if (feature[15]<=0.0):
                            if (feature[35]<=0.0):
                                bin_num[1] = 35
                            else:
                                bin_num[1] = 36
                        else:
                            if (feature[28]<=0.0):
                                bin_num[1] = 37
                            else:
                                bin_num[1] = 38
                else:
                    if (feature[2]<=4.0):
                        if (feature[21]<=0.0):
                            if (feature[31]<=0.0):
                                bin_num[1] = 39
                            else:
                                bin_num[1] = 40
                        else:
                            if (feature[1]<=3.0):
                                bin_num[1] = 41
                            else:
                                bin_num[1] = 42
                    else:
                        if (feature[35]<=0.0):
                            if (feature[38]<=0.0):
                                bin_num[1] = 43
                            else:
                                bin_num[1] = 44
                        else:
                            if (feature[20]<=0.0):
                                bin_num[1] = 45
                            else:
                                bin_num[1] = 46
            else:
                if (feature[21]<=0.0):
                    if (feature[5]<=16.0):
                        if (feature[19]<=0.0):
                            if (feature[12]<=3.0):
                                bin_num[1] = 47
                            else:
                                bin_num[1] = 48
                        else:
                            if (feature[10]<=1.0):
                                bin_num[1] = 49
                            else:
                                bin_num[1] = 50
                    else:
                        if (feature[8]<=36.0):
                            if (feature[11]<=0.0):
                                bin_num[1] = 51
                            else:
                                bin_num[1] = 52
                        else:
                            if (feature[36]<=0.0):
                                bin_num[1] = 53
                            else:
                                bin_num[1] = 54
                else:
                    if (feature[17]<=0.0):
                        if (feature[26]<=0.0):
                            if (feature[18]<=0.0):
                                bin_num[1] = 55
                            else:
                                bin_num[1] = 56
                        else:
                            if (feature[19]<=0.0):
                                bin_num[1] = 57
                            else:
                                bin_num[1] = 58
                    else:
                        if (feature[2]<=4.0):
                            if (feature[10]<=1.0):
                                bin_num[1] = 59
                            else:
                                bin_num[1] = 60
                        else:
                            if (feature[30]<=0.0):
                                bin_num[1] = 61
                            else:
                                bin_num[1] = 62
    else:
        if (feature[5]<=16.0):
            if (feature[25]<=0.0):
                if (feature[22]<=0.0):
                    if (feature[8]<=36.0):
                        if (feature[27]<=0.0):
                            if (feature[24]<=0.0):
                                bin_num[1] = 63
                            else:
                                bin_num[1] = 64
                        else:
                            if (feature[11]<=0.0):
                                bin_num[1] = 65
                            else:
                                bin_num[1] = 66
                    else:
                        if (feature[34]<=0.0):
                            if (feature[24]<=0.0):
                                bin_num[1] = 67
                            else:
                                bin_num[1] = 68
                        else:
                            if (feature[31]<=0.0):
                                bin_num[1] = 69
                            else:
                                bin_num[1] = 70
                else:
                    if (feature[19]<=0.0):
                        if (feature[1]<=3.0):
                            if (feature[21]<=0.0):
                                bin_num[1] = 71
                            else:
                                bin_num[1] = 72
                        else:
                            if (feature[18]<=0.0):
                                bin_num[1] = 73
                            else:
                                bin_num[1] = 74
                    else:
                        if (feature[10]<=1.0):
                            if (feature[38]<=0.0):
                                bin_num[1] = 75
                            else:
                                bin_num[1] = 76
                        else:
                            if (feature[1]<=3.0):
                                bin_num[1] = 77
                            else:
                                bin_num[1] = 78
            else:
                if (feature[23]<=0.0):
                    if (feature[3]<=2.0):
                        if (feature[9]<=0.0):
                            if (feature[37]<=0.0):
                                bin_num[1] = 79
                            else:
                                bin_num[1] = 80
                        else:
                            if (feature[21]<=0.0):
                                bin_num[1] = 81
                            else:
                                bin_num[1] = 82
                    else:
                        if (feature[12]<=3.0):
                            if (feature[17]<=0.0):
                                bin_num[1] = 83
                            else:
                                bin_num[1] = 84
                        else:
                            if (feature[29]<=0.0):
                                bin_num[1] = 85
                            else:
                                bin_num[1] = 86
                else:
                    if (feature[29]<=0.0):
                        if (feature[21]<=0.0):
                            if (feature[27]<=0.0):
                                bin_num[1] = 87
                            else:
                                bin_num[1] = 88
                        else:
                            if (feature[24]<=0.0):
                                bin_num[1] = 89
                            else:
                                bin_num[1] = 90
                    else:
                        if (feature[10]<=1.0):
                            if (feature[7]<=7.0):
                                bin_num[1] = 91
                            else:
                                bin_num[1] = 92
                        else:
                            if (feature[38]<=0.0):
                                bin_num[1] = 93
                            else:
                                bin_num[1] = 94
        else:
            if (feature[12]<=3.0):
                if (feature[21]<=0.0):
                    if (feature[29]<=0.0):
                        if (feature[28]<=0.0):
                            if (feature[0]<=0.0):
                                bin_num[1] = 95
                            else:
                                bin_num[1] = 96
                        else:
                            if (feature[22]<=0.0):
                                bin_num[1] = 97
                            else:
                                bin_num[1] = 98
                    else:
                        if (feature[2]<=4.0):
                            if (feature[18]<=0.0):
                                bin_num[1] = 99
                            else:
                                bin_num[1] = 100
                        else:
                            if (feature[13]<=0.0):
                                bin_num[1] = 101
                            else:
                                bin_num[1] = 102
                else:
                    if (feature[18]<=0.0):
                        if (feature[35]<=0.0):
                            if (feature[24]<=0.0):
                                bin_num[1] = 103
                            else:
                                bin_num[1] = 104
                        else:
                            if (feature[26]<=0.0):
                                bin_num[1] = 105
                            else:
                                bin_num[1] = 106
                    else:
                        if (feature[17]<=0.0):
                            if (feature[31]<=0.0):
                                bin_num[1] = 107
                            else:
                                bin_num[1] = 108
                        else:
                            if (feature[4]<=1974.0):
                                bin_num[1] = 109
                            else:
                                bin_num[1] = 110
            else:
                if (feature[22]<=0.0):
                    if (feature[4]<=1974.0):
                        if (feature[29]<=0.0):
                            if (feature[10]<=1.0):
                                bin_num[1] = 111
                            else:
                                bin_num[1] = 112
                        else:
                            if (feature[20]<=0.0):
                                bin_num[1] = 113
                            else:
                                bin_num[1] = 114
                    else:
                        if (feature[1]<=3.0):
                            if (feature[32]<=0.0):
                                bin_num[1] = 115
                            else:
                                bin_num[1] = 116
                        else:
                            if (feature[21]<=0.0):
                                bin_num[1] = 117
                            else:
                                bin_num[1] = 118
                else:
                    if (feature[18]<=0.0):
                        if (feature[21]<=0.0):
                            if (feature[2]<=4.0):
                                bin_num[1] = 119
                            else:
                                bin_num[1] = 120
                        else:
                            if (feature[14]<=0.0):
                                bin_num[1] = 121
                            else:
                                bin_num[1] = 122
                    else:
                        if (feature[17]<=0.0):
                            if (feature[36]<=0.0):
                                bin_num[1] = 123
                            else:
                                bin_num[1] = 124
                        else:
                            if (feature[0]<=0.0):
                                bin_num[1] = 125
                            else:
                                bin_num[1] = 126
    # Tree 0
    if (feature[0]<=0.0):
        if (feature[10]<=1.0):
            if (feature[12]<=3.0):
                if (feature[19]<=0.0):
                    if (feature[18]<=0.0):
                        if (feature[13]<=0.0):
                            if (feature[35]<=0.0):
                                bin_num[0] = 0
                            else:
                                bin_num[0] = 1
                        else:
                            if (feature[8]<=36.0):
                                bin_num[0] = 2
                            else:
                                bin_num[0] = 3
                    else:
                        if (feature[35]<=0.0):
                            if (feature[20]<=0.0):
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
                        if (feature[2]<=4.0):
                            if (feature[7]<=7.0):
                                bin_num[0] = 8
                            else:
                                bin_num[0] = 9
                        else:
                            if (feature[13]<=0.0):
                                bin_num[0] = 10
                            else:
                                bin_num[0] = 11
                    else:
                        if (feature[35]<=0.0):
                            if (feature[5]<=14.0):
                                bin_num[0] = 12
                            else:
                                bin_num[0] = 13
                        else:
                            if (feature[6]<=2.0):
                                bin_num[0] = 14
                            else:
                                bin_num[0] = 15
            else:
                if (feature[6]<=2.0):
                    if (feature[35]<=0.0):
                        if (feature[23]<=0.0):
                            if (feature[2]<=4.0):
                                bin_num[0] = 16
                            else:
                                bin_num[0] = 17
                        else:
                            if (feature[19]<=0.0):
                                bin_num[0] = 18
                            else:
                                bin_num[0] = 19
                    else:
                        if (feature[18]<=0.0):
                            if (feature[11]<=0.0):
                                bin_num[0] = 20
                            else:
                                bin_num[0] = 21
                        else:
                            if (feature[17]<=0.0):
                                bin_num[0] = 22
                            else:
                                bin_num[0] = 23
                else:
                    if (feature[5]<=14.0):
                        if (feature[18]<=0.0):
                            if (feature[36]<=0.0):
                                bin_num[0] = 24
                            else:
                                bin_num[0] = 25
                        else:
                            if (feature[3]<=2.0):
                                bin_num[0] = 26
                            else:
                                bin_num[0] = 27
                    else:
                        if (feature[7]<=7.0):
                            if (feature[8]<=36.0):
                                bin_num[0] = 28
                            else:
                                bin_num[0] = 29
                        else:
                            if (feature[18]<=0.0):
                                bin_num[0] = 30
                            else:
                                bin_num[0] = 31
        else:
            if (feature[5]<=14.0):
                if (feature[12]<=3.0):
                    if (feature[20]<=0.0):
                        if (feature[19]<=0.0):
                            if (feature[38]<=0.0):
                                bin_num[0] = 32
                            else:
                                bin_num[0] = 33
                        else:
                            if (feature[28]<=0.0):
                                bin_num[0] = 34
                            else:
                                bin_num[0] = 35
                    else:
                        if (feature[35]<=0.0):
                            if (feature[34]<=0.0):
                                bin_num[0] = 36
                            else:
                                bin_num[0] = 37
                        else:
                            if (feature[17]<=0.0):
                                bin_num[0] = 38
                            else:
                                bin_num[0] = 39
                else:
                    if (feature[6]<=2.0):
                        if (feature[8]<=36.0):
                            if (feature[35]<=0.0):
                                bin_num[0] = 40
                            else:
                                bin_num[0] = 41
                        else:
                            if (feature[22]<=0.0):
                                bin_num[0] = 42
                            else:
                                bin_num[0] = 43
                    else:
                        if (feature[27]<=0.0):
                            if (feature[8]<=36.0):
                                bin_num[0] = 44
                            else:
                                bin_num[0] = 45
                        else:
                            if (feature[18]<=0.0):
                                bin_num[0] = 46
                            else:
                                bin_num[0] = 47
            else:
                if (feature[7]<=7.0):
                    if (feature[2]<=4.0):
                        if (feature[20]<=0.0):
                            if (feature[25]<=0.0):
                                bin_num[0] = 48
                            else:
                                bin_num[0] = 49
                        else:
                            if (feature[35]<=0.0):
                                bin_num[0] = 50
                            else:
                                bin_num[0] = 51
                    else:
                        if (feature[20]<=0.0):
                            if (feature[28]<=0.0):
                                bin_num[0] = 52
                            else:
                                bin_num[0] = 53
                        else:
                            if (feature[12]<=3.0):
                                bin_num[0] = 54
                            else:
                                bin_num[0] = 55
                else:
                    if (feature[12]<=3.0):
                        if (feature[19]<=0.0):
                            if (feature[22]<=0.0):
                                bin_num[0] = 56
                            else:
                                bin_num[0] = 57
                        else:
                            if (feature[21]<=0.0):
                                bin_num[0] = 58
                            else:
                                bin_num[0] = 59
                    else:
                        if (feature[22]<=0.0):
                            if (feature[29]<=0.0):
                                bin_num[0] = 60
                            else:
                                bin_num[0] = 61
                        else:
                            if (feature[2]<=4.0):
                                bin_num[0] = 62
                            else:
                                bin_num[0] = 63
    else:
        if (feature[5]<=14.0):
            if (feature[12]<=3.0):
                if (feature[6]<=2.0):
                    if (feature[24]<=0.0):
                        if (feature[18]<=0.0):
                            if (feature[27]<=0.0):
                                bin_num[0] = 64
                            else:
                                bin_num[0] = 65
                        else:
                            if (feature[36]<=0.0):
                                bin_num[0] = 66
                            else:
                                bin_num[0] = 67
                    else:
                        if (feature[9]<=0.0):
                            if (feature[32]<=0.0):
                                bin_num[0] = 68
                            else:
                                bin_num[0] = 69
                        else:
                            if (feature[38]<=0.0):
                                bin_num[0] = 70
                            else:
                                bin_num[0] = 71
                else:
                    if (feature[3]<=2.0):
                        if (feature[10]<=1.0):
                            if (feature[28]<=0.0):
                                bin_num[0] = 72
                            else:
                                bin_num[0] = 73
                        else:
                            if (feature[28]<=0.0):
                                bin_num[0] = 74
                            else:
                                bin_num[0] = 75
                    else:
                        if (feature[28]<=0.0):
                            if (feature[21]<=0.0):
                                bin_num[0] = 76
                            else:
                                bin_num[0] = 77
                        else:
                            if (feature[23]<=0.0):
                                bin_num[0] = 78
                            else:
                                bin_num[0] = 79
            else:
                if (feature[10]<=1.0):
                    if (feature[22]<=0.0):
                        if (feature[38]<=0.0):
                            if (feature[15]<=0.0):
                                bin_num[0] = 80
                            else:
                                bin_num[0] = 81
                        else:
                            if (feature[9]<=0.0):
                                bin_num[0] = 82
                            else:
                                bin_num[0] = 83
                    else:
                        if (feature[20]<=0.0):
                            if (feature[9]<=0.0):
                                bin_num[0] = 84
                            else:
                                bin_num[0] = 85
                        else:
                            if (feature[28]<=0.0):
                                bin_num[0] = 86
                            else:
                                bin_num[0] = 87
                else:
                    if (feature[24]<=0.0):
                        if (feature[27]<=0.0):
                            if (feature[20]<=0.0):
                                bin_num[0] = 88
                            else:
                                bin_num[0] = 89
                        else:
                            if (feature[6]<=2.0):
                                bin_num[0] = 90
                            else:
                                bin_num[0] = 91
                    else:
                        if (feature[1]<=2.0):
                            if (feature[21]<=0.0):
                                bin_num[0] = 92
                            else:
                                bin_num[0] = 93
                        else:
                            if (feature[7]<=7.0):
                                bin_num[0] = 94
                            else:
                                bin_num[0] = 95
        else:
            if (feature[10]<=1.0):
                if (feature[2]<=4.0):
                    if (feature[19]<=0.0):
                        if (feature[7]<=7.0):
                            if (feature[21]<=0.0):
                                bin_num[0] = 96
                            else:
                                bin_num[0] = 97
                        else:
                            if (feature[37]<=0.0):
                                bin_num[0] = 98
                            else:
                                bin_num[0] = 99
                    else:
                        if (feature[22]<=0.0):
                            if (feature[12]<=3.0):
                                bin_num[0] = 100
                            else:
                                bin_num[0] = 101
                        else:
                            if (feature[32]<=0.0):
                                bin_num[0] = 102
                            else:
                                bin_num[0] = 103
                else:
                    if (feature[19]<=0.0):
                        if (feature[20]<=0.0):
                            if (feature[27]<=0.0):
                                bin_num[0] = 104
                            else:
                                bin_num[0] = 105
                        else:
                            if (feature[18]<=0.0):
                                bin_num[0] = 106
                            else:
                                bin_num[0] = 107
                    else:
                        if (feature[12]<=3.0):
                            if (feature[6]<=2.0):
                                bin_num[0] = 108
                            else:
                                bin_num[0] = 109
                        else:
                            if (feature[28]<=0.0):
                                bin_num[0] = 110
                            else:
                                bin_num[0] = 111
            else:
                if (feature[2]<=4.0):
                    if (feature[21]<=0.0):
                        if (feature[29]<=0.0):
                            if (feature[35]<=0.0):
                                bin_num[0] = 112
                            else:
                                bin_num[0] = 113
                        else:
                            if (feature[9]<=0.0):
                                bin_num[0] = 114
                            else:
                                bin_num[0] = 115
                    else:
                        if (feature[38]<=0.0):
                            if (feature[12]<=3.0):
                                bin_num[0] = 116
                            else:
                                bin_num[0] = 117
                        else:
                            if (feature[30]<=0.0):
                                bin_num[0] = 118
                            else:
                                bin_num[0] = 119
                else:
                    if (feature[24]<=0.0):
                        if (feature[12]<=3.0):
                            if (feature[35]<=0.0):
                                bin_num[0] = 120
                            else:
                                bin_num[0] = 121
                        else:
                            if (feature[21]<=0.0):
                                bin_num[0] = 122
                            else:
                                bin_num[0] = 123
                    else:
                        if (feature[31]<=0.0):
                            if (feature[6]<=2.0):
                                bin_num[0] = 124
                            else:
                                bin_num[0] = 125
                        else:
                            if (feature[21]<=0.0):
                                bin_num[0] = 126
                            else:
                                bin_num[0] = 127
    # Tree 1
    if (feature[6]<=2.0):
        if (feature[7]<=7.0):
            if (feature[13]<=0.0):
                if (feature[35]<=0.0):
                    if (feature[21]<=0.0):
                        if (feature[0]<=0.0):
                            if (feature[8]<=36.0):
                                bin_num[1] = 0
                            else:
                                bin_num[1] = 1
                        else:
                            if (feature[5]<=16.0):
                                bin_num[1] = 2
                            else:
                                bin_num[1] = 3
                    else:
                        if (feature[5]<=16.0):
                            if (feature[17]<=0.0):
                                bin_num[1] = 4
                            else:
                                bin_num[1] = 5
                        else:
                            if (feature[2]<=4.0):
                                bin_num[1] = 6
                            else:
                                bin_num[1] = 7
                else:
                    if (feature[2]<=4.0):
                        if (feature[0]<=0.0):
                            if (feature[34]<=0.0):
                                bin_num[1] = 8
                            else:
                                bin_num[1] = 9
                        else:
                            bin_num[1] = 10
                    else:
                        if (feature[37]<=0.0):
                            if (feature[26]<=0.0):
                                bin_num[1] = 11
                            else:
                                bin_num[1] = 12
                        else:
                            if (feature[31]<=0.0):
                                bin_num[1] = 13
                            else:
                                bin_num[1] = 14
            else:
                if (feature[2]<=4.0):
                    if (feature[21]<=0.0):
                        if (feature[8]<=36.0):
                            if (feature[23]<=0.0):
                                bin_num[1] = 15
                            else:
                                bin_num[1] = 16
                        else:
                            if (feature[19]<=0.0):
                                bin_num[1] = 17
                            else:
                                bin_num[1] = 18
                    else:
                        if (feature[18]<=0.0):
                            if (feature[25]<=0.0):
                                bin_num[1] = 19
                            else:
                                bin_num[1] = 20
                        else:
                            if (feature[16]<=0.0):
                                bin_num[1] = 21
                            else:
                                bin_num[1] = 22
                else:
                    if (feature[23]<=0.0):
                        if (feature[4]<=1974.0):
                            if (feature[28]<=0.0):
                                bin_num[1] = 23
                            else:
                                bin_num[1] = 24
                        else:
                            if (feature[19]<=0.0):
                                bin_num[1] = 25
                            else:
                                bin_num[1] = 26
                    else:
                        if (feature[35]<=0.0):
                            if (feature[17]<=0.0):
                                bin_num[1] = 27
                            else:
                                bin_num[1] = 28
                        else:
                            if (feature[25]<=0.0):
                                bin_num[1] = 29
                            else:
                                bin_num[1] = 30
        else:
            if (feature[4]<=1974.0):
                if (feature[19]<=0.0):
                    if (feature[20]<=0.0):
                        if (feature[32]<=0.0):
                            if (feature[13]<=0.0):
                                bin_num[1] = 31
                            else:
                                bin_num[1] = 32
                        else:
                            if (feature[36]<=0.0):
                                bin_num[1] = 33
                            else:
                                bin_num[1] = 34
                    else:
                        if (feature[15]<=0.0):
                            if (feature[35]<=0.0):
                                bin_num[1] = 35
                            else:
                                bin_num[1] = 36
                        else:
                            if (feature[28]<=0.0):
                                bin_num[1] = 37
                            else:
                                bin_num[1] = 38
                else:
                    if (feature[2]<=4.0):
                        if (feature[21]<=0.0):
                            if (feature[31]<=0.0):
                                bin_num[1] = 39
                            else:
                                bin_num[1] = 40
                        else:
                            if (feature[1]<=3.0):
                                bin_num[1] = 41
                            else:
                                bin_num[1] = 42
                    else:
                        if (feature[35]<=0.0):
                            if (feature[38]<=0.0):
                                bin_num[1] = 43
                            else:
                                bin_num[1] = 44
                        else:
                            if (feature[20]<=0.0):
                                bin_num[1] = 45
                            else:
                                bin_num[1] = 46
            else:
                if (feature[21]<=0.0):
                    if (feature[5]<=16.0):
                        if (feature[19]<=0.0):
                            if (feature[12]<=3.0):
                                bin_num[1] = 47
                            else:
                                bin_num[1] = 48
                        else:
                            if (feature[10]<=1.0):
                                bin_num[1] = 49
                            else:
                                bin_num[1] = 50
                    else:
                        if (feature[8]<=36.0):
                            if (feature[11]<=0.0):
                                bin_num[1] = 51
                            else:
                                bin_num[1] = 52
                        else:
                            if (feature[36]<=0.0):
                                bin_num[1] = 53
                            else:
                                bin_num[1] = 54
                else:
                    if (feature[17]<=0.0):
                        if (feature[26]<=0.0):
                            if (feature[18]<=0.0):
                                bin_num[1] = 55
                            else:
                                bin_num[1] = 56
                        else:
                            if (feature[19]<=0.0):
                                bin_num[1] = 57
                            else:
                                bin_num[1] = 58
                    else:
                        if (feature[2]<=4.0):
                            if (feature[10]<=1.0):
                                bin_num[1] = 59
                            else:
                                bin_num[1] = 60
                        else:
                            if (feature[30]<=0.0):
                                bin_num[1] = 61
                            else:
                                bin_num[1] = 62
    else:
        if (feature[5]<=16.0):
            if (feature[25]<=0.0):
                if (feature[22]<=0.0):
                    if (feature[8]<=36.0):
                        if (feature[27]<=0.0):
                            if (feature[24]<=0.0):
                                bin_num[1] = 63
                            else:
                                bin_num[1] = 64
                        else:
                            if (feature[11]<=0.0):
                                bin_num[1] = 65
                            else:
                                bin_num[1] = 66
                    else:
                        if (feature[34]<=0.0):
                            if (feature[24]<=0.0):
                                bin_num[1] = 67
                            else:
                                bin_num[1] = 68
                        else:
                            if (feature[31]<=0.0):
                                bin_num[1] = 69
                            else:
                                bin_num[1] = 70
                else:
                    if (feature[19]<=0.0):
                        if (feature[1]<=3.0):
                            if (feature[21]<=0.0):
                                bin_num[1] = 71
                            else:
                                bin_num[1] = 72
                        else:
                            if (feature[18]<=0.0):
                                bin_num[1] = 73
                            else:
                                bin_num[1] = 74
                    else:
                        if (feature[10]<=1.0):
                            if (feature[38]<=0.0):
                                bin_num[1] = 75
                            else:
                                bin_num[1] = 76
                        else:
                            if (feature[1]<=3.0):
                                bin_num[1] = 77
                            else:
                                bin_num[1] = 78
            else:
                if (feature[23]<=0.0):
                    if (feature[3]<=2.0):
                        if (feature[9]<=0.0):
                            if (feature[37]<=0.0):
                                bin_num[1] = 79
                            else:
                                bin_num[1] = 80
                        else:
                            if (feature[21]<=0.0):
                                bin_num[1] = 81
                            else:
                                bin_num[1] = 82
                    else:
                        if (feature[12]<=3.0):
                            if (feature[17]<=0.0):
                                bin_num[1] = 83
                            else:
                                bin_num[1] = 84
                        else:
                            if (feature[29]<=0.0):
                                bin_num[1] = 85
                            else:
                                bin_num[1] = 86
                else:
                    if (feature[29]<=0.0):
                        if (feature[21]<=0.0):
                            if (feature[27]<=0.0):
                                bin_num[1] = 87
                            else:
                                bin_num[1] = 88
                        else:
                            if (feature[24]<=0.0):
                                bin_num[1] = 89
                            else:
                                bin_num[1] = 90
                    else:
                        if (feature[10]<=1.0):
                            if (feature[7]<=7.0):
                                bin_num[1] = 91
                            else:
                                bin_num[1] = 92
                        else:
                            if (feature[38]<=0.0):
                                bin_num[1] = 93
                            else:
                                bin_num[1] = 94
        else:
            if (feature[12]<=3.0):
                if (feature[21]<=0.0):
                    if (feature[29]<=0.0):
                        if (feature[28]<=0.0):
                            if (feature[0]<=0.0):
                                bin_num[1] = 95
                            else:
                                bin_num[1] = 96
                        else:
                            if (feature[22]<=0.0):
                                bin_num[1] = 97
                            else:
                                bin_num[1] = 98
                    else:
                        if (feature[2]<=4.0):
                            if (feature[18]<=0.0):
                                bin_num[1] = 99
                            else:
                                bin_num[1] = 100
                        else:
                            if (feature[13]<=0.0):
                                bin_num[1] = 101
                            else:
                                bin_num[1] = 102
                else:
                    if (feature[18]<=0.0):
                        if (feature[35]<=0.0):
                            if (feature[24]<=0.0):
                                bin_num[1] = 103
                            else:
                                bin_num[1] = 104
                        else:
                            if (feature[26]<=0.0):
                                bin_num[1] = 105
                            else:
                                bin_num[1] = 106
                    else:
                        if (feature[17]<=0.0):
                            if (feature[31]<=0.0):
                                bin_num[1] = 107
                            else:
                                bin_num[1] = 108
                        else:
                            if (feature[4]<=1974.0):
                                bin_num[1] = 109
                            else:
                                bin_num[1] = 110
            else:
                if (feature[22]<=0.0):
                    if (feature[4]<=1974.0):
                        if (feature[29]<=0.0):
                            if (feature[10]<=1.0):
                                bin_num[1] = 111
                            else:
                                bin_num[1] = 112
                        else:
                            if (feature[20]<=0.0):
                                bin_num[1] = 113
                            else:
                                bin_num[1] = 114
                    else:
                        if (feature[1]<=3.0):
                            if (feature[32]<=0.0):
                                bin_num[1] = 115
                            else:
                                bin_num[1] = 116
                        else:
                            if (feature[21]<=0.0):
                                bin_num[1] = 117
                            else:
                                bin_num[1] = 118
                else:
                    if (feature[18]<=0.0):
                        if (feature[21]<=0.0):
                            if (feature[2]<=4.0):
                                bin_num[1] = 119
                            else:
                                bin_num[1] = 120
                        else:
                            if (feature[14]<=0.0):
                                bin_num[1] = 121
                            else:
                                bin_num[1] = 122
                    else:
                        if (feature[17]<=0.0):
                            if (feature[36]<=0.0):
                                bin_num[1] = 123
                            else:
                                bin_num[1] = 124
                        else:
                            if (feature[0]<=0.0):
                                bin_num[1] = 125
                            else:
                                bin_num[1] = 126
    # Tree 0
    if (feature[0]<=0.0):
        if (feature[10]<=1.0):
            if (feature[12]<=3.0):
                if (feature[19]<=0.0):
                    if (feature[18]<=0.0):
                        if (feature[13]<=0.0):
                            if (feature[35]<=0.0):
                                bin_num[0] = 0
                            else:
                                bin_num[0] = 1
                        else:
                            if (feature[8]<=36.0):
                                bin_num[0] = 2
                            else:
                                bin_num[0] = 3
                    else:
                        if (feature[35]<=0.0):
                            if (feature[20]<=0.0):
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
                        if (feature[2]<=4.0):
                            if (feature[7]<=7.0):
                                bin_num[0] = 8
                            else:
                                bin_num[0] = 9
                        else:
                            if (feature[13]<=0.0):
                                bin_num[0] = 10
                            else:
                                bin_num[0] = 11
                    else:
                        if (feature[35]<=0.0):
                            if (feature[5]<=14.0):
                                bin_num[0] = 12
                            else:
                                bin_num[0] = 13
                        else:
                            if (feature[6]<=2.0):
                                bin_num[0] = 14
                            else:
                                bin_num[0] = 15
            else:
                if (feature[6]<=2.0):
                    if (feature[35]<=0.0):
                        if (feature[23]<=0.0):
                            if (feature[2]<=4.0):
                                bin_num[0] = 16
                            else:
                                bin_num[0] = 17
                        else:
                            if (feature[19]<=0.0):
                                bin_num[0] = 18
                            else:
                                bin_num[0] = 19
                    else:
                        if (feature[18]<=0.0):
                            if (feature[11]<=0.0):
                                bin_num[0] = 20
                            else:
                                bin_num[0] = 21
                        else:
                            if (feature[17]<=0.0):
                                bin_num[0] = 22
                            else:
                                bin_num[0] = 23
                else:
                    if (feature[5]<=14.0):
                        if (feature[18]<=0.0):
                            if (feature[36]<=0.0):
                                bin_num[0] = 24
                            else:
                                bin_num[0] = 25
                        else:
                            if (feature[3]<=2.0):
                                bin_num[0] = 26
                            else:
                                bin_num[0] = 27
                    else:
                        if (feature[7]<=7.0):
                            if (feature[8]<=36.0):
                                bin_num[0] = 28
                            else:
                                bin_num[0] = 29
                        else:
                            if (feature[18]<=0.0):
                                bin_num[0] = 30
                            else:
                                bin_num[0] = 31
        else:
            if (feature[5]<=14.0):
                if (feature[12]<=3.0):
                    if (feature[20]<=0.0):
                        if (feature[19]<=0.0):
                            if (feature[38]<=0.0):
                                bin_num[0] = 32
                            else:
                                bin_num[0] = 33
                        else:
                            if (feature[28]<=0.0):
                                bin_num[0] = 34
                            else:
                                bin_num[0] = 35
                    else:
                        if (feature[35]<=0.0):
                            if (feature[34]<=0.0):
                                bin_num[0] = 36
                            else:
                                bin_num[0] = 37
                        else:
                            if (feature[17]<=0.0):
                                bin_num[0] = 38
                            else:
                                bin_num[0] = 39
                else:
                    if (feature[6]<=2.0):
                        if (feature[8]<=36.0):
                            if (feature[35]<=0.0):
                                bin_num[0] = 40
                            else:
                                bin_num[0] = 41
                        else:
                            if (feature[22]<=0.0):
                                bin_num[0] = 42
                            else:
                                bin_num[0] = 43
                    else:
                        if (feature[27]<=0.0):
                            if (feature[8]<=36.0):
                                bin_num[0] = 44
                            else:
                                bin_num[0] = 45
                        else:
                            if (feature[18]<=0.0):
                                bin_num[0] = 46
                            else:
                                bin_num[0] = 47
            else:
                if (feature[7]<=7.0):
                    if (feature[2]<=4.0):
                        if (feature[20]<=0.0):
                            if (feature[25]<=0.0):
                                bin_num[0] = 48
                            else:
                                bin_num[0] = 49
                        else:
                            if (feature[35]<=0.0):
                                bin_num[0] = 50
                            else:
                                bin_num[0] = 51
                    else:
                        if (feature[20]<=0.0):
                            if (feature[28]<=0.0):
                                bin_num[0] = 52
                            else:
                                bin_num[0] = 53
                        else:
                            if (feature[12]<=3.0):
                                bin_num[0] = 54
                            else:
                                bin_num[0] = 55
                else:
                    if (feature[12]<=3.0):
                        if (feature[19]<=0.0):
                            if (feature[22]<=0.0):
                                bin_num[0] = 56
                            else:
                                bin_num[0] = 57
                        else:
                            if (feature[21]<=0.0):
                                bin_num[0] = 58
                            else:
                                bin_num[0] = 59
                    else:
                        if (feature[22]<=0.0):
                            if (feature[29]<=0.0):
                                bin_num[0] = 60
                            else:
                                bin_num[0] = 61
                        else:
                            if (feature[2]<=4.0):
                                bin_num[0] = 62
                            else:
                                bin_num[0] = 63
    else:
        if (feature[5]<=14.0):
            if (feature[12]<=3.0):
                if (feature[6]<=2.0):
                    if (feature[24]<=0.0):
                        if (feature[18]<=0.0):
                            if (feature[27]<=0.0):
                                bin_num[0] = 64
                            else:
                                bin_num[0] = 65
                        else:
                            if (feature[36]<=0.0):
                                bin_num[0] = 66
                            else:
                                bin_num[0] = 67
                    else:
                        if (feature[9]<=0.0):
                            if (feature[32]<=0.0):
                                bin_num[0] = 68
                            else:
                                bin_num[0] = 69
                        else:
                            if (feature[38]<=0.0):
                                bin_num[0] = 70
                            else:
                                bin_num[0] = 71
                else:
                    if (feature[3]<=2.0):
                        if (feature[10]<=1.0):
                            if (feature[28]<=0.0):
                                bin_num[0] = 72
                            else:
                                bin_num[0] = 73
                        else:
                            if (feature[28]<=0.0):
                                bin_num[0] = 74
                            else:
                                bin_num[0] = 75
                    else:
                        if (feature[28]<=0.0):
                            if (feature[21]<=0.0):
                                bin_num[0] = 76
                            else:
                                bin_num[0] = 77
                        else:
                            if (feature[23]<=0.0):
                                bin_num[0] = 78
                            else:
                                bin_num[0] = 79
            else:
                if (feature[10]<=1.0):
                    if (feature[22]<=0.0):
                        if (feature[38]<=0.0):
                            if (feature[15]<=0.0):
                                bin_num[0] = 80
                            else:
                                bin_num[0] = 81
                        else:
                            if (feature[9]<=0.0):
                                bin_num[0] = 82
                            else:
                                bin_num[0] = 83
                    else:
                        if (feature[20]<=0.0):
                            if (feature[9]<=0.0):
                                bin_num[0] = 84
                            else:
                                bin_num[0] = 85
                        else:
                            if (feature[28]<=0.0):
                                bin_num[0] = 86
                            else:
                                bin_num[0] = 87
                else:
                    if (feature[24]<=0.0):
                        if (feature[27]<=0.0):
                            if (feature[20]<=0.0):
                                bin_num[0] = 88
                            else:
                                bin_num[0] = 89
                        else:
                            if (feature[6]<=2.0):
                                bin_num[0] = 90
                            else:
                                bin_num[0] = 91
                    else:
                        if (feature[1]<=2.0):
                            if (feature[21]<=0.0):
                                bin_num[0] = 92
                            else:
                                bin_num[0] = 93
                        else:
                            if (feature[7]<=7.0):
                                bin_num[0] = 94
                            else:
                                bin_num[0] = 95
        else:
            if (feature[10]<=1.0):
                if (feature[2]<=4.0):
                    if (feature[19]<=0.0):
                        if (feature[7]<=7.0):
                            if (feature[21]<=0.0):
                                bin_num[0] = 96
                            else:
                                bin_num[0] = 97
                        else:
                            if (feature[37]<=0.0):
                                bin_num[0] = 98
                            else:
                                bin_num[0] = 99
                    else:
                        if (feature[22]<=0.0):
                            if (feature[12]<=3.0):
                                bin_num[0] = 100
                            else:
                                bin_num[0] = 101
                        else:
                            if (feature[32]<=0.0):
                                bin_num[0] = 102
                            else:
                                bin_num[0] = 103
                else:
                    if (feature[19]<=0.0):
                        if (feature[20]<=0.0):
                            if (feature[27]<=0.0):
                                bin_num[0] = 104
                            else:
                                bin_num[0] = 105
                        else:
                            if (feature[18]<=0.0):
                                bin_num[0] = 106
                            else:
                                bin_num[0] = 107
                    else:
                        if (feature[12]<=3.0):
                            if (feature[6]<=2.0):
                                bin_num[0] = 108
                            else:
                                bin_num[0] = 109
                        else:
                            if (feature[28]<=0.0):
                                bin_num[0] = 110
                            else:
                                bin_num[0] = 111
            else:
                if (feature[2]<=4.0):
                    if (feature[21]<=0.0):
                        if (feature[29]<=0.0):
                            if (feature[35]<=0.0):
                                bin_num[0] = 112
                            else:
                                bin_num[0] = 113
                        else:
                            if (feature[9]<=0.0):
                                bin_num[0] = 114
                            else:
                                bin_num[0] = 115
                    else:
                        if (feature[38]<=0.0):
                            if (feature[12]<=3.0):
                                bin_num[0] = 116
                            else:
                                bin_num[0] = 117
                        else:
                            if (feature[30]<=0.0):
                                bin_num[0] = 118
                            else:
                                bin_num[0] = 119
                else:
                    if (feature[24]<=0.0):
                        if (feature[12]<=3.0):
                            if (feature[35]<=0.0):
                                bin_num[0] = 120
                            else:
                                bin_num[0] = 121
                        else:
                            if (feature[21]<=0.0):
                                bin_num[0] = 122
                            else:
                                bin_num[0] = 123
                    else:
                        if (feature[31]<=0.0):
                            if (feature[6]<=2.0):
                                bin_num[0] = 124
                            else:
                                bin_num[0] = 125
                        else:
                            if (feature[21]<=0.0):
                                bin_num[0] = 126
                            else:
                                bin_num[0] = 127
    # Tree 1
    if (feature[6]<=2.0):
        if (feature[7]<=7.0):
            if (feature[13]<=0.0):
                if (feature[35]<=0.0):
                    if (feature[21]<=0.0):
                        if (feature[0]<=0.0):
                            if (feature[8]<=36.0):
                                bin_num[1] = 0
                            else:
                                bin_num[1] = 1
                        else:
                            if (feature[5]<=16.0):
                                bin_num[1] = 2
                            else:
                                bin_num[1] = 3
                    else:
                        if (feature[5]<=16.0):
                            if (feature[17]<=0.0):
                                bin_num[1] = 4
                            else:
                                bin_num[1] = 5
                        else:
                            if (feature[2]<=4.0):
                                bin_num[1] = 6
                            else:
                                bin_num[1] = 7
                else:
                    if (feature[2]<=4.0):
                        if (feature[0]<=0.0):
                            if (feature[34]<=0.0):
                                bin_num[1] = 8
                            else:
                                bin_num[1] = 9
                        else:
                            bin_num[1] = 10
                    else:
                        if (feature[37]<=0.0):
                            if (feature[26]<=0.0):
                                bin_num[1] = 11
                            else:
                                bin_num[1] = 12
                        else:
                            if (feature[31]<=0.0):
                                bin_num[1] = 13
                            else:
                                bin_num[1] = 14
            else:
                if (feature[2]<=4.0):
                    if (feature[21]<=0.0):
                        if (feature[8]<=36.0):
                            if (feature[23]<=0.0):
                                bin_num[1] = 15
                            else:
                                bin_num[1] = 16
                        else:
                            if (feature[19]<=0.0):
                                bin_num[1] = 17
                            else:
                                bin_num[1] = 18
                    else:
                        if (feature[18]<=0.0):
                            if (feature[25]<=0.0):
                                bin_num[1] = 19
                            else:
                                bin_num[1] = 20
                        else:
                            if (feature[16]<=0.0):
                                bin_num[1] = 21
                            else:
                                bin_num[1] = 22
                else:
                    if (feature[23]<=0.0):
                        if (feature[4]<=1974.0):
                            if (feature[28]<=0.0):
                                bin_num[1] = 23
                            else:
                                bin_num[1] = 24
                        else:
                            if (feature[19]<=0.0):
                                bin_num[1] = 25
                            else:
                                bin_num[1] = 26
                    else:
                        if (feature[35]<=0.0):
                            if (feature[17]<=0.0):
                                bin_num[1] = 27
                            else:
                                bin_num[1] = 28
                        else:
                            if (feature[25]<=0.0):
                                bin_num[1] = 29
                            else:
                                bin_num[1] = 30
        else:
            if (feature[4]<=1974.0):
                if (feature[19]<=0.0):
                    if (feature[20]<=0.0):
                        if (feature[32]<=0.0):
                            if (feature[13]<=0.0):
                                bin_num[1] = 31
                            else:
                                bin_num[1] = 32
                        else:
                            if (feature[36]<=0.0):
                                bin_num[1] = 33
                            else:
                                bin_num[1] = 34
                    else:
                        if (feature[15]<=0.0):
                            if (feature[35]<=0.0):
                                bin_num[1] = 35
                            else:
                                bin_num[1] = 36
                        else:
                            if (feature[28]<=0.0):
                                bin_num[1] = 37
                            else:
                                bin_num[1] = 38
                else:
                    if (feature[2]<=4.0):
                        if (feature[21]<=0.0):
                            if (feature[31]<=0.0):
                                bin_num[1] = 39
                            else:
                                bin_num[1] = 40
                        else:
                            if (feature[1]<=3.0):
                                bin_num[1] = 41
                            else:
                                bin_num[1] = 42
                    else:
                        if (feature[35]<=0.0):
                            if (feature[38]<=0.0):
                                bin_num[1] = 43
                            else:
                                bin_num[1] = 44
                        else:
                            if (feature[20]<=0.0):
                                bin_num[1] = 45
                            else:
                                bin_num[1] = 46
            else:
                if (feature[21]<=0.0):
                    if (feature[5]<=16.0):
                        if (feature[19]<=0.0):
                            if (feature[12]<=3.0):
                                bin_num[1] = 47
                            else:
                                bin_num[1] = 48
                        else:
                            if (feature[10]<=1.0):
                                bin_num[1] = 49
                            else:
                                bin_num[1] = 50
                    else:
                        if (feature[8]<=36.0):
                            if (feature[11]<=0.0):
                                bin_num[1] = 51
                            else:
                                bin_num[1] = 52
                        else:
                            if (feature[36]<=0.0):
                                bin_num[1] = 53
                            else:
                                bin_num[1] = 54
                else:
                    if (feature[17]<=0.0):
                        if (feature[26]<=0.0):
                            if (feature[18]<=0.0):
                                bin_num[1] = 55
                            else:
                                bin_num[1] = 56
                        else:
                            if (feature[19]<=0.0):
                                bin_num[1] = 57
                            else:
                                bin_num[1] = 58
                    else:
                        if (feature[2]<=4.0):
                            if (feature[10]<=1.0):
                                bin_num[1] = 59
                            else:
                                bin_num[1] = 60
                        else:
                            if (feature[30]<=0.0):
                                bin_num[1] = 61
                            else:
                                bin_num[1] = 62
    else:
        if (feature[5]<=16.0):
            if (feature[25]<=0.0):
                if (feature[22]<=0.0):
                    if (feature[8]<=36.0):
                        if (feature[27]<=0.0):
                            if (feature[24]<=0.0):
                                bin_num[1] = 63
                            else:
                                bin_num[1] = 64
                        else:
                            if (feature[11]<=0.0):
                                bin_num[1] = 65
                            else:
                                bin_num[1] = 66
                    else:
                        if (feature[34]<=0.0):
                            if (feature[24]<=0.0):
                                bin_num[1] = 67
                            else:
                                bin_num[1] = 68
                        else:
                            if (feature[31]<=0.0):
                                bin_num[1] = 69
                            else:
                                bin_num[1] = 70
                else:
                    if (feature[19]<=0.0):
                        if (feature[1]<=3.0):
                            if (feature[21]<=0.0):
                                bin_num[1] = 71
                            else:
                                bin_num[1] = 72
                        else:
                            if (feature[18]<=0.0):
                                bin_num[1] = 73
                            else:
                                bin_num[1] = 74
                    else:
                        if (feature[10]<=1.0):
                            if (feature[38]<=0.0):
                                bin_num[1] = 75
                            else:
                                bin_num[1] = 76
                        else:
                            if (feature[1]<=3.0):
                                bin_num[1] = 77
                            else:
                                bin_num[1] = 78
            else:
                if (feature[23]<=0.0):
                    if (feature[3]<=2.0):
                        if (feature[9]<=0.0):
                            if (feature[37]<=0.0):
                                bin_num[1] = 79
                            else:
                                bin_num[1] = 80
                        else:
                            if (feature[21]<=0.0):
                                bin_num[1] = 81
                            else:
                                bin_num[1] = 82
                    else:
                        if (feature[12]<=3.0):
                            if (feature[17]<=0.0):
                                bin_num[1] = 83
                            else:
                                bin_num[1] = 84
                        else:
                            if (feature[29]<=0.0):
                                bin_num[1] = 85
                            else:
                                bin_num[1] = 86
                else:
                    if (feature[29]<=0.0):
                        if (feature[21]<=0.0):
                            if (feature[27]<=0.0):
                                bin_num[1] = 87
                            else:
                                bin_num[1] = 88
                        else:
                            if (feature[24]<=0.0):
                                bin_num[1] = 89
                            else:
                                bin_num[1] = 90
                    else:
                        if (feature[10]<=1.0):
                            if (feature[7]<=7.0):
                                bin_num[1] = 91
                            else:
                                bin_num[1] = 92
                        else:
                            if (feature[38]<=0.0):
                                bin_num[1] = 93
                            else:
                                bin_num[1] = 94
        else:
            if (feature[12]<=3.0):
                if (feature[21]<=0.0):
                    if (feature[29]<=0.0):
                        if (feature[28]<=0.0):
                            if (feature[0]<=0.0):
                                bin_num[1] = 95
                            else:
                                bin_num[1] = 96
                        else:
                            if (feature[22]<=0.0):
                                bin_num[1] = 97
                            else:
                                bin_num[1] = 98
                    else:
                        if (feature[2]<=4.0):
                            if (feature[18]<=0.0):
                                bin_num[1] = 99
                            else:
                                bin_num[1] = 100
                        else:
                            if (feature[13]<=0.0):
                                bin_num[1] = 101
                            else:
                                bin_num[1] = 102
                else:
                    if (feature[18]<=0.0):
                        if (feature[35]<=0.0):
                            if (feature[24]<=0.0):
                                bin_num[1] = 103
                            else:
                                bin_num[1] = 104
                        else:
                            if (feature[26]<=0.0):
                                bin_num[1] = 105
                            else:
                                bin_num[1] = 106
                    else:
                        if (feature[17]<=0.0):
                            if (feature[31]<=0.0):
                                bin_num[1] = 107
                            else:
                                bin_num[1] = 108
                        else:
                            if (feature[4]<=1974.0):
                                bin_num[1] = 109
                            else:
                                bin_num[1] = 110
            else:
                if (feature[22]<=0.0):
                    if (feature[4]<=1974.0):
                        if (feature[29]<=0.0):
                            if (feature[10]<=1.0):
                                bin_num[1] = 111
                            else:
                                bin_num[1] = 112
                        else:
                            if (feature[20]<=0.0):
                                bin_num[1] = 113
                            else:
                                bin_num[1] = 114
                    else:
                        if (feature[1]<=3.0):
                            if (feature[32]<=0.0):
                                bin_num[1] = 115
                            else:
                                bin_num[1] = 116
                        else:
                            if (feature[21]<=0.0):
                                bin_num[1] = 117
                            else:
                                bin_num[1] = 118
                else:
                    if (feature[18]<=0.0):
                        if (feature[21]<=0.0):
                            if (feature[2]<=4.0):
                                bin_num[1] = 119
                            else:
                                bin_num[1] = 120
                        else:
                            if (feature[14]<=0.0):
                                bin_num[1] = 121
                            else:
                                bin_num[1] = 122
                    else:
                        if (feature[17]<=0.0):
                            if (feature[36]<=0.0):
                                bin_num[1] = 123
                            else:
                                bin_num[1] = 124
                        else:
                            if (feature[0]<=0.0):
                                bin_num[1] = 125
                            else:
                                bin_num[1] = 126
    
    return bin_num

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

def run_bins(input_file,output_file):
    #repeat of before to generate OHETrainDataBins
    dataRDD=sc.textFile(input_file).map(lambda x: x.replace('\t',','))
    dataRDDParsed=dataRDD.map(parsePoint).cache()
    featSet=dataRDDParsed.flatMap(lambda x: x).map(maaro).reduceByKey(lambda a,b: a+b).takeOrdered(26,lambda (k,v): -v)
    OHEdict={}
    for i,x in enumerate(featSet):
        OHEdict[x[0]]=i
    OHETrainData = dataRDD.map(lambda point: parseOHEPoint(point, OHEdict, 39))
    
    #apply the new decision tree
    OHETrainDataDense = OHETrainData.map(lambda x: SparseVector.toArray(x.features))
    OHETrainDataBins = OHETrainDataDense.map(lambda x: get_bins(x))
    OHETrainDataBins.coalesce(1).saveAsTextFile(output_file)


if __name__== '__main__':
    
    if len(sys.argv) < 2:
        print >> sys.stderr, "Usage: page_rank <initialize sc ?> <input file> <output file> <damping factor> <number_of_iterations>"
        exit(-1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    sc = SparkContext(appName="GBDT2")
    run_bins(input_file,output_file)
    sc.stop()