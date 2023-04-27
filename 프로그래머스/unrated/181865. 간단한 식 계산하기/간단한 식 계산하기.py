def solution(binomial):
    a,op,b = binomial.split()
    a,b = map(int, (a,b))
    return get_op(op)(a,b)
    
def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

op_dict = {
    '+': add,
    '-': sub,
    '*': mul,
}

def get_op(key):
    return op_dict[key]