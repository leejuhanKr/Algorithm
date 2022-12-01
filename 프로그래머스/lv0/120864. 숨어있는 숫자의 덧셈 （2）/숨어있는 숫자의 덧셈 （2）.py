# import re

# def solution(my_string):
#     return eval(re.sub('\D','+',my_string)+'+0')

def solution(my_string):
    return sum(i for i in gen(my_string))

def gen(word):
    res = ""
    for w in word:
        if w.isalpha():
            if res:
                yield int(res)
                res=''
        else:
            res+=w
    yield int(res) if res else 0
            