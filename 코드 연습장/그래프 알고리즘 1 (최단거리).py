
V = 6
start = 1
edges = [    # 단방향 그래프
    '1 2 2', # from, to, cost
    '1 3 5',
    '1 4 1',
    '2 3 3',
    '2 4 2',
    '3 2 3',
    '3 6 5',
    '4 3 3',
    '4 5 1',
    '5 3 1',
    '5 6 2',
    '5 1 5',
    '6 2 6',
]



INF = int(1e9)

# 다익스트라 알고리즘
# - 시작 노드 부터 다른 모든 노드 까지의 최단 거리를 구하는 알고리즘
# 원리
# - 시작 노드로 부터의 최소 거리를 알고있는 노드만을 포함한 sub-graph를
#   이미 최단거리 문제가 해결된 그래프로 생각하는 그리디 알고리즘이다.
# - 또한, 각 노드까지의 최소거리와 문제해결 여부(visited)를
#   따로 저장하는 다이내믹 프로그래밍 알고리즘이다.
# 알고리즘
# - 시작 노드 하나만을 포함한 그래프를 이미 문제가 해결된 그래프로
#   생각하여 시작한다.
# - 문제가 해결된 sub-graph의 아무 노드로 부터 거리가 가장 가까운 노드를
#   sub-graph에 새롭게 포함시킨다.
# - 모든 노드가 포함될 때 까지 반복한다.

# 일반적인 다익스트라
def shortest_path(V, edges_str, start):
    edges = [ [] for _ in range(V + 1) ]
    for edge_str in edges_str:
        a, b, c = map(int, edge_str.split())
        edges[a].append( (c, b) )

    visited = [False] * (V + 1)
    costs = [INF] *  (V + 1)

    a = start
    visited[a] = True
    costs[a] = 0

    for _ in range(V - 1):
        for c, b in edges[a]:
            costs[b] = min(costs[b], c + costs[a])
        
        min_v, min_c = 0, INF
        for v in range(1, V + 1):
            if not visited[v] and costs[v] < min_c:
                min_v = v
                min_c = costs[v]
        
        visited[min_v] = True
        a = min_v
    
    return costs

# expected output: 0 2 3 1 2 4
costs = shortest_path(V, edges, start)
print(costs)
print()

# 힙을 이용한 다익스트라
# sub-graph에서 뻗어 나가는 모든 간선을 확인하는 
# 
from heapq import heappush as push, heappop as pop

def shortest_path(V, edges_str, start):
    edges = [ [] for _ in range(V + 1) ]

    for edge_str in edges_str:
        a, b, c = map(int, edge_str.split())
        edges[a].append( (c, b) )
    
    costs = [INF] * (V + 1)
    h = []

    costs[start] = 0
    push(h, (0, start)) # (마지막으로 방문한 노드까지의 최소 거리, 마지막으로 방문한 노드)
    while h:
        cost, a = pop(h)
        
        if cost > costs[a]: continue   # 이미 방문한 노드 처리, 불필요한 메모리 쓰기를 방지한다.
        # for c, b in edges[a]:                       # 기존 다익스트라 알고리즘에서 이 부분이
        #     costs[b] = min(costs[b], c + costs[a])  # 메모리 쓰기를 많이 하게 된다
                                                      
        for c, b in edges[a]:
            if costs[b] > c + cost:
                costs[b] = c + cost
                push(h, (c + cost, b))
        # min_v, min_c = 0, INF
        # for v in range(1, V + 1):
        #     if not visited[v] and costs[v] < min_c:
        #         min_v = v
        #         min_c = costs[v]

    return costs

costs = shortest_path(V, edges, start)
print(costs)
print()


# 크루스칼 알고리즘
# - 인덱스 루프 순서가 k, a, b 여야 하는 이유는 논문으로 증명될
#   정도로 복잡하니 그냥 외우면 된다.
# -> 그만큼 면접 질문으로 활용될 가능성도 적다.
def shortest_path_all_pairs(V, edges_str, start):
    mat = [ [(0 if a == b else INF) for a in range(V + 1)] for b in range(V + 1) ]
    for edge_str in edges_str:
        a, b, c = map(int, edge_str.split())
        mat[a][b] = c

    for k in range(1, V + 1):
        for a in range(1, V + 1):
            for b in range(1, V + 1):
                mat[a][b] = min(mat[a][b], mat[a][k] + mat[k][b])
    
    return mat
    
costs = shortest_path_all_pairs(V, edges, start)
for a in range(1, V + 1):
    for b in range(1, V + 1):
        print( costs[a][b], end=' ' )
    print()
print()