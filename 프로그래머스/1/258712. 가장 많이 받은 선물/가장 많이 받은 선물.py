from collections import Counter

def solution(_friends, gifts):
    friends = { name: Friend(name) for name in _friends }
    
    for gift in gifts:
        giver, givee = map(lambda name: friends[name], gift.split())
        giver.give(givee)
        
    for A in friends.values():
        for B in friends.values():
            give_num_AB, give_num_BA = A.have_given(B), B.have_given(A)
            if (A == B): continue
            if (give_num_AB < give_num_BA): continue
            
            if (give_num_AB > give_num_BA):
                A.shouldGet += 1
            elif (A.index > B.index):
                A.shouldGet += 1
                
    return max(f.shouldGet for f in friends.values())
        

        
        
    return True

class Friend:
    def __init__(self, name):
        self.name = name
        self._give_dict = Counter()
        self._get = 0
        self.shouldGet = 0;
    
    def give(self, cls):
        self._give_dict[cls.name] += 1
        cls.get()
        
    def get(self):
        self._get += 1
        
    def have_given(self, cls):
        return self._give_dict[cls.name]
    
    @property
    def index(self):
        return sum(self._give_dict.values()) - self._get