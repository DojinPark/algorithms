
# 크루스칼 알고리즘
#
# - 최소 신장 트리 알고리즘
# - 그리디 알고리즘
#
# 모든 간선을 오름차순으로 정렬
# 작은 간서부터 하나씩,
#   사이클을 발생시키지 않으면 그래프에 추가
# 추가한 간선의 개수가 V-1개 일 때 까지 반복
#
# O(E logE)
# - 간선을 가중치에 따라 정렬하는데 드는 시간 복잡도
# - 간선 추가시 사이클 발생 여부 검출에 드는 시간은 작으므로 무시

V, E = 7, 9
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

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

parent = [i for i in range(V+1)]
edges = []
for estr in edges_str:
    a, b, c = map(int, estr.split())
    edges.append( (c, a, b) )

edges.sort()    # 간선 비용을 튜플의 첫번째 항으로 두면 .sort(key=lambda x: x[키 인덱스]) 처럼 람다를 사용하지 않고 정렬할 수 있다.

total_cost = 0
added = 0
for edge in edges:
    c, a, b = edge
    
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        total_cost += c
        added += 1
        if added == V-1:
            break

print('크루스칼 알고리즘')
print(total_cost)






# 위상 정렬
#
# 정해져 있는 일련의 작업을 차례대로 수행해야 할 때 사용
#
# ! 진입차수: 한 노드로 들어오는 방향의 간선 개수
#
# 진입차수가 0 인 노드를 큐에 넣는다
# 큐가 빌 떄 까지
#   큐에서 노드를 하나 꺼내고 그 노드에서 출발하는 모든 간선을 제거한다
#   이후 진입차수가 새롭게 0 이 된 노드를 큐에 넣는다.
#
# O(V + E)  모든 노드에 대해 작업함 + 모든 간선을 하나씩 제거함
from collections import deque

V, E = 7, 8
edges_str = [
    '1 2',
    '1 5',
    '2 3',
    '2 6',
    '3 4',
    '4 7',
    '5 6',
    '6 4'
]
# 1 2 5 3 6 4 7

indegree = [0] * (V + 1)
graph = [ [] for _ in range(V + 1) ]

for edge_str in edges_str:
    a, b = map(int, edge_str.split())
    graph[a].append(b)
    indegree[b] += 1

result = []
q = deque()

for i in range(1, V + 1):
    if indegree[i] == 0:
        q.appendleft(i)

while q:
    now = q.pop()
    result.append(now)

    for b in graph[now]:
        indegree[b] -= 1
        if indegree[b] == 0:
            q.appendleft(b)

print('\n위상 정렬')
print(result)



# 노트: 크루스칼 VS 프림 알고리즘
#
# Kruskal vs Prim
# O(E logE) vs O(V^2) ( O(V logE) )
# Sparse Graph vs Dense Graph
#
#
# Kruskal's 알고리즘
# "간선 기준 MST 알고리즘"
# 비용이 작은 간선 순서로, 사이클을 형성하지 않을 때 마다 연결하여 총 V-1 개의 간선을 연결.
# 시간 복잡도: O(E logE) (간선 정렬 시간)
# 
#
# Prim's 알고리즘
# "정점 기준 MST 알고리즘"
# 아무 정점에서나 시작한다. 그 정점에 연결된 간선 중 비용이 가장 작으면서 아직 방문하지 않은 정점과 연결 된 것을 연결한다. 새롭게 연결된 정점에서 같은 동작을 반복하여 총 V개의 정점을 방문.
# 시간 복잡도: O(V^2) -> 힙 이용 시 O(V logE)