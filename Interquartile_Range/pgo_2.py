# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())

x = [int(i) for i in input().split()]

f = [int(i) for i in input().split()]

data = []

for i in range(n):
    v = x[i]
    frequency = f[i]
    for j in range(frequency):
        data.append(v)

data = sorted(data)
#print(data)

def median(x):
    len_x = len(x)

    if len_x % 2 == 0:
        return (x[int(len_x/2)-1] + x[int(len_x/2)])//2
    else:
        return x[int(len_x/2)]

def quartile(x,n):
    fst = median(x[:n//2])
    snd = median(x)

    if n%2 == 0:
        trd = median(x[n//2:])
    else:
        trd = median(x[n//2+1:])
    return fst,snd,trd

Q1,Q2,Q3=quartile(data,n)

print(Q3)
print(Q1)

iqr = float(Q3 - Q1)

print(iqr)
