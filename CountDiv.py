# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B, K):
    # write your code in Python 3.6
    ans =  B//K - A//K 
    if A % K == 0: ans += 1
    return ans
