import re
def solution(my_string):
    return eval(re.sub('[a-zA-Z]','+',my_string)+'+0')