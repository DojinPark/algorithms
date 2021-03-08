N = 9
edges = [ [0, 1], [0, 2], [0, 3],
[1, 4], [1, 5],   [2, 6],   [3, 7], [3, 8] ]
cyclic_edges = [ [5, 3], [7, 1] ]

graph = [ [] for _ in range(N) ]
for a, b in edges:
    graph[a].append(b)

cyclic_graph = [ [] for _ in range(N) ]
for a, b in edges + cyclic_edges:
    cyclic_graph[a].append(b)

# 위상 정렬 알고리즘을 이용한 사이클 판별
from collections import deque
def topological_is_cycle(graph, edges):
    indegree = [0] * N
    visited = [False] * N
    q = deque()

    for a, b in edges:
        indegree[b] += 1

    visited[0] = True
    q.append(0)
    while q:
        a = q.popleft()
        for b in graph[a]:
            if visited[b]: continue
            indegree[b] -= 1
            if indegree[b] == 0:
                visited[b] = True
                q.append(b)

    for v in visited:
        if not v: return True
    return False

print('topological_is_cycle()')
print( topological_is_cycle(graph, edges) )
print( topological_is_cycle(cyclic_graph, cyclic_edges) )


# DFS cycle 판별 1: Global counter, order array, finished array
# 사이클 판별 및 순행, 역행, 교차 간선을 구분할 수 있는 알고리즘
counter = 0
def counter_dfs_is_cycle(graph, order, finished, a=0):
    global counter

    counter += 1
    order[a] = counter

    for b in graph[a]:
        if not order[b]:
            if counter_dfs_is_cycle(graph, order, finished, b):
                return True
        elif order[a] > order[b] and not finished[b]:
            return True # Back Edge
        # #-----------------------------------------#
        # elif order[a] > order[b] and finished[b]
        #     1 # Cross Edge 
        # else: # order[a] < order[b]:
        #     1 # Forward Edge
        # #-----------------------------------------#
    finished[a] = True
    
    return False

print( 'counter_dfs_is_cycle()' )
print( counter_dfs_is_cycle(graph, [0] * N, [False] * N) )
print( counter_dfs_is_cycle(cyclic_graph, [0] * N, [False] * N) )

# DFS cycle 판별 2: visited array, finished array
# 사이클 판별. 순행, 교차 간선을 판별할 수 있나?
def dfs_is_cycle(graph, visited, finished, a=0):
    visited[a] = True

    for b in graph[a]:
        if not visited[b]:
            if dfs_is_cycle(graph, visited, finished, b):
                return True
        elif visited[b] and not finished[b]:
            return True # Back Edge
        # elif visited[b] and finished[b]:
        #     1 # Cross Edge
        # #------------------------------#
    finished[a] = True
    return False

print( 'dfs_is_cycle()' )
print( dfs_is_cycle(graph, [False] * N, [False] * N) )
print( dfs_is_cycle(cyclic_graph, [False] * N, [False] * N) )


# 사이클 내의 정점 찾기
# "DFS cycle 판별 2"의 코드의 각 조건식에
# parent 행렬 표시와
# denote_cycle() 함수 추가
def denote_cycle(parent, is_cycle, a, b):
    is_cycle[a] = True
    
    if a == b: return

    denote_cycle(parent, is_cycle, parent[a], b)

def dfs_get_cyclic_nodes(graph, visited, finished, parent, a=0):
    visited[a] = True

    for b in graph[a]:
        if not visited[b]:
            parent[b] = a
            ret = dfs_get_cyclic_nodes(graph, visited, finished, parent, b)
            if ret: return ret

        elif visited[b] and not finished[b]:
            is_cycle = [False] * len(graph)
            denote_cycle(parent, is_cycle, a, b)
            return is_cycle
            
    finished[a] = True
    return []

print( 'dfs_get_cyclic_nodes()' )
print( dfs_get_cyclic_nodes(graph, [False] * N, [False] * N, [i for i in range(N)]) )
print( dfs_get_cyclic_nodes(cyclic_graph, [False] * N, [False] * N, [i for i in range(N)]) )
# 1, 3, 5, 7 번 노드