# Enter your code here. Read input from STDIN. Print output to STDOUT

# import numpy as np
# from scipy import stats

# n = int(input())

# data = list(map(int, input().split()))
# print(np.mean(data))
# print(np.median(data))
# print(int(stats.mode(data)[0]))


def Mean(data):
    sum = 0
    
    for i in data:
        sum += i
    
    mean = float(sum) / len(data)

    return mean

def Median(data):
    median = 0.0
    size = len(data)
    data_copy = data.copy()
    data_copy.sort()

    if size % 2 == 0:
        median = float(data_copy[size//2 - 1] +
                       data_copy[size//2]) / 2
    else:
        median = data_copy[int((size-1)/2)]

    return median

def Mode(data):
    mode = 0
    count = 0
    maxv = 0
    data_copy = data.copy()
    data_copy.sort()
    current = 0

    for i in data_copy:
        if i == current:
            count += 1
        else:
            count = 1
            current = i
        
        if count > maxv:
            maxv = count
            mode = i
    
    return mode

size = int(input())
data = list(map(int, input().split()))

print(Mean(data))
print(Median(data))
print(Mode(data))
