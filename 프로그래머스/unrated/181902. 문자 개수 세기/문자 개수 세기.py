from collections import Counter

def solution(my_string):
    cnt = Counter(my_string)
    return [
        cnt[chr(i)]
        for i in (*range(ord('A'),ord('Z')+1),*range(ord('a'),ord('z')+1))
    ]