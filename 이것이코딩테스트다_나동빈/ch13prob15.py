# 특정 거리의 도시 찾기
# https://www.acmicpc.net/problem/18352

answer = []

INF = int(1e9)

import sys

N, M, K, X = map(int, sys.stdin.readline().rstrip().split())
E = [ [] for _ in range(N + 1) ]
dist = [INF] * (N + 1)
for _ in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    E[a].append(b)

from collections import deque
q = deque()
q.appendleft(X)
dist[X] = 0

while q:
    a = q.pop()
    for b in E[a]:
        if dist[b] == INF and dist[a] + 1 <= K:
            q.appendleft(b)
            dist[b] = dist[a] + 1
            if (dist[b] == K):
                answer.append(b)
if answer:
    answer.sort()
    for a in answer:
        print(a)
else:
    print(-1)
    