from itertools import combinations
def solution(cards):
    cards = {i:v for i,v in enumerate(cards,1)}
    sets = []
    for tmp in list(cards):
        if tmp in cards:
            _set = set()
            while tmp in cards:
                _set.add(tmp)
                prev, tmp = tmp, cards[tmp]
                del cards[prev]
            sets.append(len(_set))
    return max((i*j for i,j in combinations(sets,2)), default = 0)

        
    