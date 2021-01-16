# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    cnt_dic = {}
    N = len(A)
    for i,num in enumerate(A):
        if num not in cnt_dic:
            cnt_dic[num] = 1
        else:
            cnt_dic[num] += 1
        if cnt_dic[num] * 2 > N:
            return i
    return -1
