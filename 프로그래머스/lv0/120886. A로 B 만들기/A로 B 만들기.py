from collections import Counter
def solution(before, after):
    return +(Counter(before) == Counter(after))