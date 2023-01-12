def solution(n, stations, w):
    ans = 0
    idx = 0
    location = 1

    while(location <= n) :
        if(idx < len(stations) and location >= stations[idx]-w) :
            location = stations[idx]+w+1
            idx += 1
        else :
            location += 2*w+1
            ans += 1
    return ans