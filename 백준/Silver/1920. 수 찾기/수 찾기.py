#%%
input1 = input()
input2 = input()
input3 = input()
input4 = input()
#%%
n=int(input1)
n_list = [int(i) for i in input2.split()]

m= int(input3) 
m_list = [(int(j),i) for i,j in enumerate(input4.split())]
# %%
n_list.sort()
m_list.sort()

# %%
lst = [False] * m
i,j = 0,0
while j < m:
    try:
        m_j = m_list[j][0]
        while m_j > (n_i := n_list[i]) :
            i += 1
        if m_j == n_i:
            lst[m_list[j][1]] = True
        else:
            lst[m_list[j][1]] = False
        j += 1
    except:
        break

for i in lst:
    print(int(i))