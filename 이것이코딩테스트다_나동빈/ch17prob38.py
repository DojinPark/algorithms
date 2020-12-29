# 정확한 순위

N, M = 6, 6
data = [
    (1, 5),
    (3, 4),
    (4, 2),
    (4, 6),
    (5, 2),
    (5, 4)
]
e = [  [[] for _ in range(N)] for __ in range(2) ]
for d in data:
    a, b = d
    a -= 1
    b -= 1
    e[0][a].append(b)
    e[1][b].append(a)

def dfs(e, v, x):
    ret = 1 # 한 노드를 방문 할 때 마다 카운트를 1 증가
    for y in e[x]:
        if not v[y]:
            v[y] = True
            ret += dfs(e, v, y) # 재귀 호출을 통해 ret 을 누적
    return ret

answer = 0

# 원리
# - 각 노드에서 간선의 정방향, 반대방향에 대하여 각각 dfs 탐색을 하여
# - 연결된 노드의 총 개수를 구한다.
# - 연결 된 노드의 개수 = N 이면 해당 노드는 순위를 확실히 정할 수 있다.
#
# 시간복잡도:
# - 정점 N = 500, 간선 M = 10,000
# - 각 정점에 대하여 최악의 경우 모든 간선을 확인 O(N * E) = 5,000,000
for start in range(N):
    v = [False] * N
    # dfs forwards
    forward = dfs(e[0], v, start)
    # dfs backwards
    backward = dfs(e[1], v, start)
    count = forward + backward - 1
    if count == N:
        answer += 1

print(answer)