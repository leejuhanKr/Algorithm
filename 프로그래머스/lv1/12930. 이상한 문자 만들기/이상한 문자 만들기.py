def convert(s:str):
    flag = True
    for c in s:
        if c == ' ':
            yield c
            flag = True
        else:
            if flag:
                yield c.upper()
            else:
                yield c.lower()
            flag = not flag

def solution(s):
    return "".join(convert(s))