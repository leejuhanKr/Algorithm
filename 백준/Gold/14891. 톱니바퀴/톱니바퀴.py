from collections import deque


class Gear:
    # N:0, S:1
    # cw:1 ccw:-1
    def __init__(self, tooths):
        self.status = deque(map(int, tooths))

    def rotate(self, dir):
        self.status.rotate(dir)

    def shape(self):
        shape = [[" "] * 3 for _ in range(3)]
        shape[1][1] = "@"

        positions = [(0, 1), (0, 2), (1, 2), (2, 2), (2, 1), (2, 0), (1, 0), (0, 0)]
        for pole, (r, c) in zip(self.status, positions):
            shape[r][c] = ["N", "S"][pole]
        return [" ".join(i) for i in shape]

    @property
    def right(self):
        return self.status[2]

    @property
    def left(self):
        return self.status[-2]

    @property
    def top(self):
        return self.status[0]


class GearSystem:
    def __init__(self, gears):
        self.gears = gears

    def __str__(self):
        res = ["|".join(s) for s in zip(*map(lambda ins: ins.shape(), self.gears))]
        return "\n".join((*res, "_" * len(res[0])))

    def _rotate_gear_n(self, idx, dir):
        if idx in self._visited:
            return
        self._visited.add(idx)
        if 0 <= idx - 1:
            if self.gears[idx - 1].right != self.gears[idx].left:
                # self.gears[idx-1].rotate(-dir)
                self._rotate_gear_n(idx - 1, -dir)
        if idx + 1 < 4:
            if self.gears[idx + 1].left != self.gears[idx].right:
                # self.gears[idx+1].rotate(-dir)
                self._rotate_gear_n(idx + 1, -dir)
        self.gears[idx].rotate(dir)

    def rotate_gear_n(self, idx, dir):
        self._visited = set()
        self._rotate_gear_n(idx, dir)
        self._visited.clear()


gears = [Gear(input()) for _ in range(4)]
g = GearSystem(gears)

n = int(input())

for _ in range(n):
    idx, dir = map(int, input().split())
    g.rotate_gear_n(idx - 1, dir)
    # print(idx, 'cw' if dir=='1' else 'ccw')
    # print(g)

_g = [gear.top for gear in g.gears]
print(sum(v * (2**i) for i, v in enumerate(_g)))
