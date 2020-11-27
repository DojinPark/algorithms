# 미래 도시

INF = int(1e9)

# 플로이드-워셜 알고리즘
def solve(V, E, edges, X, K):
    graph = [ [INF] * (V+1) for _ in range(V+1) ]
    for e in edges:
        a, b = map(int, e.split())
        graph[a][b] = 1
        graph[b][a] = 1     # 이거 안했다가 틀림
    for a in range(V+1):
        graph[a][a] = 0
    
    for a in range(1, V+1):
        for b in range(1, V+1):
            for k in range(1, V+1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
    
    answer = graph[1][K] + graph[K][X]
    if answer <= INF:
        return answer
    else:
        return -1


V, E = 5, 7
edges = {
    '1 2',
    '1 3',
    '1 4',
    '2 4',
    '3 4',
    '3 5',
    '4 5',
}
X, K = 4, 5
# 3
print(solve(V, E, edges, X, K))

V, E = 4, 2
edges = {
    '1 3',
    '2 4'
}
X, K = 3, 4
# -1
print(solve(V, E, edges, X, K))
