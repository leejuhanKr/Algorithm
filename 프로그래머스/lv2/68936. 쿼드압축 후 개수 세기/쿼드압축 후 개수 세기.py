from collections import Counter


def solution(arr):
    def foo(r, c, _len):
        if _len == 1:
            return Counter([arr[r][c]])

        _len //= 2
        lt = foo(r, c, _len)
        lb = foo(r + _len, c, _len)
        rt = foo(r, c + _len, _len)
        rb = foo(r + _len, c + _len, _len)
        res = lt + lb + rt + rb
        if res == Counter({0: 4}):
            return Counter([0])
        elif res == Counter({1: 4}):
            return Counter([1])
        return res
    
    ans = foo(0, 0, len(arr))
    
    return [ans[0],ans[1]]