def solution(lines):
    l = [0]*200
    for line in lines:
        for x in range(*sorted(line)):
            l[x+100] += 1
    return sum(v >= 2 for v in l)