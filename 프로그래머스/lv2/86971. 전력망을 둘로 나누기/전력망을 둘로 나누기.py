def solution(n, wires):
    res = 100
    tree = Tree(n, wires)
    for s,e in wires:
        tree.cut([s,e])
        diff = abs(len(tree.traverse(s))-len(tree.traverse(e)))
        res = min(res, diff)
        tree.attach([s,e])
    return res

class Tree:
    def __init__(self, n, wires):
        self.graph = [[0] * (n+1) for _ in range(n+1)]
        for s,e in wires:
            self.graph[s][e] = 1
            self.graph[e][s] = 1
            
    def traverse(self, root_node):
        visited = set()
        stack = [root_node]
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            for i,is_link in enumerate(self.graph[node]):
                if is_link:
                    stack.append(i)
        return visited
    
    def cut(self, wire):
        s, e = wire
        self.graph[s][e] = 0
        self.graph[e][s] = 0
    
    def attach(self, wire):
        s, e = wire
        self.graph[s][e] = 1
        self.graph[e][s] = 1
        