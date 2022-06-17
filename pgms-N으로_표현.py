def solution(N, number):
    answer = [None,*({int(str(N)*i)} for i in range(1,9))]

    for i in range(1,9):
        if number in answer[i]:
            return i
        for j in range(1,i):
            for a in answer[j]:
                for b in answer[i-j]:
                    for opt in (int.__add__, int.__sub__, int.__mul__, int.__floordiv__):                        
                        if (res := opt(a,b)) == number:
                            return i
                        if res != 0:
                            answer[i].add(res)
    return -1

print(solution(2,11))