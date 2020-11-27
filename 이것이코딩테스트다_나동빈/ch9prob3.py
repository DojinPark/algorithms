# 전보

INF = int(1e9)

V, E, C = 3, 2, 1
edges = {
    '1 2 4',
    '1 3 2'
}

# 플로이드-워셜로 짜면 전보가 가쳐가는 길의 가중치 중복이 일어남
# 전보의 시작점이 하나다 + 전보는 도시를 하나씩 거쳐가면서 가중치가 누적된다 => 다익스트라 알고리즘

from heapq import heappush as push
from heapq import heappop as pop

graph = [ [] for _ in range(V+1) ]
for e in edges:
    a, b, c = map(int, e.split())
    graph[a].append( (b, c) )
    graph[b].append( (a, c) )

distance = [INF] * (V+1)
q = []

distance[C] = 0
push(q, (C, 0))

while q:
    now, nowc = pop(q)
    
    if distance[now] < nowc:
        continue
    
    for e in graph[now]:
        nextv, nextd = e
        nextc = nowc + nextd
        if distance[nextv] > nextc:
            distance[nextv] = nextc
            push(q, (nowc, nextc))


cnt = 0
max_cost = 0
for v in range(1, V+1):
    if distance[v] < INF and v != C:
        cnt += 1
        max_cost = max(max_cost, distance[v])

print(cnt, max_cost)