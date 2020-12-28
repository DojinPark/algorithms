# 플로이드
# https://www.acmicpc.net/problem/11404

INF = 10000001   # N의 최대 100 * 간선 비용의 최대 100,000

import sys

N = int( input() )
M = int( input() )
e = [ [INF] * N for _ in range(N) ]
for _ in range(M):
    #a, b, c = map(int, input().split())
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    a -= 1
    b -= 1
    e[a][b] = min(e[a][b], c) # 같은 경로상에서 비용이 더 큰 버스 노선은 제외

# 일반적인 플로이드-워셜 알고리즘
for k in range(N):
    for a in range(N):
        for b in range(N):
            if a == b: continue
            if a == k: continue
            if b == k: continue
            e[a][b] = min(e[a][b], e[a][k] + e[k][b])

for a in range(N):
    for b in range(N):
        if e[a][b] == INF:
            e[a][b] = 0

for a in range(N):
    for b in range(N):
        print(e[a][b], end=' ')
    print()
            
