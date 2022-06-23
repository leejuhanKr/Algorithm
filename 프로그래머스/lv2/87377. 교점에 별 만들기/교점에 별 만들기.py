def solution(line):
    x_lim = y_lim = [float('inf'),-float('inf')]
    
    int_cross_point = []
    for i in range(len(line)):
        l1 = line[i]
        
        for j in range(i+1,len(line)):
            l2 = line[j]
            
            cross_point = get_cross_point(l1,l2)
            if cross_point == None:
                continue
                
            x,y = cross_point
            if all(map(float.is_integer,(x,y))):
                x,y = int(x), int(y)
                int_cross_point.append((x,y))
                x_lim = [min(x_lim[0],x), max(x_lim[1],x)]
                y_lim = [min(y_lim[0],y), max(y_lim[1],y)]

    cross_map = [
        ['.']*(x_lim[1]-x_lim[0]+1) 
        for _ in range(y_lim[1]-y_lim[0]+1)
    ]

    for x,y in int_cross_point:
        cross_map[y_lim[1]-y][x-x_lim[0]] = '*'
        
    for i,v in enumerate(cross_map): 
        cross_map[i] = ''.join(v)
        
    return cross_map

def get_cross_point(l1, l2):
    a, b, e = l1
    c, d, f = l2
    if (divider := a*d-b*c) == 0:
        return None
    return ((b*f-e*d)/divider, (e*c-a*f)/divider)