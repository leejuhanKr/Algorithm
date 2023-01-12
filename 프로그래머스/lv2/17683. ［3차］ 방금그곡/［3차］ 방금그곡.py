from collections import namedtuple
from datetime import timedelta
import re

Music = namedtuple("Music", ['runtime','title','melody'])

def convert2time(time_string):
    kargs = {k:int(v) for k,v in zip(['hours','minutes'],time_string.split(':'))}
    return timedelta(**kargs)

def solution(m, musicinfos):
    patterns = 'C#|D#|F#|G#|A#|C|D|E|F|G|A|B'
    m = ",".join(re.findall(patterns, m)) + ','
    infos = []
    for info in musicinfos:
        start,end,title,melody = info.split(',')
        runtime = int((convert2time(end) - convert2time(start)).total_seconds()//60)
        melody = re.findall(patterns, melody)
        infos.append(Music(runtime, title, melody))
    infos.sort(key=lambda x: -x.runtime)
    
    for runtime, title, melody in infos:
        runtime_melody = ','.join(melody[i%len(melody)] for i in range(runtime)) + ','
        if m in runtime_melody:
            return title
    return '(None)'