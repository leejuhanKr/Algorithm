def solution(my_string):
    return "".join(j for i,j in enumerate(my_string) if my_string.find(j) == i)