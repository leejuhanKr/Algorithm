def cache(func):
    mem = {}
    def wrapper(*args):
        key = tuple(args)
        if key in mem:
            return mem[key]
        res = func(*args)
        mem[key] = res
        return res
    return wrapper
        

def solution(info, n, m):
    max_size_n = 10e9
    info_len = len(info)

    @cache
    def get_min_a(i, prev):
        a, b = prev
        if a >= n or b >= m:
            return max_size_n
       	if i >= info_len:
            return a
        w_a, w_b = info[i]
        res_a = get_min_a(i+1, (a, b+w_b))
        res_b = get_min_a(i+1, (a+w_a, b))
        return min(res_a, res_b)
        
        
    res = get_min_a(0, (0, 0))
    return res if res != max_size_n else -1