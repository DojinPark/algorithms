# https://programmers.co.kr/learn/courses/30/lessons/72413
# 4. 합승 택시 요금
#
# 걸린 시간 0:58

# 최단거리, MST 알고리즘 코드 통째로 외우는 복습 하기!!!

INF = int(1e9)

from heapq import heappush as push, heappop as pop

def shortest_path(edges, start):
    cost = [INF] * len(edges)
    h = []
    
    cost[start] = 0
    push(h, (0, start))

    while h:
        c, x = pop(h)

        if c > cost[x]: continue

        for d, y in edges[x]:
            # print('y:',y, cost[y], ">?", c, '+', d)
            if cost[y] > c + d:
                cost[y] = c + d
                push(h, (c + d, y))
    return cost

def solution(n, s, a, b, fares):
    answer = INF

    N = n + 1
    edges = [ [] for _ in range(N) ]
    for fare in fares:
        x, y, d = fare
        edges[x].append( (d, y) )
        edges[y].append( (d, x) )
    # print(edges)

    to_common = shortest_path(edges, s)
    # print(to_common)
    for common in range(1, N):
        from_common = shortest_path(edges, common)
        answer = min(answer, to_common[common] + from_common[a] + from_common[b])

    return answer

n = 6
s = 4
a = 6
b = 2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
print( solution(n, s, a, b, fares) )
# 82

n = 7
s = 3
a = 4
b = 1
fares = [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]
print( solution(n, s, a, b, fares) )
# 14

n = 6
s = 4
a = 5
b = 6
fares = [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]
print( solution(n, s, a, b, fares) )
# 18