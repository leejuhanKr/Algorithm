def wrap(w_list: list[str], prefix, suffix):
    return "".join(f"{prefix}{w}{suffix}" for w in w_list)

def sol(n):
    intro = '어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.'
    s1 = '"재귀함수가 뭔가요?"'
    s2 = '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.'
    s3 = '마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.'
    s4 = '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."'
    main = '"재귀함수는 자기 자신을 호출하는 함수라네"'
    e1 = '라고 답변하였지.'

    wrap4 = lambda w_list, cur: wrap(w_list, '_'*4*cur, '\n')
    
    def recursive(n, cur):
        if n == 0:
            return wrap4([s1, main, e1], cur)
        return wrap4([s1, s2, s3, s4], cur) + recursive(n - 1, cur + 1) + wrap4([e1], cur)

    return f"{intro}\n{recursive(n, 0)}"

if __name__ == "__main__":
    print(sol(int(input())))