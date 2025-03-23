def comb(seq, n):
    len_ = len(seq)
    def _comb(prev, i):
        if len(prev) == n:
            yield prev
            return
        if i >= len_:
            return
        cur_el = seq[i]
        cur = [*prev, cur_el]
        yield from _comb(cur, i+1)
        yield from _comb(prev, i+1)
    yield from _comb([], 0)
            
def cond(seq, q, a):
    s_i, l_s = 0, len(seq)
    q_i, l_q = 0, len(q)
    r = 0
    while s_i < l_s and q_i < l_q:
        if seq[s_i] == q[q_i]:
            r+=1
            s_i += 1
            q_i += 1
        elif seq[s_i] > q[q_i]:
            q_i += 1
        else:
            s_i += 1
    return r == a

def debug_func(func):
    def wrapped(*args):
        try:
            return func(*args)
        except Exception as e:
            print(e)
            return 0
    return wrapped

# @debug_func
def solution(n, qs, ans):
    answer = 0
    for seq in comb([i for i in range(1, n+1)], 5):
        # print(seq)
        if all(cond(seq, q, a) for q, a in zip(qs, ans)):
            answer+=1
    return answer