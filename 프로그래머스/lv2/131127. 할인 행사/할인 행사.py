from collections import Counter

def solution(want, number, discount):
    dic = Counter(dict(zip(want,number)))
    return sum(
        dic == Counter(discount[i:i+10]) 
        for i in range(len(discount)-9)
    )