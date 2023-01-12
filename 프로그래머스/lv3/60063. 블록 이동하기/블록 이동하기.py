from collections import deque
def solution(board):
    n = len(board) + 2
    board = sum(([1] * n,*([1, *row, 1] for row in board),[1] * n), [])

    check = lambda pos: not any(board[i] for i in pos)
    def next_move_candiate(pos):
        align, shift = (1, n) if pos[1] - pos[0] == 1 else (n, 1)
        for _sign in (-1, 1):
            if check(next := tuple(i + _sign * align for i in pos)):
                yield next
            if check(next := tuple(i + _sign * shift for i in pos)):
                yield next
                yield from zip(*[pos, next][::_sign])

    inital_pos = (n + 1, n + 2)
    visited = set()
    q = deque([(inital_pos, 0)])
    destination = n*n - n - 2

    while q:
        pos, dist = q.popleft()
        if destination in pos:
            return dist
        if pos not in visited:
            visited.add(pos)
            for next_pos in next_move_candiate(pos):
                q.append((next_pos, dist + 1))