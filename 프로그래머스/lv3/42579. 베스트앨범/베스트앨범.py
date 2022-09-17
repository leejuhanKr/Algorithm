def solution(genres, plays):
    dct = {}
    
    datas = zip(genres,plays)
    
    for idx,data in enumerate(datas):
        genre,play = data
        
        dct.setdefault(genre,[])
        dct[genre].append((play,idx))
    # print(dct)
    
    # ans = {k:[] for k in dct}
    ans=[]
    # print(ans)
    
    for genre,datas in dct.items():
        
        pick = []
        sum= 0
        for play,idx in datas:
            sum += play
            pick.append((play,idx))
            _key = lambda x: (-x[0],x[1])
            pick = sorted(pick,key=_key)[:2]
        
        ans.append((sum, [j for i,j in pick]))
    ans.sort(reverse=True)
    answer =  []
    for i,j in ans:
        answer+=j
    return(answer)