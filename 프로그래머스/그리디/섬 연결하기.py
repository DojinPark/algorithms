# https://programmers.co.kr/learn/courses/30/lessons/42861
# 섬 연결하기 (Level 3)
# 걸린 시간: 0:17
#
# 노트: MST 기본 문제

from heapq import heappush as push, heappop as pop

INF = -1

def solution(n, costs):
    answer = 0
    edges = [ [INF] * n for _ in range(n) ]
    visited = [False] * n
    q = []

    for a, b, c in costs:
        edges[a][b] = c
        edges[b][a] = c

    push(q, (0, 0) )
    for _ in range(n):
        c, a = pop(q)
        while visited[a]:
            c, a = pop(q)
        visited[a] = True

        answer += c

        for b in range(n):
            if edges[a][b] == INF: continue
            push(q, (edges[a][b], b))
    
    return answer


print( solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]) )