n = int(input())
x = list(map(int,input().split()))
w = list(map(int,input().split()))

weighted=0
for i in range(n):
    weighted += x[i]*w[i]
res = weighted/sum(w)
print("{:.1f}".format(res))