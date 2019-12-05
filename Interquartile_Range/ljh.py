from statistics import median
# import numpy as np
n = int(input())
x = list(map(int,input().split()))
f = list(map(int,input().split()))

elist = []
for i in range(n):
    elist += [x[i] for _ in range(f[i])]
elist = sorted(elist)
print(elist)
print(len(elist))
print(elist[:(len(elist)//2)])
print(elist[(len(elist)//2)+1:])
q1 = median(elist[:(len(elist)//2)])
if len(elist)%2==0:
    q3 = median(elist[len(elist)//2:])
else:
    q3 = median(elist[(len(elist)//2)+1:])

print(float(q3-q1))