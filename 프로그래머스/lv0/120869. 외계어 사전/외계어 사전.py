def solution(spell, dic):
    spell = set(spell)
    return 1 if any(spell == set(word) for word in dic) else 2
    