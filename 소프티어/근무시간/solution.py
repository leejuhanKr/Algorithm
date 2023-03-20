from sys import stdin


def get_daily_work_time():
    start, end = stdin.readline().rstrip().split(" ")
    return start, end


def parse_str2min(_str):
    h, m = map(int, _str.split(":"))
    return 60 * h + m


def solution():
    res = []
    for i in range(5):
        start, end = map(parse_str2min, get_daily_work_time())
        work_time = end - start
        res.append(work_time)
    return sum(res)


print(solution())
