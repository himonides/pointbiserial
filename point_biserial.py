# Point-Biserial Correlation
# based on Bruning & Kintz,
# Computational Handbook of Statistics
# by Dr Evangelos Himonides, for Dr Desmond Sergeant

#enforce proper floating point division
from __future__ import division

#import square root function
from math import sqrt

#import csv library
import csv

reader = csv.reader(open("matrix.csv", "rb"), delimiter=',')
matrix = []
i = 0
j = 0
for row in reader:
    matrix.append(row)
while i < len(matrix):
    matrix[i][0]=int(matrix[i][0])
    matrix[i][1]=int(matrix[i][1])    
    i = i + 1

#Step 3a --- compute mean of group 1 (the ones)
def OneMeans(matrix):
    m = 0
    n = 0
    i = 0
    result = 0.0
    while i < len(matrix):
        if matrix[i][1] == 1:
            m = m + matrix[i][0]
            n = n + 1
        i = i + 1
    result = m / n
    return result

#Step 3b --- compute mean of group 2 (the zeroes)
def ZeroMeans(matrix):
    o = 0
    p = 0
    j = 0
    result = 0.0
    while j < len(matrix):
        if matrix[j][1] == 0:
            o = o + matrix[j][0]
            p = p + 1
        j = j + 1
    result = o / p
    return result

#Step 4 --- Ybar1 - Ybar2
def Step4(matrix):
    s4 = 0.0
    s4 = OneMeans(matrix) - ZeroMeans(matrix)
    return s4

#Step 5 ---
def Step5(matrix):
    n_one = 0
    n_zero = 0
    n = 0.0
    i = 0
    result5 = 0.0
    while i < len(matrix):
        if matrix[i][1] == 0:
            n_zero = n_zero + 1
        elif matrix[i][1] == 1:
            n_one = n_one + 1
        else:
            pass
        i = i + 1
    n = n_zero + n_one
    result5 = sqrt((n_one*n_zero)/(n*(n-1)))
    return result5

#Step 6 --- Sum of squares of all examination points
def Step6(matrix):
    i = 0
    sq = 0
    while i < len(matrix):
        sq = sq + (matrix[i][0])** 2
        i = i + 1
    return sq

#Step 7 --- Step 6 x N
def Step7(matrix):
    result = Step6(matrix) * len(matrix)
    return result

#Step 8 --- Add all examination scores
def Step8(matrix):
    i = 0
    sum = 0
    while i < len(matrix):
        sum = sum + matrix[i][0]
        i = i + 1
    return sum

#Step 9 --- Square step 8 value
def Step9(matrix):
    result = Step8(matrix)**2
    return result

#Step 10 --- Subtract the result of step 9 form the result of step 7
def Step10(matrix):
    result = Step7(matrix) - Step9(matrix)
    return result

#Step 11 --- Divide the result of Step 10 by N(N-1)
def Step11(matrix):
    n = len(matrix)
    result = Step10(matrix)/(n*(n-1))
    return result

#Step 12 --- Square root of step 11 result
def Step12(matrix):
    result = sqrt(Step11(matrix))
    return result

#Step 13 --- Divide the result of step 4 by result of step 12
def Step13(matrix):
    result = Step4(matrix)/Step12(matrix)
    return result

#Step 14 --- Multiply step 13 result by Step 5 result
def pointbiserial(matrix):
    result = Step13(matrix) * Step5(matrix)
    return result

#Supplement --- T value calculation
def Tvalue(matrix):
    n = len(matrix)
    result = pointbiserial(matrix) * sqrt((n-2)/(1-(pointbiserial(matrix))**2))
    return result

#Report
print "Request for Point Biserial Correlation coefficient calculation"
print "for the following matrix of numbers:"
print "-----------------------------------------------------------"
z = 0
while z < len(matrix):
    print matrix[z][0],',',matrix[z][1]
    z = z + 1
print "-----------------------------------------------------------"
print "mean of group 1 (the ones): ", OneMeans(matrix)
print "mean of group 2 (the zeroes): ", ZeroMeans(matrix)
print "Ybar1 - Ybar2: ", Step4(matrix)
print "Step 5: ", Step5(matrix)
print "Step 6: ", Step6(matrix)
print "Step 7: ", Step7(matrix)
print "Step 8: ", Step8(matrix)
print "Step 9: ", Step9(matrix)
print "Step 10: ", Step10(matrix)
print "Step 11: ", Step11(matrix)
print "Step 12: ", Step12(matrix)
print "Step 13: ", Step13(matrix)
print "-----------------------------------------------------------"
print "Point Biserial correlation rpb = ", pointbiserial(matrix)
print "T-Test t value for testing significance: ", Tvalue(matrix)
print "-----------------------------------------------------------"
print "Above 3 degrees of freedom, any t value greater than -+3.18"
print "is significant at the .05 level using a two-tailed test...."
