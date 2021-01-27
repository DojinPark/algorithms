# 행성 터널
# https://www.acmicpc.net/problem/2887
#
# Kruskal's 알고리즘 문제이지만 거리의 정의에서 간선의 개수를 V^2 보다 훨씬 적게 추려낼 수 있는 문제
#
# 정렬이 필요한지 유추하는 법
# - 행성의 개수 100,000개 -> 프림 X (V^2 = 10,000,000,000)
# - 간선의 개수 10,000,000,000개 -> 크루스칼 X (E logE = 100,000,000,000)
# - 행성의 개수 100,000개 -> 정렬 O (V logV = 1,000,000)

def update_find_root(roots, a):
    if roots[a] != a:
        roots[a] = update_find_root(roots, roots[a])
    return roots[a]

def union(roots, a, b):
    a = update_find_root(roots, a)
    b = update_find_root(roots, b)
    if a < b:
        roots[b] = a
    else:
        roots[a] = b

def is_cycle(roots, a, b):
    return update_find_root(roots, a) == update_find_root(roots, b)

def solution(N, planets):
    planets = [ tuple( planets[i] + [i] ) for i in range(N) ]
    edges = []
    
    for dim in range(3):
        planets.sort(key=lambda p: p[dim])
        for i in range(N-1):
            edges.append( ( planets[i + 1][dim] - planets[i][dim], planets[i + 1][3], planets[i][3]) )
    
    edges.sort()

    roots = [ i for i in range(N) ]
    total_cost = 0
    connected = 0
    for edge in edges:
        cost, a, b = edge
        if is_cycle(roots, a, b): continue
        total_cost += cost
        union(roots, a, b)
        connected += 1
        if connected == N-1: break
    
    return total_cost


import sys
N = int(sys.stdin.readline().rstrip())
planets = []
for _ in range(N):
    line = list( map(int, sys.stdin.readline().rstrip().split()) )
    planets.append(line)

print( solution(N, planets) )