import sys
n = int(sys.stdin.readline())
arr =list(map(int, sys.stdin.readline().split()))

arr.sort()
avg = (arr[n-1]-arr[0])//2
median = (n-1)//2

print(arr[median])
