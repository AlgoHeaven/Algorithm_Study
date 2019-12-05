n,k = map(int,input().split())
alist = list(map(int,input().split()))

for a in alist:
    print(a)
    if a <= 0:
        k -= 1
if k <= 0: print("NO")
else: print("YES")
