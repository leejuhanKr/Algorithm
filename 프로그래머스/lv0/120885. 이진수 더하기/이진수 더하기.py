def solution(*b):
    return bin(sum(map(lambda x: int(x,2), b)))[2:]