from sys import stdin
from enum import IntEnum, auto
from itertools import product


def get_N():
    return int(stdin.readline())


def config_block(val):
    return Board.BLOCK if val == "1" else Board.PATH


def get_Board():
    return [list(map(config_block, i.rstrip())) for i in stdin.readlines()]


class Board(IntEnum):
    BLOCK = auto()
    PATH = auto()


def solution():
    N = get_N()
    board = get_Board()

    def dfs(start, board_type):
        stack = [start]
        diffs = ((-1, 0), (1, 0), (0, -1), (0, 1))
        visited = set()

        while stack:
            pos = stack.pop()
            x, y = pos

            if pos in visited:
                continue

            if not (0 <= x < N and 0 <= y < N and board[x][y] == board_type):
                continue

            visited.add(pos)

            for dx, dy in diffs:
                nx, ny = x + dx, y + dy
                stack.append((nx, ny))

        return visited

    visited = set()
    res = set()
    for x, y in product(range(N), range(N)):
        start = x, y
        board_type = board[x][y]
        if start in visited:
            continue
        _vistied = dfs(start, board_type)

        visited.update(_vistied)
        if board_type == Board.BLOCK:
            res.add(len(_vistied))

    return sorted(res)


blocks = solution()
print(len(blocks))
for block in blocks:
    print(block)
