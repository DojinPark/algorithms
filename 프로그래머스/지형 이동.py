# https://programmers.co.kr/learn/courses/30/lessons/62050
# 지형 이동
# 0:30

from heapq import heappush as push, heappop as pop

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def ok(N, x, y):
    return x >= 0 and x < N and y >= 0 and y < N

def get_root(roots, xy):
    x, y = xy
    if xy == roots[x][y]: return xy
    roots[x][y] = get_root(roots, roots[x][y])
    return roots[x][y]

def union(roots, xy, nxy):
    xy = get_root(roots, xy)
    nxy = get_root(roots, nxy)
    x, y = xy
    nx, ny = nxy
    if xy < nxy: roots[nx][ny] = xy
    else: roots[x][y] = nxy

def is_cycle(roots, xy, nxy):
    return get_root(roots, xy) == get_root(roots, nxy)

def solution(land, height):
    answer = 0
    N = len(land)
    h = []
    roots = [ [(x, y) for y in range(N)] for x in range(N) ]

    for x in range(N):
        for y in range(N):
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if not ok(N, nx, ny): continue

                diff = abs(land[x][y] - land[nx][ny])
                cost = 0 if diff <= height else diff

                push(h, (cost, (x, y), (nx, ny)))
    
    cnt = 0
    cnt_max = N * N - 1

    cost, xy, nxy = pop(h)
    union(roots, xy, nxy)
    answer += cost
    cnt = 1

    while h and cnt < cnt_max:
        cost, xy, nxy = pop(h)
        if not is_cycle(roots, xy, nxy):
            answer += cost
            union(roots, xy, nxy)
            cnt += 1

    return answer

land = [[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]]
height = 3
print( solution(land, height) )