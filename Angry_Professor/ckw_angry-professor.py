
#첫 줄
#n: 학생 수(size of a) a[i]<= 0 정시 도착   a>0 == a[i]분만큼 지각
#k: 수업을 진행할 최소 학생 수(cancellation threshold)

#둘째 줄
#n: 각 학생의 도착시간

#input data
#k, a
import math
import os
import random
import re
import sys

# Complete the angryProfessor function below.
def angryProfessor(k, a):

    late = []  #Counting the number of students those who are late for class.
    for i in range(len(a)):
        if a[i]>0:
            late.append(a[i])
    
    if len(late) < k:
        return 'YES'    #Class is canceled.
    else:
        return 'NO'     #Class is not canceled.

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())

    for t_itr in range(t):
        nk = input().split()
        n = int(nk[0])
        k = int(nk[1])
        a = list(map(int, input().rstrip().split()))
        result = angryProfessor(k, a)
    
        fptr.write(result + '\n')
    fptr.close()

