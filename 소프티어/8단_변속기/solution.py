from sys import stdin
from enum import Enum


def get_gears():
    return [int(gear) for gear in stdin.readline().rstrip().split()]


def pairwise(iterable):
    a = iter(iterable)
    b = iter(iterable)
    next(b)
    return iter(zip(a, b))


class GearDiff(Enum):
    ASC = "ascending"
    DESC = "descending"
    MIX = "mixed"


def solution():
    gears = get_gears()
    gearDiffs = []
    for prev, tmp in pairwise(gears):
        if tmp == prev + 1:
            gearDiffs.append(GearDiff.ASC)
        elif tmp == prev - 1:
            gearDiffs.append(GearDiff.DESC)
        else:
            raise ValueError()

    for gearDiff in (GearDiff.ASC, GearDiff.DESC):
        if all((_gearDiff == gearDiff for _gearDiff in gearDiffs)):
            return gearDiff.value
    return GearDiff.MIX.value


print(solution())
