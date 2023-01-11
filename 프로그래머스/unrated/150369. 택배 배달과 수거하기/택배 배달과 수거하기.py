def solution(cap, n, deliveries, pickups):
    deliver = Deliveries(cap, n, deliveries, pickups)
    deliver.run()
    return deliver.s*2

class Deliveries:
    def __init__(self, cap, n, dv, pu):
        self.cap = cap
        self.n = n
        self.dv = dv
        self.pu = pu
        self.s = 0
        
    def run(self):
        self._pop_last_zeros(self.dv)
        self._pop_last_zeros(self.pu)
        
        while self.dv or self.pu:
            self.go_routine()
        return self.s
    
    def go_routine(self):
        s_dv = self._go_one_way(self.dv)
        s_pu = self._go_one_way(self.pu)
        self.s += max(s_dv, s_pu)
        
    def _go_one_way(self, stacks):
        rest_cap = self.cap
        s = len(stacks)
        
        for _ in range(len(stacks)):
            if stacks[-1] < rest_cap:
                rest_cap -= stacks[-1]
                stacks.pop()
            else:
                stacks[-1] = stacks[-1] - rest_cap
                break
                
        self._pop_last_zeros(stacks)
        return s
                
    def _pop_last_zeros(self, stacks):
        for _ in range(len(stacks)):
            if stacks[-1]:
                break
            else:
                stacks.pop()
                
                
                
        
        