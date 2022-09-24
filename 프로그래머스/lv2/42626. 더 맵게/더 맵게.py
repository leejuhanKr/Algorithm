import heapq as hq

def solution(scoville, K):
    ans=0
    hq.heapify(scoville)
    
    while scoville:
        first = hq.heappop(scoville)
        
        if first >=K:
            return ans
        
        if scoville:
            second = hq.heappop(scoville)
            
            replaced = first + second*2
            ans+=1
            
            hq.heappush(scoville, replaced)
            
    return -1