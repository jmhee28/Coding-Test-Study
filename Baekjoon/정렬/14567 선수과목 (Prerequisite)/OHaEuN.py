import sys
import collections

n,m = map(int,sys.stdin.readline().split())
count = [0 for _ in range(n + 1)]
res = [0 for _ in range(n + 1)]
dq= collections.deque()
arr = collections.defaultdict(list)

for i in range(m):
    a, b = map(int,sys.stdin.readline().split())
    arr[a].append(b)
    res[b]+=1

for i in range(1,n+1):
    if res[i]==0:
        dq.append((i,1))
        count[i]=1

while dq:
    a, cnt = dq.popleft()
    for i in arr[a]:
        res[i] -=1
        if res[i] == 0:
            dq.append((i,cnt+1))
            count[i] = cnt+1

print(*count[1:])
