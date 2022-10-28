def solution(quiz):
    return [['X','O'][eval(s.replace('=','=='))] for s in quiz]