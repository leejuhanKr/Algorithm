def solution(ineq, eq, n, m):
    if eq=='!':
        return +eval(f'{n}{ineq}{m}')
    else:
        return +eval(f'{n}{ineq}={m}')