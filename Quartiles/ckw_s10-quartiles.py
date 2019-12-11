###기본 개념: https://m.blog.naver.com/PostView.nhn?blogId=istech7&logNo=50152009300&proxyReferer=https%3A%2F%2Fwww.google.com%2F

#quartile:'등위' 개념.   first/second/third/fourth quantile
#1분위수: 전체 원소의 중앙값을 기준으로 좌측 원소들의 중앙값.
#2분위수: 전체 원소의 중앙값.
#3분위수: 전체 원소의 중앙값을 기준으로 우측 원소들의 중앙값.
#quantile:'백분율' 개념.  25% /  50% / 75% / 100% quartile 
##########################################################################
###문제 조건.

#X: 배열
#n: 정수형
#정수형인 1분위수, 2분위수, 3분위수를 각각 구하라.

#input format: 배열의 원소 개수(n), 공간으로 띄워진 n개의 원소값
#output format: Q1값, Q2값, Q3값 순으로 출력
# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
from statistics import median

def Q1(x, n):
    #First, sort the array 'x'.
    for i in range(n-1):
        min_idx = i
        for j in range(i, n):
            if x[j] < x[min_idx]:
                min_idx = j
        x[i], x[min_idx] = x[min_idx], x[i]

    #Second, divide array 'x' by the median(x).
    half_list = []
    for i in range(0, math.floor(n/2)):
        half_list.append(x[i])

    #Result: easy version
    return int(median(half_list))
    #Result: hard version
#    if len(half_list)%2 == 0:
#        return int(half_list[len(half_list)//2 - 1] + half_list[len(half_list)//2]) // 2
#    else:
#        return half_list[len(half_list)//2]


def Q2(x, n):
    for i in range(n-1):
        min_idx = i
        for j in range(i, n):
            if x[j] < x[min_idx]:
                min_idx = j
        x[i], x[min_idx] = x[min_idx], x[i]

    if n%2 == 0:
        return (x[len(x)//2 - 1] + x[len(x)/2]) // 2
    else:
        return x[len(x)//2]

def Q3(x, n):
    for i in range(n-1):
        min_idx = i
        for j in range(i, n):
            if x[j] < x[min_idx]:
                min_idx = j
        x[i], x[min_idx] = x[min_idx], x[i]

    half_list = []
    for i in range(math.ceil(n/2), n):
        half_list.append(x[i])

    if len(half_list)%2 == 0:
        return (half_list[len(half_list)//2 - 1] + half_list[len(half_list)//2]) // 2
    else:
        return half_list[len(half_list)//2]

array = [3, 7, 8, 5, 12, 14, 21, 13, 18]
num = 9

print(Q1(array, num))
print(Q2(array, num))
print(Q3(array, num))