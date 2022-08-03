n = int(input())

arr = [*map(int,input().split())]

max_len = 1

increase_cnt = 1
decrease_cnt = 1
a = arr[0]
for b in arr[1:]:
    if a < b:
        increase_cnt+=1
        max_len = max(max_len, decrease_cnt)
        decrease_cnt=1
    elif a > b:
        decrease_cnt+=1
        max_len = max(max_len, increase_cnt)
        increase_cnt=1
    else:
        increase_cnt+=1
        decrease_cnt+=1
    a=b
else:
    print(max(max_len, decrease_cnt, increase_cnt))