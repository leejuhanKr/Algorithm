from collections import deque

def solution(A, B):
    a,b = map(deque, (A,B))
    for i in range(len(A)):
        if list(a) == list(b):
            return i
        a.rotate()
    return -1
