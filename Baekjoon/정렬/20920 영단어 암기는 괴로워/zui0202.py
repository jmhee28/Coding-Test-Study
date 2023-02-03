import sys

input = sys.stdin.readline

N, M = map(int, input().split())
voca = {}

for _ in range(N):
    word = input().strip()
    
    # 단어의 길이가 M 미만인 경우     
    if len(word) < M:
        # 단어장에 추가하지 않음        
        continue
    # 단어의 길이가 M 이상인 경우
    else:   
        # 단어가 단어장에 있다면
        if word in voca:
            # 횟수 1 증가
            voca[word] += 1
        else:
            # 횟수 1 정의
            voca[word] = 1

# 우선순위대로 정렬
# 빈출단어(-x[1]), 길이가 긴 순(-len(x[0])), 단어사전순(x[0])
voca = sorted(voca.items(), key = lambda x : (-x[1], -len(x[0]), x[0]))

for i in voca:
    print(i[0])
