# 연구소
# https://www.acmicpc.net/problem/14502

EMPTY = 0
WALL = 1
VIRUS = 2
INFECTED = 3
INF = int(1e9)
DX = [-1, 1, 0, 0]
DY = [0, 0, -1, 1]

import sys
from collections import deque
from copy import deepcopy

# 입력
N, M = map(int, sys.stdin.readline().rstrip().split())
globe = [ [] for _ in range(N) ]
for i in range(N):
    globe[i] = list( map(int, sys.stdin.readline().rstrip().split()) )

# 초기 변수 정리
virus_count = 0
wall_count = 0
for x in range(N):
    for y in range(M):
        if globe[x][y] == WALL:
            wall_count += 1
        elif globe[x][y] == VIRUS:
            virus_count += 1
# 초기 바이러스 위치 찾기
viruses = []
for x in range(N):
    for y in range(M):
        if globe[x][y] == VIRUS:
            viruses.append( (x,y) )

def ok(x, y):
    return 0 <= x and x < N and 0 <= y and y < M

def bfs(N, M, globe, walls):
    globe = deepcopy(globe)

    # 세개의 벽 추가
    for wall in walls:
        x, y = wall
        globe[x][y] = WALL
    
    # bfs 바이러스 전염
    q = deque()
    for v in viruses:
        q.appendleft(v)
        x, y = v
    
    infection_count = 0
    while q:
        x, y = q.pop()
        for i in range(4):
            dx, dy = DX[i], DY[i]
            xx, yy = x + dx, y + dy
            if ok(xx, yy) and globe[xx][yy] == EMPTY:
                q.appendleft( (xx, yy) )
                globe[xx][yy] = INFECTED
                infection_count += 1
    
    # 안전지대 계산
    safe_zone = N * M - virus_count - wall_count - 3 - infection_count
    return safe_zone

# 세개의 벽 조합 만들어 두기
X = [x for x in range(0, N)]
Y = [y for y in range(0, M)]

from itertools import product
from itertools import combinations

XY = list( product(X, Y) )
XY_set = list( combinations(XY, 3) )

max_safe_zone = 0
for walls in XY_set:
    max_safe_zone = max(max_safe_zone, bfs(N, M, globe, walls))

print(max_safe_zone)