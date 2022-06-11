pillar, beam = 0, 1

class Wall:
    def __init__(self):
        self.members = set()
    
    def build_condition(self, x, y, _type):
        if _type == pillar:
            cond = [
                y == 0,
                (x,y-1,pillar) in self.members,
                (x,y,beam) in self.members, (x-1,y,beam) in self.members,
            ]
        elif _type == beam:
            cond = [
                (x,y-1,pillar) in self.members, (x+1,y-1,pillar) in self.members,
                {(x-1,y,beam),(x+1,y,beam)}.issubset(self.members)
            ]
        return any(cond)
    
    def remove_condition(self, x, y, _type):
        self.members.remove((x,y,_type))

        if _type == pillar:
            relations = [
                (x,y+1,pillar),
                (x,y+1,beam), (x-1,y+1, beam),
            ]
        elif _type == beam:
            relations = [
                (x,y,pillar), (x+1,y,pillar),
                (x-1,y,beam), (x+1,y,beam)
            ]

        relations = filter(lambda x: x in self.members,relations)
        condition = all(map(lambda x: self.build_condition(*x), relations))
        self.members.add((x,y,_type))
        return condition

    def build(self, x, y, _type):
        if self.build_condition(x,y,_type):
            self.members.add((x,y,_type))

    def remove(self, x, y, _type):
        if self.remove_condition(x,y,_type):
            self.members.remove((x,y,_type))

def solution(n, build_frame):
    wall = Wall()
    build_action = {0: wall.remove, 1: wall.build}
    for x, y, type_, command in build_frame:
        build_action[command](x,y,type_)
    res = sorted(wall.members)
    return list(map(list,res))

n=5
# build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
ans = solution(n,build_frame)
print(ans)
print(*ans, sep='\n')
