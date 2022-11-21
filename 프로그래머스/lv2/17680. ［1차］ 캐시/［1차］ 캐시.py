from collections import deque

def solution(cache_size, cities):
    total_time = 0
    cache = deque([], maxlen = cache_size)
    for city in cities:
        city = city.lower()
        
        if city in cache:
            cache.remove(city)
            total_time+=1
        else: # cache miss
            total_time+=5

        cache.append(city)
                
    return total_time