from statistics import median
from collections import Counter
n = int(input())
x = list(map(int,input().split()))
print(sum(x)/n)
print(median(x))
count = Counter(x)
maxval = max(count.values())
temp = []
for k,v in count.items():
    if v==maxval:
        temp.append(k)
print(min(temp))