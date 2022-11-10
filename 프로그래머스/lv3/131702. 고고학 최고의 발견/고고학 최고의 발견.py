# from itertools import product

# def solution(clockHands):
#     res = 10e9
#     for inital_pos in product(range(4), repeat=len(clockHands)):
#         b = Board(clockHands)
#         initial_cnt = sum(inital_pos)
#         for j, n in enumerate(inital_pos, 1):
#             for i in range(n):
#                 b.turn_sets(1,j)
#         is_unlocked, cnt = solve(b, limit=res-initial_cnt)
#         if is_unlocked:
#             res = cnt + initial_cnt
#     return res

# def solve(b, limit=10e9):
#     cnt = 0
#     for i in range(1,b._len-2):
#         for j in range(1,b._len-1):
#             if direction := b.board[i][j]:
#                 cnt += 4-direction
#                 if cnt > limit:
#                     return False, limit
#                 for _ in range(4-direction):
#                     b.turn_sets(i+1,j)
#     # return b.can_unlock(), cnt
#     return not any(b.board[-2][1:-1]), cnt

# class Board:
#     def __init__(self, clockHands):
#         self._len = len(clockHands)+2
#         self.board = Board.set_board(clockHands)
        
#     def __str__(self):
#         return "\n".join(" ".join(i) for i in self.map)
    
#     @property
#     def map(self):
#         _dict = {0: '⬆️',1:'➡️',2:'⬇️',3:'⬅️'}
#         _len = self._len
#         _map = [
#             [_dict[self.board[i][j]] for j in range(1,_len-1)]
#             for i in range(1,_len-1)
#         ]
#         return _map
    
#     @staticmethod
#     def set_board(matrix):
#         _len = len(matrix)+2
#         board = [[0]*_len for _ in range(_len)]
#         for i, row in enumerate(matrix,1):
#             for j, v in enumerate(row,1):
#                 board[i][j] = v
#         return board
    
#     @staticmethod
#     def clock_set(i,j):
#         return ((i,j), (i-1,j), (i,j-1), (i+1,j), (i, j+1))
    
#     def turn(self, i,j):
#         self.board[i][j] = (self.board[i][j]+1)%4
    
#     def turn_sets(self, i,j):
#         for i,j in Board.clock_set(i,j):
#             self.turn(i,j)
    
#     def can_unlock(self):
#         for i in range(1,self._len-1):
#             for j in range(1,self._len-1):
#                 if self.board[i][j]:
#                     return False
#         return True

from itertools import product

def solution(clockHands):
    res = 10e9
    for inital_pos in product(range(4), repeat=len(clockHands)):
        b = Board(clockHands)
        initial_cnt = sum(inital_pos)
        for j, n in enumerate(inital_pos, 1):
            b.turn_sets(1,j,n)
        is_unlocked, cnt = solve(b, limit=res-initial_cnt)
        if is_unlocked:
            res = cnt + initial_cnt
    return res

def solve(b, limit=10e9):
    cnt = 0
    for i in range(1,b._len-2):
        for j in range(1,b._len-1):
            if direction := b.board[i][j]:
                cnt += 4-direction
                if cnt > limit:
                    return False, limit
                b.turn_sets(i+1,j,4-direction)
    # return b.can_unlock(), cnt
    return not any(b.board[-2][1:-1]), cnt

class Board:
    def __init__(self, clockHands):
        self._len = len(clockHands)+2
        self.board = Board.set_board(clockHands)
        
    def __str__(self):
        return "\n".join(" ".join(i) for i in self.map)
    
    @property
    def map(self):
        _dict = {0: '⬆️',1:'➡️',2:'⬇️',3:'⬅️'}
        _len = self._len
        _map = [
            [_dict[self.board[i][j]] for j in range(1,_len-1)]
            for i in range(1,_len-1)
        ]
        return _map
    
    @staticmethod
    def set_board(matrix):
        _len = len(matrix)+2
        board = [[0]*_len for _ in range(_len)]
        for i, row in enumerate(matrix,1):
            for j, v in enumerate(row,1):
                board[i][j] = v
        return board
    
    @staticmethod
    def clock_set(i,j):
        return ((i,j), (i-1,j), (i,j-1), (i+1,j), (i, j+1))
    
    def turn(self, i,j,n):
        self.board[i][j] = (self.board[i][j]+n)%4
    
    def turn_sets(self, i,j,n):
        for i,j in Board.clock_set(i,j):
            self.turn(i,j,n)
    
    def can_unlock(self):
        for i in range(1,self._len-1):
            for j in range(1,self._len-1):
                if self.board[i][j]:
                    return False
        return True