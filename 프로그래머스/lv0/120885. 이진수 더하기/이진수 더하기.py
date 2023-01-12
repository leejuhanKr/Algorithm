def solution(*b):
    return format(sum(map(lambda x: int(x,2), b)),'b')