def solution(my_string):
    return ''.join(i.lower() if i.isupper() else i.upper() for i in my_string)