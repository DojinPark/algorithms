# 화성 탐사

# 3
# 3
# 5 5 4
# 3 9 1
# 3 2 7
# 5
# 3 7 2 0 1
# 2 8 0 9 1
# 1 2 1 8 1
# 9 8 9 2 0
# 3 6 5 1 5
# 7
# 9 0 5 1 1 5 3
# 4 1 2 1 6 5 3
# 0 7 6 1 6 8 5
# 1 1 7 8 3 2 3
# 9 4 0 7 6 4 1
# 5 8 3 2 4 8 3
# 7 4 8 4 8 3 4

from heapq import heappush as push
from heapq import heappop as pop

INF = int(1e9)
N = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def ok(x, y):
    global N
    return x >= 0 and x < N and  y >= 0 and y < N

def next_xy(x, y):
    ret = []
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if ok(nx, ny):
            ret.append( (nx, ny) )
    return ret

T = int( input() )
for test_case in range(1, T+1):
    N = int( input() )
    globe = []
    cost = [ [INF] * N for _ in range(N) ]
    for _ in range(N):
        line = list( map(int, input().split()) )
        globe.append(line)

    h = []
    x = 0
    y = 0
    c = globe[x][y]
    push(h, (c, x, y))
    while h:
        c, x, y = pop(h)
        for nx, ny in next_xy(x, y):
            if c + globe[nx][ny] < cost[nx][ny]:
                cost[nx][ny] = c + globe[nx][ny]
                push(h, (cost[nx][ny], nx, ny))
    print( cost[N-1][N-1] )
