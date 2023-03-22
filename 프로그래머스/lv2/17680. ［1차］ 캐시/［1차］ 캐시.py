from functools import lru_cache

def solution(cache_size, cities):
    
    @lru_cache(maxsize=cache_size)
    def foo(city): pass

    for city in cities: foo(city.lower())

    return foo.cache_info().hits * 1 + foo.cache_info().misses * 5