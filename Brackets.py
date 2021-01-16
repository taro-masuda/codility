# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    N = len(S)
    if N == 0: return 1 # True
    elif N == 1: return 0 # False

    stack = []
    for char in S:
        if char == '(' or char == '{' or char == '[':
            stack.append(char)
        else:
            if len(stack) == 0: return 0
            elif char == ')':
                if stack[-1] == '(': stack.pop(-1)
                else: return 0
            elif char == '}':
                if stack[-1] == '{': stack.pop(-1)
                else: return 0
            else:
                if stack[-1] == '[': stack.pop(-1)
                else: return 0
    if len(stack) == 0: return 1
    else: return 0
