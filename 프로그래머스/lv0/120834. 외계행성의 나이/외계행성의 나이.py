def solution(age):
    a = {str(k):v for k,v in enumerate('abcdefghij')}
    return ''.join(a[i] for i in str(age))