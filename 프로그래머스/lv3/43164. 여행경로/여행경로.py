from collections import defaultdict
def solution(tickets):
    tickets.sort()
    routes = defaultdict(list)
    for s,e in tickets:
        routes[s].append([e, 1])
    visited = ['ICN' ,*(0 for _ in range(len(tickets)))]
    res = []
    def back(tmp):
        if res:
            return
        if tmp == len(visited):
            res.append(visited.copy())
            return
        for ticket_info in routes[visited[tmp-1]]:
            e, not_used = ticket_info
            if not_used:
                visited[tmp] = e
                ticket_info[1] = 0
                back(tmp+1)
                ticket_info[1] = 1
    back(1)
    return(res[0])