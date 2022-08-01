import sys
limit_number = 15000
sys.setrecursionlimit(limit_number)

def solution(enroll, referral, seller, amount):
    names = {'-':Seller()}
    for e,r in zip(enroll, referral):
        names[e] = Seller(names[r])
    for s,a in zip(seller, amount):
        names[s].earn(a*100)
    return [names[e].money for e in enroll]

class Seller():
    def __init__(self, parent=None):
        self.parent = parent
        self.money = 0
        
    def earn(self, amount):
        if self.parent:
            cost = amount//10
            amount-=cost
            self.money+=amount
            if cost:
                self.parent.earn(cost)
        else:
            self.money+=amount
        