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
distance = [INF] * (V + 1)

graph = [ [] for _ in range(V+1) ]
for e in edges:
    a, b, c = map(int, e.split())
    graph[a].append( (b, c) )

from heapq import heappush as push
from heapq import heappop as pop

# O(E logV)
# 단순한 다익스트라 알고리즘은 다음 정점을 인덱스 순서로 결정하는 반면
# 개선된 다익스트라 알고리즘은 (정점, 다음 간선
def djikstra(start):
    global distance
    global graph

    q = []
    push(q, (start, 0))
    distance[start] = 0
    while q:
        v, d = pop(q)

        if distance[v] < d:
            continue

        for e in graph[v]:
            cost = d + e[1]
            if cost < distance[e[0]]:
                distance[e[0]] = cost
                push(q, (e[0], cost))

djikstra(start)

for v in range(1, V+1):
    if distance[v] == INF:
        print('INF', end=' ')
    else:
        print(distance[v], end=' ')
