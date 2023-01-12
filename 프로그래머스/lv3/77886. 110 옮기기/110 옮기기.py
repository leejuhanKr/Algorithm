def solution(s):
    return list(map(sol,s))

def sol(s):
    ws = []
    w = ''
    cnt=0
    for c in s:
        if c == "1":
            w += '1'
            continue
        if w[-2:] == '11':
            # ws.append('110')
            cnt+=1
            w = w[:-2]
        else:
            ws.append(w+'0')
            w=''
    ws.append(w)
    return ''.join((*ws[0:len(ws)-1],'110'*cnt ,*ws[len(ws)-1:]))
