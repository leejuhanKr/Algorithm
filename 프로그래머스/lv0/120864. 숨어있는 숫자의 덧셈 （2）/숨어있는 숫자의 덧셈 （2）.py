import re
def solution(my_string):
    return eval(re.sub('\D','+',my_string)+'+0')