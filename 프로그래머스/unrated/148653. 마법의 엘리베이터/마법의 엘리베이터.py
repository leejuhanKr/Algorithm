def solution(storey):
    return foo([0, *(int(i) for i in str(storey))], 0)

def foo(rest, step):
    if not rest: return step
    *rest, tmp = rest
    if tmp == 5:
        step += 5
        if rest[-1] >= 5:
            rest[-1] += 1
    elif tmp > 5:
        step += 10 - tmp
        rest[-1] += 1
    else:
        step += tmp
    return foo(rest, step)
    