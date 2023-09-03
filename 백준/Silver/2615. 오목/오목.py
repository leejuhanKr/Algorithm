from sys import stdin
from typing import Dict, Tuple


def solution(g: Dict[Tuple[int, int], int]):
    arr = sorted(g)

    for r, c in arr:
        if block := g[r, c]:
            for dx, dy in ((1, 0), (1, 1), (0, 1), (-1, 1)):
                x, y = r - dx, c - dy
                if g.get((x, y)) == block:
                    continue

                x, y = r, c
                for _ in range(5):
                    if g.get((x, y)) != block:
                        break
                    x += dx
                    y += dy

                else:
                    if g.get((x, y)) != block:
                        return block, (r, c)
    return 0, (-1, -1)


if __name__ == "__main__":
    g = {}
    for r in range(19):
        row = map(int, stdin.readline().rstrip().split(" "))

        for c, val in enumerate(row):
            if val:
                g[r, c] = val

    block, pos = solution(g)

    print(block)
    if block:
        print(*map(lambda x: x + 1, pos))
