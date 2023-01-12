def solution(babbling):
    return len([i for i in babbling if check(i)])

def check(s):
    prev = ''
    i=0
    while i < len(s):
        for c in ['aya', 'ye', 'woo', 'ma']:
            if s[i:].startswith(c) and prev != c :
                i += len(c)
                prev = c
                break
        else:
            return False
    return True