# 안테나를 중앙값에 위치한 집에 설치했을 때 최소비용을 가짐
# 즉, 정렬 후 중앙값을 구하는 문제
n = int(input())
a = list(map(int, input().split()))

a.sort()
print(a[(n-1)//2])
