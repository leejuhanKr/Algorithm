from collections import Counter

def solution(s):
    return ''.join(sorted(i for i,j in Counter(s).items() if j==1))