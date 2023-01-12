def solution(board, moves):
    ans = 0
    stack = []
    items = Board(board)
    for move in moves:
        item = items.pop(move)
        if not item:
            continue
        if stack and stack[-1] == item:
            stack.pop()
            ans += 2
        else:
            stack.append(item)
    return ans

class Board:
    def __init__(self, board: list):
        self.board = [[] for _ in range(len(board))]
        for rows in reversed(board):
            for i, item in enumerate(rows):
                if item != 0:
                    self.board[i].append(item)

    def pop(self, col):
        if not self.board[col - 1]:
            return None
        return self.board[col - 1].pop()