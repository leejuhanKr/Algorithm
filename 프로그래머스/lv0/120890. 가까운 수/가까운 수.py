def solution(array, n):
    return sorted(array, key=lambda x: (abs(x-n),x))[0]