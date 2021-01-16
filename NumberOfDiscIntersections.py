# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    N = len(A)
    if N <= 1: return 0

    start_list = []
    end_list = []
    for i, radius in enumerate(A):
        left, right = i - radius, i + radius
        start_list.append(left)
        end_list.append(right)
    start_list.sort()
    end_list.sort()

    cur_started = 0
    idx_stt = 0; idx_end = 0
    ans = 0
    while idx_stt < N:
        stt = start_list[idx_stt]; end = end_list[idx_end]
        if stt <= end:
            ans += cur_started
            cur_started += 1
            idx_stt += 1
        else:
            cur_started -= 1
            idx_end += 1
            
    if ans > 10_000_000:
        return -1
    else:
        return ans
