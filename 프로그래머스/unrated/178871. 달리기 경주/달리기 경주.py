def solution(players, callings):
    lst = LinkedList.from_(players)
    for call in callings:
        a, b = lst.prev(call), call
        lst.switch(a, b)
    return list(lst)
    
class LinkedList:
    def __init__(self):
        self.lst = {}
        self.head = None
        self.tail = None
        
    def append_first(self, val):
        self.lst[val] = [None, None]
        self.head = val
        self.tail = val
    
    def append(self, val):
        self.lst[self.tail][1] = val
        self.lst[val] = [self.tail, None]
        self.tail = val
        
    @classmethod
    def from_(cls, lst):
        instance = cls()
        if len(lst):
            instance.append_first(lst[0])
        for val in lst[1:]:
            instance.append(val)
        return instance
    
    def prev(self, val):
        return self.lst[val][0]
    
    def next(self, val):
        return self.lst[val][1]
    
    def __iter__(self):
        tmp = self.head
        while tmp:
            yield tmp
            tmp = self.next(tmp)
    
    def switch(self, x, y):
        a,b,c,d = self.lst[x][0], x, y, self.lst[y][1]
        if not a:
            self.head = c
        else:
            self.lst[a][1] = c
        self.lst[c][:] = [a,b]
        self.lst[b][:] = [c,d]
        if not d:
            self.tail = b
        else:
            self.lst[d][0] = b


    