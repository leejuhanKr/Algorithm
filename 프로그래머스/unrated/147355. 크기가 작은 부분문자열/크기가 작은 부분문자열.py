def solution(t, p):
    num_len = len(p)
    base = int(p)
    return sum(num <= base for num in generate_num(t,num_len))

def generate_num(t, num_len):
    num = t[:num_len]
    yield int(num)
    for digit in t[num_len:]:
        num = num[1:]+digit
        yield int(num)