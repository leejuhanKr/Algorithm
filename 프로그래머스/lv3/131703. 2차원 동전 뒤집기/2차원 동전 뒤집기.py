def solution(beginning, target):
    diff_mat = diff(beginning, target)
    _row = diff_mat[0]

    r = 0
    c = sum(_row)
    
    for row in diff_mat[1:]:
        if row != _row:
            r += 1
            if [not i for i in row] != _row:
                return -1

    return min(r+c, len(diff_mat)+len(diff_mat[0])-r-c)
        
def diff(mat1, mat2):
    for i, row in enumerate(mat1):
        for j, v in enumerate(row):
            mat1[i][j] = v != mat2[i][j]
    return mat1