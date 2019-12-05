x1V1X2V2 = input().split()
x1 = int(x1V1X2V2[0])
v1 = int(x1V1X2V2[1])
x2 = int(x1V1X2V2[2])
v2 = int(x1V1X2V2[3])

def kangaroo(x1, v1, x2, v2):
    if v2>=v1: return "NO"
    if (x1-x2)%(v2-v1)==0: return "YES"
    else: return "NO"
print(kangaroo(x1,v1,x2,v2))
