from functools import reduce
def solution(num_list):
    return reduce(lambda a,c: [a[0]+(c+1)%2, a[1]+ c%2], num_list, [0,0])