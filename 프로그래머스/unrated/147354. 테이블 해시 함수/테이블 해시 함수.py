def solution(data, col, row_begin, row_end):
    data.sort(key=lambda x: (x[col-1],-x[0]))
    data = data[row_begin-1: row_end]
    data = [
        sum(val%data_idx for val in row)
        for data_idx, row in enumerate(data,row_begin)
    ]
    res = data[0]
    for val in data[1:]:
        res^=val
    return res
    
def mod_sum(num_arr, data_idx):
    return sum(i%data_idx for i in num_arr)
