n = int(input())
x = list(map(int,input().split()))
mean = sum(x)/n
diff = 0
for val in x:
    diff += (val-mean)**2
devi = (diff/n)**0.5
print(devi)