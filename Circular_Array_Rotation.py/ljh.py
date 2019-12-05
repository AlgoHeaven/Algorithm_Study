from queue import deque

nkq = input().split()
n,k,q = int(nkq[0]),int(nkq[1]),int(nkq[2])
a = list(map(int, input().rstrip().split()))
queries = []
for _ in range(q):
    queries_item = int(input())
    queries.append(queries_item)

que = deque()
for num in a:
    que.append(num)
que.rotate(k)

for q in queries:
    print(que[q])
