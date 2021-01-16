# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, A):
    # write your code in Python 3.6
    answers = [0] * N
    max_num = 0
    min_num = 0
    for query in A:
        if query == N + 1: min_num = max_num
        else:
            idx = query - 1
            answers[idx] = max(min_num + 1, answers[idx] + 1)
            max_num = max(max_num, answers[idx])
    for i,_ in enumerate(answers):
        answers[i] = max(answers[i], min_num)
    return answers
