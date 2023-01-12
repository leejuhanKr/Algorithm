import re
import heapq as hq

def solution(lines):
    q = []
    res = 0
    for l in reversed(lines):
        _, t, dt = l.split(' ')
        t_ms, dt_ms = time2ms(t), timedelta2ms(dt)
        while q and -q[0] >= t_ms+1000:
            el = hq.heappop(q)
        hq.heappush(q,-(t_ms-dt_ms+1))
        res = max(res, len(q))
    return res

def timedelta2ms(string):
    string_s = re.fullmatch('(?P<s>\d+(.\d+)?)s',string).group('s')
    return int(1000*float(string_s))
    
def time2ms(string):
    match_pattern = '(?P<t>\d+):(?P<m>\d+):(?P<s>\d+(.\d+)?)'
    t_dict = re.fullmatch(match_pattern,string).groupdict()
    t,m,s = int(t_dict['t']), int(t_dict['m']), float(t_dict['s'])
    return 60*60*1000*t + 60*1000*m + int(1000*s)