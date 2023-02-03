def head_sort(file):
    for i in range(len(file)):
        if file[i].isdigit():
            head = file[:i]
            head = head.lower()
            return head
def number_sort(file):
    for i in range(len(file)):
        if file[i].isdigit():
            after_head = file[i:]
            break
    for i in range(len(after_head)):
        if i == len(after_head)-1:
            number = after_head[:i+1]
            return int(number)
        if not after_head[i].isdigit():
            number = after_head[:i]
            return int(number)


def solution(files):
    answer = sorted(files, key=number_sort)
    answer = sorted(answer, key=head_sort)
    return answer
