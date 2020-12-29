# 다익스트라 Dijkstra 알고리즘
#
# 최적 경로 알고리즘은 그리디 알고리즘의 일종이다.
# "가장 비용이 적은 노드를 선택" 하는 과정을 반복하기 때문이다.
#
# - 음의 간선이 없어야 함
#
# 자다가도 일어나서 짤수 있도록 외워야한다.

INF = int(1e9)

V, E = 6, 11
start = 1
edges = [
    '1 2 2',
    '1 3 5',
    '1 4 1',
    '2 3 3',
    '2 4 2',
    '3 2 3',
    '3 6 5',
    '4 3 3',
    '4 5 1',
    '5 3 1',
    '5 6 2'
]
# expected output: 0 2 3 1 2 4


# 일반적인 다익스트라 알고리즘 구현
# O(V^2)
graph = [ [] for _ in range(V+1) ]
for e in edges:
    a, b, c = map(int, e.split())   # from "a" to "b" with cost "c"
    graph[a].append( (b, c) )
distance = [INF] * (V + 1)
visited = [False] * (V + 1)

def get_smallest_node():

    small_v, small_d = None, INF

    for v in range(1, V+1):
        if visited[v]:
            continue
        if distance[v] < small_d:
            small_v = v
            small_d = distance[v]
    
    return small_v

def dijkstra(start):

    v = start
    visited[v] = True
    distance[v] = 0

    # O(V)
    for _ in range(V-1):    # range(V) 까지 해서 get_smallest_node 에서 None 타입 반환받고 visited[v] = True 에서 인덱스 타입 오류 남
        for e in graph[v]:
            adjv, adjd = e
            cost = distance[v] + adjd   # 현재 정점까지의 최소거리 + 다음 간선의 가중치 (현재 정점까지의 최소거리 더하는거 잊지 말기!)
            if not visited[adjv] and cost < distance[adjv]:
                distance[adjv] = cost
        
        # O(V)
        v = get_smallest_node()
        visited[v] = True
    
dijkstra(start)

for v in range(1, V+1):
    if distance[v] == INF:
        print('INF', end=' ')
    else:
        print(distance[v], end=' ')
print()




# Heapq를 이용한 빠른 다익스트라 알고리즘 구현
#
# 코드에서 시간복잡도를 유추하면 1과 2 루프때문에 헷갈릴 수 있다.
# 하지만 간단히 생각할 때 E개의 간선을 heapq에 모두 넣고, 빼는( O(logE) ) 알고리즘이므로
# O(E logE) 이다.
#
# 그런데 E <= V^2 이므로
# = O(E logV^2)
# = O(E logV)
#
# E << V^2 인경우에 빠르게 동작한다.
graph = [ [] for _ in range(V+1) ]
for e in edges:
    a, b, c = map(int, e.split())
    graph[a].append( (b, c) )
distance = [INF] * (V + 1)
# visited 리스트가 필요없음

# O(E logV)
from heapq import heappush as push
from heapq import heappop as pop

def djikstra_fast(start):
    global distance
    global graph

    q = []
    distance[start] = 0
    push(q, (start, 0))

    # O(E)  -- [1]
    while q:
        # O(logE)
        v, d = pop(q)

        if distance[v] < d: # 거리가 더 멀어서 간선을 무시하는 경우, 이미 최소거리를 구해낸 정점인 경우가 이 조건문으로 처리됨
            continue

        # O(E)   -- [2]     시간 복잡도를 구할 때 루프[1]과 함께 O(E)로 계산되는 루프
        for e in graph[v]:
            adjv, adjd = e
            cost = d + adjd
            if cost < distance[adjv]:
                distance[adjv] = cost
                # O(logE)
                push(q, (adjv, cost))
    

djikstra_fast(start)

for v in range(1, V+1):
    if distance[v] == INF:
        print('INF', end=' ')
    else:
        print(distance[v], end=' ')
print('\n')







# 플로이드-워셜 알고리즘
#
# V개의 정점에 대해 이차원행렬 탐색 연산 O(V^2)을 수행해야하기 때문에
# O(V^3)
#
# 다익스트라 - 그리디 알고리즘
# 플로이드-워셜 - DP 알고리즘
#
# DP라서 코드가 진짜 간단
# for k: 1~V              -> O(V)
#   for all (a,b) pairs   -> O(V^2)
#     D(a,b) = min( D(a,k), D(k,b) )   -> DP 점화식
#
# 똑같이 동작하나?
# for all (a,b) pairs   -> O(V^2)
#   for k: 1~V          -> O(V)
#       D(a,b) = min( D(a,k), D(k,b) )   -> DP 점화식
V, E = 4, 7
edges = {
    '1 2 4',
    '1 4 6',
    '2 1 3',
    '2 3 7',
    '3 1 5',
    '3 4 4',
    '4 3 2'
}
# expected ouput:
# 0 4 8 6
# 3 0 7 9
# 5 9 0 4
# 7 11 2 0

graph = [ [INF] * (E+1) for _ in range(E+1) ]
for e in edges:
    a, b, c = map(int, e.split())
    graph[a][b] = c
for a in range(1, V+1):
    graph[a][a] = 0

for a in range(1, V+1):
    for b in range(1, V+1):
        for k in range(1, V+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, V+1):
    for b in range(1, V+1):
        print(graph[a][b], end=' ')
    print()