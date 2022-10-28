def solution(numbers):
    return int(''.join(gen(numbers)))

a = ("zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
d = {k:str(v) for v,k in enumerate(a)}

def gen(numbers):
    acc = ''
    for i in numbers:
        acc += i
        if acc in d:
            yield d[acc]
            acc = ''
            

        