from itertools import product
def solution(n, computers):
    _range = range(len(computers))
    sets = [{v} for v in _range]
    for i,j in product(_range, repeat=2):
        if computers[i][j] and sets[i]!=sets[j]:
            sets[i]|=sets[j]
            for node in sets[j]:
                sets[node] = sets[i]
    return len(set(map(id, sets)))
            
            
        