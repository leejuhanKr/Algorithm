from copy import deepcopy

sum_board = lambda mat: sum(sum(rows) for rows in mat)

def diff(mat1, mat2):
    r = len(mat1)
    c = len(mat1[0])
    mat = [[1]*c for i in range(r)]
    for i in range(r):
        for j in range(c):
            if mat1[i][j] == mat2[i][j]:
                mat[i][j] = 0
    return mat

def flip(mat, p, col = False):
    r = len(mat)
    c = len(mat[0])
    if col:
        for i in range(r):
            mat[i][p] = +(not mat[i][p])
        return
    for j in range(c):
        mat[p][j] = +(not mat[p][j])

def solution(beginning, target):
    r = len(beginning)
    c = len(beginning[0])
    res = 10e9
    
    basic_mat = diff(beginning, target)
    for is_flip_top in (0,1):
        k = 0
        mat1 = deepcopy(basic_mat)
        if is_flip_top:
            k+=1
            flip(mat1,0)
        for j in range(c):
            if not mat1[0][j]:
                continue
            k+=1
            flip(mat1, j, 1)
        for is_flip_left in (0,1):
            m = k
            mat2 = deepcopy(mat1)
            if is_flip_left:
                m+=1
                flip(mat2,0)
            for i in range(r):
                if not mat1[i][0]:
                    continue
                m+=1
                flip(mat2, i)
            if sum_board(mat2) == 0:
                res = min(res, m)
    
    return res if res!=10e9 else -1

    