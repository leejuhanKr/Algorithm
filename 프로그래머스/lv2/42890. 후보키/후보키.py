from itertools import combinations


def solution(relation):
    res = set()
    for i in range(1,len(relation[0])+1):
        for j in combinations(range(len(relation[0])),i):
            for k in res:
                if set(j).issuperset(set(k)):
                    break
            else:
                keys = [tuple(r[v] for v in j) for r in relation]
                if len(keys) == len(set(keys)):
                    res.add(j)

    return len(res)