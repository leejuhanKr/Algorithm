from collections import deque

def find_start_end(graph, start_val, end_val):
    start, end = None, None
    for r, row in enumerate(graph):
        for c, val in enumerate(row):
            if val == start_val:
                start = (r, c)
            elif val == end_val:
                end = (r, c)

    if not all((start, end)):
        raise ValueError

    return start, end


def generate_next_pos(pos, graph, block):
    max_r, max_c = len(graph) - 1, len(graph[0]) - 1
    pos_r, pos_c = pos
    for r in reversed(range(pos_r + 1)):
        if r == 0 or graph[r - 1][pos_c] == block:
            yield r, pos_c
            break
    for r in range(pos_r, max_r+1, 1):
        if r == max_r or graph[r + 1][pos_c] == block:
            yield r, pos_c
            break
    for c in reversed(range(pos_c + 1)):
        if c == 0 or graph[pos_r][c - 1] == block:
            yield pos_r, c
            break
    for c in range(pos_c, max_c+1, 1):
        if c == max_c or graph[pos_r][c + 1] == block:
            yield pos_r, c
            break


def bfs(graph, start, end):
    q = deque([(start, 0)])
    visited = set()

    while q:
        pos, step = q.popleft()

        if pos == end:
            return step

        if pos in visited:
            continue
        visited.add(pos)

        step += 1
        for next in generate_next_pos(pos, graph, block="D"):
            q.append((next, step))

    return -1


def solution(board):
    start, end = find_start_end(board, start_val="R", end_val="G")
    return bfs(board, start, end)