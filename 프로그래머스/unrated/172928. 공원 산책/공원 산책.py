class Park:
    def __init__(self, graph):
        self.map = graph
        self.max_row = len(graph[0]) - 1
        self.max_col = len(graph[1]) - 1

    def can_move(self, from_, to) -> bool:
        if not (0 <= to[0] <= self.max_row and 0 <= to[1] <= self.max_col):
            return False

        x_i, y_i, x_f, y_f = *from_, *to
        if y_i == y_f:
            y = y_i
            x_i, x_f = sorted((x_i, x_f))
            return all(self.map[x][y] for x in range(x_i, x_f + 1))
        else:
            x = x_i
            y_i, y_f = sorted((y_i, y_f))
            #
            return all(self.map[x][y] for y in range(y_i, y_f + 1))


class Point:
    def __init__(self, pos):
        self.x, self.y = pos

    def set_pos(self, pos):
        self.x, self.y = pos

    @property
    def pos(self):
        return [self.x, self.y]


def parse_park(park):
    _map = []
    start = (-1, -1)
    for r_idx, row in enumerate(park):
        _row = []
        for c_idx, v in enumerate(row):
            flag = 1
            if v == "X":
                flag = 0
            elif v == "S":
                start = (r_idx, c_idx)
            _row.append(flag)
        _map.append(_row)
    return _map, start


def parse_route(string):
    _command, _x = string.split()
    return _command, int(_x)


def get_next_pos(pos, command, w):
    _dict = {
        "E": (0, 1),
        "S": (1, 0),
        "W": (0, -1),
        "N": (-1, 0),
    }
    x, y = pos
    dx, dy = _dict[command]
    return x + w * dx, y + w * dy


def solution(park, routes):
    _map, start = parse_park(park)
    dog = Point(start)
    park = Park(_map)
    print(park.map)
    for command, w in map(parse_route, routes):
        tmp_pos, next_pos = dog.pos, get_next_pos(dog.pos, command, w)
        if park.can_move(tmp_pos, next_pos):
            dog.set_pos(next_pos)
    return dog.pos