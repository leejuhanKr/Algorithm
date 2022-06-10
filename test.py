def solution(n, build_frame):
    n=n+1
    wall = [[[] for _ in range(n)] for _ in range(n)]
    pillar,beam = 0,1

    def can_bulid_pillar(x,y):
        if y == 0:
            return True
        elif pillar in wall[x][y-1]:
            return True
        elif x!=0 and beam in wall[x-1][y]:
            return True
        return False
        
    def can_build_beam(x,y):
        if y == 0:
            return False
        if pillar in wall[x][y-1]:
            return True
        if x+1 == n:
            return False
        if pillar in wall[x+1][y-1]:
            return True
        if (beam in wall[x][y]) and (beam in wall[x+1][y]):
            return True
        return False

    def can_build(x,y,_type):
        if _type == 0:
            return can_bulid_pillar(x,y)
        else:
            return can_build_beam(x,y)

    def can_remove(x,y,_type):
        wall[x][y].remove(_type)
        check_require=[]
        if _type == pillar:
            for el in wall[x][y+1]:
                check_require.append([x,y+1,el])
        else:
            for _x in (x-1,x+1):
                for el in wall[_x][y]:
                    check_require.append([_x,y,el])
        wall[x][y].insert(_type,_type)     
        return all(map(lambda x: can_build(*x),check_require))


    for x, y, _type, create in build_frame:
        if create == 0: # 0은 삭제를 의미
            if not can_remove(x,y,_type):
                continue
            wall[x][y].remove(_type)
        else:
            if not can_build(x,y,_type):
                continue
            # print(f'{wall=}, {x,y=}, {_type=}')
            wall[x][y].insert(_type,_type)

    result = []
    for r in range(n):
        for c in range(n):
            # print(result)
            for _type in wall[r][c]:
                result.append([r,c,_type])
    print(*wall, sep="\n")
    return result

n = 5
build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
result = [[1,0,0],[1,1,1],[2,1,0],[2,2,1],[3,2,1],[4,2,1],[5,0,0],[5,1,0]]

build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
result = [[0,0,0],[0,1,1],[1,1,1],[2,1,1],[3,1,1],[4,0,0]]

ans = solution(n, build_frame)
print(ans)
