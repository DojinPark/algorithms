# https://programmers.co.kr/learn/courses/30/lessons/49189
# 가장 먼 노드
# 걸린 시간: 0:11

from collections import deque

def solution(n, edge):
    answer = 0

    edges = [ [] for _ in range(n) ]
    visited = [False] * n
    q = deque()

    for a, b in edge:
        edges[a - 1].append(b - 1)
        edges[b - 1].append(a - 1)
    
    cnt = 0
    max_d = 0
    visited[0] = True
    q.append( (0, 0) ) # distance, node #
    while q:
        d, a = q.popleft()

        if max_d < d:
            cnt = 1
            max_d = d
        else:
            cnt += 1
        
        for b in edges[a]:
            if not visited[b]:
                visited[b] = True
                q.append( (d + 1, b) )
    
    answer = cnt

    return answer

n = 6
vertex = 	[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print( solution(n, vertex) ) # 3