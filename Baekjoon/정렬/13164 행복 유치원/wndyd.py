import sys
lst = list()
sum = 0
N, K = sys.stdin.readline().split()
N, K = int(N), int(K)
members = list(map(int, sys.stdin.readline().split()))
for i in range(len(members)-1):
    lst.append(members[i+1]-members[i])
lst = sorted(lst, reverse=True)
for i in lst[(K-1):]:
    sum += i

print(sum)