def solution(order):
    return sum(i in '369' for i in str(order))