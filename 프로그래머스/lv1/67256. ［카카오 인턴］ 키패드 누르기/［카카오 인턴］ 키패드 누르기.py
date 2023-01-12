def solution(nums, hand):
    answer = ""
    t = Typing()
    
    for num in nums:
        if num in (1,4,7):
            answer+='L'
            t.left = num
            continue
        elif num in (3,6,9):
            answer+='R'
            t.right = num
            continue
        
        d_l,d_r = t.distance_lr(num)
        if d_l < d_r:
            answer+='L'
            t.left = num
        elif d_l > d_r:
            answer+='R'
            t.right = num
        elif hand=="left":
            answer += 'L'
            t.left = num
        else:
            answer += 'R'
            t.right = num
            
    return answer

class Typing:
    pad = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        ["*", 0, "#"],
    ]
    
    def __init__(self):
        Typing.pos = {value:(r,c) for r,rows in enumerate(Typing.pad) for c,value in enumerate(rows)}
        self.left = "*"
        self.right = "#"
    
    @staticmethod
    def distance_from_pos(tmp_num,target_num):
        tmp_pos = Typing.pos[tmp_num]
        target_pos = Typing.pos[target_num]
        d_x,d_y = map(lambda x: abs(x[0]-x[1]), zip(tmp_pos, target_pos))
        return d_x+d_y

    def distance_lr(self, target_num):
        l_distance = Typing.distance_from_pos(self.left, target_num)
        r_distance = Typing.distance_from_pos(self.right, target_num)
        return l_distance, r_distance