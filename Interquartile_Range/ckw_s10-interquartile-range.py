#기본 개념:

#interquantile range: Q1 - Q3

#조건
#X: 배열
#F: X의 원소의 빈도

import math
from statistics import median

def interquantile(X, F):
    


#    for i in range(len(X)-1):
#        for j in range(F[i]-1):
#            X.append(X[j])

    X = sorted(X)
    return(X)
#    X = sorted(X)

X = [6, 12, 8, 10, 20, 16] #Array
F = [5, 4, 3, 2, 1, 5] #Frequency

for i in range(len(F)):
    print(X[i])
    print(F[i])
print(interquantile(X, F))