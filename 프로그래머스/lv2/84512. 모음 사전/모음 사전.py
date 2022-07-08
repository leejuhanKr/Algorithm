def solution(word):
    convert={'A':0,'E':1,'I':2,'O':3,'U':4}
    weights = [781, 156, 31, 6, 1]
    ans = len(word)
    for c,w in zip(word,weights):
        ans += convert[c]*w
    return ans

# weights=[1,1,1,1,1]
# for i in range(3,-1,-1):
#     weights[i] += 5*weights[i+1]