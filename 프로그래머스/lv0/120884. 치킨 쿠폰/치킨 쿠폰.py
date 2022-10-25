def solution(chicken):
    q, r = divmod(chicken, 10)
    return q+solution(q+r) if q else 0
    