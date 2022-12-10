class Gems:
    def __init__(self):
        self.gems = {}
        self.len = 0
    def append(self,gem):
        if gem in self.gems:
            self.gems[gem]+=1
        else:
            self.gems[gem]=1
            self.len +=1
    def pop(self,gem):
        self.gems[gem]-=1
        if self.gems[gem]==0:
            del self.gems[gem]
            self.len-=1
    def get_number(self,gem):
        return self.gems.get(gem,0)

def solution(gems):
    res = [0,10e9]
    required_gems = len(set(gems))
    s=0
    e=0
    scope = Gems()
    while e<len(gems):
        scope.append(gems[e])
        e+=1
        while scope.get_number(gems[s])>1:
            scope.pop(gems[s])
            s+=1
        if required_gems == scope.len and e-s-1<res[1]-res[0]:
            res = [s+1,e]
    return res

    