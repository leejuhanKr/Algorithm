def solution(score):
    res = sorted(
        enumerate(map(sum,score)), 
        key=lambda x: x[1], 
        reverse = True
    )
    ans = [0] * len(score)
    prev = -1
    acc = 0
    for j,(i,v) in enumerate(res,1):
        if prev != v:
            acc = 0
            prev = v
        else:
            acc+=1
        ans[i] = j-acc

    return ans