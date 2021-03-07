# https://programmers.co.kr/learn/courses/30/lessons/67260
# 5. 동굴 탐험
# 풀이 시간 초과
#
# 노트: Directed Graph를 처음 다루어 보았음.
#      Directed Graph의 cycle 판별은 위상 정렬 알고리즘으로 하면 됨!

import sys
sys.setrecursionlimit(200009)

def dfs_tree(tree, edge, visited, a = 0):
    visited[a] = True
    for b in edge[a]:
        if not visited[b]:
            tree[a].append(b)
            dfs_tree(tree, edge, visited, b)

from collections import deque
def solution(n, path, order):
    graph = [ [] for _ in range(n) ]
    cnt = [1] * n; cnt[0] = 0
    visited = set()
    q = deque()

    edge = [ [] for _ in range(n) ]
    for a, b in path:
        edge[a].append(b)
        edge[b].append(a)
    
    dfs_tree(graph, edge, [False] * n)

    for a, b in order:
        graph[a].append(b)
        cnt[b] += 1
    
    if cnt[0] == 0:
        q.append(0)
        visited.add(0)
    while q:
        a = q.popleft()
        for b in graph[a]:
            if b in visited: continue
        
            cnt[b] -= 1
            if cnt[b] == 0:
                visited.add(b)
                q.append(b)
    
    if len(visited) == n: return True
    else: return False

n = 9
path = 	[[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]]
order = [[8,5],[6,7],[4,1]]
print( solution(n, path, order) )
# true

n = 9
path = [[8,1],[0,1],[1,2],[0,7],[4,7],[0,3],[7,5],[3,6]]
order = [[4,1],[5,2]]
print( solution(n, path, order) )
# true

n = 9
path = 	[[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]]
order = [[4,1],[8,7],[6,5]]	
print( solution(n, path, order) )
# false