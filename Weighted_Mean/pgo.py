# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())

x = list(map(int, input().split()))
y = list(map(int, input().split()))

tot = 0
ytot = 0


for i in range(n):
    #print(i)
    tot += x[i]*y[i]
    ytot += y[i]

ans = round(tot/float(ytot),1)

print(ans)
