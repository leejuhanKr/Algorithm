def solution(new_id):
    id = list(new_id)
    
    for process in (pc1, pc2, pc3, pc4, pc5, pc6, pc7):
        id = process(id)
        
    return "".join(id)

def pc1(id):
    return [i.lower() if i.isupper else i for i in id]

def pc2(id):
    return [i for i in id if any((i.islower(), i.isnumeric(), i in ("-", "_", ".")))]

def pc3(id):
    id = "".join(id)
    while '..' in id:
        id = id.replace("..",'.')
    return list(id)

def pc4(id):
    return list("".join(id).strip('.'))

def pc5(id):
    return ["a"] if not id else id

def pc6(id):
    id = id[:15]
    return id[:-1] if id[-1]=="." else id

def pc7(id):
    return id+([id[-1]]*shortage) if (shortage:= (3-len(id))) > 0 else id