import heapq as hq

def solution(operations):
    q = TwoFaceQueue()
    func = {
        'I': lambda n: q.insert(n),
        'D': lambda flag: q.pop(flag)
    }
    for op, param in map(lambda x: x.split(), operations):
        func.get(op)(int(param))
        
    return q()
    
class TwoFaceQueue:
    def __init__(self):
        self.min_q = []
        self.max_q = []
        self._len = 0
        
    def __call__(self):
        if self._len <= 0:
            return [0, 0]
        return [-self.max_q[0], self.min_q[0]]
    
    def insert(self, n):
        hq.heappush(self.min_q, n)
        hq.heappush(self.max_q, -n)
        self._len += 1
    
    def pop(self, flag):
        if self._len <= 0:
            return None
        self._len -= 1
        res = -flag * hq.heappop(self.max_q if flag == 1 else self.min_q)
        if self._len <= 0:
            self.min_q.clear()
            self.max_q.clear()
        return res