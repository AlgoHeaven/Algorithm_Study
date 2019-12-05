n = int(input())
q = list(map(int,input().split()))
q = sorted(q)

def find_median(qlist):
    if len(qlist)%2!=0:
        return qlist[len(qlist)//2]
    else:
        return (qlist[(len(qlist)//2)-1] + qlist[len(qlist)//2])/2

q1 = find_median(q[:len(q)//2])
q2 = find_median(q)
if n%2!=0:
    q3 = find_median(q[(len(q)//2)+1:])
else:
    q3 = find_median(q[len(q)//2:])
    
print(int(q1))
print(int(q2))
print(int(q3))
