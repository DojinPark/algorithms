# https://programmers.co.kr/learn/courses/30/lessons/43164
# 여행경로

ret = []
route = ['ICN']
def dfs(edges, N, a = 'ICN'):
    global ret, route

    # print(len(route), N, route)
    
    if len(route) == N:
        ret = route
        return ret

    if not edges[a]:
        return ret

    for i, (b, visited) in enumerate(edges[a]):
        if not visited:
            edges[a][i][1] = True
            route.append(b)

            dfs(edges, N, b)
            if len(ret) == N:
                return ret

            edges[a][i][1] = False
            route.pop()
    
    return ret
    
def solution(tickets):
    global ret
    ret = []

    answer = []
    edges = {}
    for a, b in tickets:
        if a not in edges.keys():
            edges[a] = []
        if b not in edges.keys():
            edges[b] = []
        edges[a].append([b, False])
    for a in edges.keys():
        edges[a].sort()
    # print(edges)
    
    answer = dfs(edges, len(tickets) + 1)

    return answer

# tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
# print( solution(tickets) )

# tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
# print( solution(tickets) )

tickets = 	[["ICN", "B"], ["B", "C"], ["C", "ICN"], ["ICN", "D"], ["ICN", "E"], ["E", "F"]]
print( solution(tickets) ) # 	["ICN", "B", "C", "ICN", "E", "F", "D"]