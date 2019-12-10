# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
x = sorted(map(int, input().split()))

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

Q1,Q2,Q3=quartile(x,n)

print(Q1)
print(Q2)
print(Q3)
