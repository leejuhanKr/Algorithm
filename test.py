# def comb(lst,n):
#     visited = [None] * n
#     def helper(i,j):
#         if i >= n:
#             print(visited)
#             return
#         if j >= len(lst):
#             return
#         visited[i] = lst[j]
#         helper(i+1, j+1)
#         visited[i] = None
#         helper(i, j+1)
#     helper(0,0)

# def comb(lst,n):
#     visited = [None] * n
#     def helper(i,j):
#         if i < 0:
#             print(visited)
#             return
#         if j < 0:
#             return
#         helper(i, j-1)
#         visited[i] = lst[j]
#         helper(i-1, j-1)
#     helper(n-1,len(lst)-1) 

# comb([1,2,3,4,5,6],3)

def comb(m,n):
    lst = [0]*m
    def helper(i,n:int):
        if n == 0:
            yield lst
        elif i < m:
            lst[i]=1
            yield from helper(i+1,n-1)
            lst[i]=0
            yield from helper(i+1,n)
    yield from helper(0,n)

for i in comb(5,2):
    i[0]=4
    print(i)