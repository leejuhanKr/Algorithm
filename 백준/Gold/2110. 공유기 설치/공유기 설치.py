from sys import stdin

_, c = map(int,input().split())
positions = sorted(map(int,stdin.readlines()))
dists = [p2-p1 for p1,p2 in zip(positions,positions[1:])]

def check(dists, c):
    """ 
    각 집들간의 간격에 대한 배열 dists와 공유기의 개수 c를 받아
    target이 주어졌을때 최댓값을 target보다 크거나 같게 만들수 있는지 반환하는 함수 리턴
    """
    def helper(target):
        sum = 0
        cnt = c-1 # 첫번째 설치후 남아있는 공유기 개수
        for dist in dists:
            sum+=dist
            if sum>=target:
                cnt-=1
                if not cnt: # 더이상 설치할 공유기 없으면 true 반환
                    return True
                sum=0
        return False
    return helper

cb = check(dists, c)

def bisect(l, r, cb):
    while l <= r:
        mid = (l+r)//2
        if cb(mid):
            l = mid + 1
        else:
            r = mid - 1
    return r

print(bisect(0,positions[-1]-positions[0],cb))