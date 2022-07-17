def solution(distance, rocks, n):
    rock_positions = sorted(rocks)
    
    def cond(s,n):
        # 바위를 거리의 최소값이 s 일때 바위를 n 개이상 지울 수 있는지 여부 반환
        removed = 0
        tmp_position = 0
        for rock_position in rock_positions:
            if rock_position-tmp_position < s:
                removed+=1
                if removed > n:
                    return True
            else:
                tmp_position = rock_position

        return False

    def bisect(left ,right, cond):
        while left <= right:
            mid = (left+right)>>1
            if cond(mid,n): 
                right = mid - 1
            else: 
                left = mid + 1
        return right
    
    return bisect(0, distance, cond)