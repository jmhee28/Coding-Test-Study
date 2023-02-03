def solution(s):
    # 배열 형태로 저장 후 길이순으로 정렬     
    # {{1,2,3},{2,1},{1,2,4,3},{2}} 를
    # [['2'], ['2', '1'], ['1', '2', '3'], ['1', '2', '4', '3']] 으로 변환
    ls = sorted([s.split(',') for s in s[2:-2].split('},{')], key=len)
    
    answer = []
    # 반복문을 돌며 answer에 새로운 원소 추가
    for l in ls:
        for s in l:
            if int(s) not in answer:
                answer.append(int(s))
                break
    return answer
