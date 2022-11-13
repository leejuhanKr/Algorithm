import sys
sys.setrecursionlimit(10**6)

def solution(nodeinfo):
    nodeinfo = dict(sorted(
        enumerate(nodeinfo,1),
        key=lambda p: (-p[1][1], p[1][0])
    ))
    nodes = ((k, nodeinfo[k]) for k in nodeinfo)
    root_val = next(nodes)[0]
    tree = Tree(Node(root_val))
    
    for v, (x,_) in nodes:
        parent = tree.root
        while True:
            if nodeinfo[parent.val][0] <= x:
                if parent.right:
                    parent = parent.right
                else:
                    parent.right = Node(v)
                    break
            else:
                if parent.left:
                    parent = parent.left
                else:
                    parent.left = Node(v)
                    break
    return [tree.traverse(),tree.traverse(reverse=1)]

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.childs =[self.left, self.right]
    
    def set_left(self, val):
        self.left = val
    
    def set_right(self, val):
        self.right = val

    
class Tree:
    def __init__(self, node: Node):
        self.root = node
        self.visited = {}
    
    def t1(self, node):
        self.visited[node.val] = True
        if node.left:
            self.t1(node.left)
        if node.right:
            self.t1(node.right)
    
    def t2(self, node):
        if node.left:
            self.t2(node.left)
        if node.right:
            self.t2(node.right)
        self.visited[node.val] = True

    def traverse(self, reverse=False):
        self.visited.clear()
        if reverse:
            self.t2(self.root)
        else:
            self.t1(self.root)
        return list(self.visited.keys())
        
        