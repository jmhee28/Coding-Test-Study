import sys
from collections import Counter
word_list = []
result = []
N, L = sys.stdin.readline().split()
N, L = int(N), int(L)
for i in range(N):
    word = sys.stdin.readline().strip()
    if len(word) >= L:
        word_list.append(word)

sorted_word_list = sorted(word_list)
sorted_word_list = sorted(sorted_word_list, key=len, reverse=True)
MC = Counter(sorted_word_list).most_common()
for mc in MC:
    print(mc[0])