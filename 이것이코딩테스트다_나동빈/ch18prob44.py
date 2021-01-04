# 행성 터널
# https://www.acmicpc.net/problem/2887
#
# Prim's 알고리즘
# 한줄 설명: 아무 정점에서나 시작한다. 그 정점에 연결된 간선 중 비용이 가장 작으면서 아직 방문하지 않은 정점과 연결 된 것을 연결한다. 새롭게 연결된 정점에서 같은 동작을 반복한다.
# 시간 복잡도: O(V^2) -> 힙 이용 시 O(V logE)
#
# Kruskal vs Prim
# O(E logE) vs O(V^2) ( O(V logE) )
# Sparse Graph vs Dense Graph

INF = int(1e10)

import sys
from math import sqrt
from collections import deque

def get_dist(star_a, star_b):
    ax, ay, az = star_a
    bx, by, bz = star_b
    return min( (abs(ax - bx), abs(ay - by), abs(az - bz)) )
    

N = int(input())
stars = []
for _ in range(N):
    x, y, z = map(int, sys.stdin.readline().rstrip().split())
    stars.append( (x, y, z) )

total_cost = 0
V = [False] * N
now = 0
V[now] = True

for _ in range(N-1):
    min_dist = INF
    min_dist_v = -1
    
    for nex in range(N):
        if V[nex]: continue

        dist = get_dist(stars[now], stars[nex])

        if dist < min_dist:
            min_dist = dist
            min_dist_v = nex
    
    total_cost += min_dist
    V[min_dist_v] = True
    now = min_dist_v

print(total_cost)