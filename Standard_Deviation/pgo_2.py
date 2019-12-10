# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

n = int(input())

x = list(map(int, input().split()))

#print(n)
#print(x)

tot = 0
mean = sum(x) / n

for i in range(n):
    tot += (x[i]-mean)**2

ans = math.sqrt(tot/n)

print(ans)
