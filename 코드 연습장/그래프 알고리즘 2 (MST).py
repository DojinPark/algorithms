# 크루스칼 vs 프림
# - 간선 중심 vs 정점 중심
# - O(E logE) vs O(E logV)
#
# 구현 비교
# - [간선 리스트 vs 인접 리스트]
#   (list of (c, a, b)  vs  list of edges[a] = (c, b))
#
# - [정렬 vs 힙]
#   간선 리스트 정렬  vs  정점 방문 마다 연결된 간선 힙에 push
#
# - [union-find vs visited]
#   알고리즘으로 사이클 확인  vs  정점 방문 마다 visited 행렬에 표시
#
# 공통점
# - 일반적으로, 무방향성 간선으로 출제됨

V = 7
edges_str = [
    '1 2 29',
    '1 5 75',
    '2 3 35',
    '2 6 34',
    '3 4 7',
    '4 6 23',
    '4 7 13',
    '5 6 53',
    '6 7 25'
]
# Expected Output: 159

# 크루스칼 알고리즘을 구현하기 이전에 외워야하는
# union-find 서로소 집합 함수 두가지와 is_cycle 함수
# 정점을 중심으로 확장해나가는 알고리즘이 아니기 때문에 cycle 확인 함수가 필요하다.
def get_root(roots, i): # (find 함수)
    if roots[i] == i: return i
    else:
        roots[i] = get_root(roots, roots[i])
        return roots[i]

def union(roots, i, j):
    i = get_root(roots, i)
    j = get_root(roots, j)
    if i < j:
        roots[j] = i
    else:
        roots[i] = j

def is_cycle(roots, i, j):
    return get_root(roots, i) == get_root(roots, j)

# 크루스칼 알고리즘의 코드 바디 자체는 간단하다.
# 모든 간선을 가중치가 작은 것 부터 정렬 한 후,
# 사이클이 형성 되지 않는 간선이면 추가한다.
def kruskal(V, edges_str):
    edges = [ map(int, e.split()) for e in edges_str ]
    edges = [ (c, a, b) for a, b, c in edges ]
    roots = [ i for i in range(V + 1) ]
    
    total = 0
    cnt = 0

    edges.sort() # O(E logE)
    
    for c, a, b in edges:
        if not is_cycle(roots, a, b):
            total += c
            cnt += 1
            if cnt == V - 1: break
            union(roots, a, b)

    return total

print( kruskal(V, edges_str) )


# 프림 알고리즘
from heapq import heappush as push, heappop as pop
def prim(V, edges_str):
    edges = [ [] for _ in range(V + 1) ]
    visited = [False] * (V + 1)
    h = []

    for edge_str in edges_str:
        a, b, c = map(int, edge_str.split())
        edges[a].append( (c, b) )
        edges[b].append( (c, a) )

    total = 0
    a = 1
    visited[a] = True
    
    for i in range(V - 1):
        for e in edges[a]:
            push(h, e)
        
        while h:
            c, b = pop(h)
            if not visited[b]:
                visited[b] = True
                total += c
                a = b
                break
    
    return total

print( prim(V, edges_str) )