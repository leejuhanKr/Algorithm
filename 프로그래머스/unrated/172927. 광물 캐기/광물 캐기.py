from operator import mul
from itertools import repeat, chain


def count_mineral(minerals):
    res = [0, 0, 0]
    for mineral in minerals:
        if mineral == "diamond":
            res[0] += 1
        elif mineral == "iron":
            res[1] += 1
        else:
            res[2] += 1
    return res


def pairwise(iterable, _len=2, func=tuple):
    group = []
    for v in iterable:
        group.append(v)
        if len(group) >= _len:
            yield func(group)
            group.clear()
    if any(group):
        yield func(group)


fatigue = [
    [1, 1, 1],
    [5, 1, 1],
    [25, 5, 1],
]


def solution(picks, minerals):
    res = 0
    minerals = minerals[: sum(picks * 5)]
    mineral_groups = sorted(pairwise(minerals, 5, count_mineral), reverse=True)

    _picks = chain(*(repeat(i, int(amount)) for i, amount in enumerate(picks)))
    for pick, mineral_group in zip(_picks, mineral_groups):
        res += sum(mul(a, b) for a, b in zip(fatigue[pick], mineral_group))
    return res