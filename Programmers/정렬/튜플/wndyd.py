from collections import Counter
import re
def solution(s):
    answer = []
    p = re.compile("[0-9]+")
    m = re.findall(p, s)
    mc = Counter(m).most_common()
    for i in mc:
        answer.append(int(i[0]))
    return answer