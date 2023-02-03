import sys

input = sys.stdin.readline

N, K = map(int, input().split())

# 원생들의 키 저장
# [1, 3, 5, 6, 10]
heights = list(map(int, input().split()))

# 원생들의 키 차이 저장
# [2, 2, 1, 4]
diff = []

for i in range(1, N):
    diff.append(heights[i] - heights[i-1])

# 키 차이가 큰 순으로 정렬
# [4, 2, 2, 1]
diff.sort(reverse=True)

# 큰 차이를 보이는 구간을 다른 조로 구분하는 것이 가장 효율적
# K개의 조로 구분한다면, K-1개의 구간을 선택할 수 있음
# 나머지 차이들을 모두 합한 것이 최소 비용
ans = sum(diff[K-1:])

print(ans)
