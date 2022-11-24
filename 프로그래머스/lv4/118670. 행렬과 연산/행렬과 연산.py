from collections import deque


class Box:
    def __init__(self, rc):
        self.l, self.r, self.t, self.b, self.m = Box.split_arr(rc)

    @staticmethod
    def split_arr(rc):
        l, r, m = map(deque, [[]] * 3)
        for a, *b, c in rc:
            l.append(a)
            r.append(c)
            m.append(deque(b))
        t = m.popleft()
        b = m.pop()
        return l, r, t, b, m

    @property
    def shape(self):
        return [
            [self.l[i], *row, self.r[i]]
            for i, row in enumerate((self.t, *self.m, self.b))
        ]

    def __str__(self):
        return str(self.shape)

    def shift(self):
        self.l.rotate()
        self.r.rotate()
        self.m.appendleft(self.t)
        self.t = self.b
        self.b = self.m.pop()

    def rotate(self):
        self.t.appendleft(self.l.popleft())
        self.r.appendleft(self.t.pop())
        self.b.append(self.r.pop())
        self.l.append(self.b.popleft())


def solution(rc, operations):
    box = Box(rc)
    box_func = lambda ops: {"Rotate": box.rotate, "ShiftRow": box.shift}.get(ops)()
    for ops in operations:
        box_func(ops)
    return box.shape