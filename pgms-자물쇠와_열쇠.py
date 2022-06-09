KEY = [
    [0, 0, 0], 
    [1, 0, 0], 
    [1, 1, 1]
    ]
LOCK = [
    [1, 1, 1], 
    [1, 1, 0], 
    [1, 0, 1]
    ]

def solution(key, lock):
    n = len(key)
    m = len(lock)

    def rotate(key):
        res = [[0]*n for _ in range(n)]
        for i in range(n):
            c = n-i-1
            for j in range(n):
                r = j
                res[r][c] = key[i][j]
        return res

    def is_fit_pos(key,dr,dc):
        for r in range(m):
            for c in range(m):
                if not(0<=r-dr<n and 0<=c-dc<n):
                    if lock[r][c]:
                        continue
                    else:
                        return False
                if key[r-dr][c-dc] == lock[r][c]:
                    return False
        return True

    def is_fit_all_dir(key):
        for dr in range(-n+1,m):
            for dc in range(-n+1,m):
                if is_fit_pos(key,dr,dc):
                    return True
        return False

    def is_fit(key):
        for _ in range(4):
            if is_fit_all_dir(key):
                return True
            key = rotate(key)
        return False

    return is_fit(key)

print(solution(KEY,LOCK))




