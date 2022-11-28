import heapq as hq

def solution(scoville, K):
    ans=0
    hq.heapify(scoville)
    
    while scoville:
        first = hq.heappop(scoville)
        
        if first >=K:
            return ans
        
        if scoville:
            ans+=1   
            hq.heapreplace(scoville, first + scoville[0]*2)
            
    return -1