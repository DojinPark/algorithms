# 블록 이동하기
# https://programmers.co.kr/learn/courses/30/lessons/60063

EMPTY = 0
WALL = 1
INF = int(1e9)

X, Y = 0, 0
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
drx = [1, -1, -1, 1]
dry = [1, 1, -1, -1]

def ok(nxy):
    global X, Y
    (nx1, ny1), (nx2, ny2) = nxy 
    return (0 <= nx1 and nx1 < X and 0 <= ny1 and ny1 < Y) \
    and (0 <= nx2 and nx2 < X and 0 <= ny2 and ny2 < Y)


def move(xy, d):
    (x1, y1), (x2, y2) = xy
    nxy = [x1 + dx[d], y1 + dy[d]], [x2 + dx[d], y2 + dy[d]]
    if not ok(nxy): return False

    return nxy

def rotate(xy, sel, d):
    [ax, ay], [rx, ry] = xy[sel], xy[not sel]
    nrx = rx + drx[d]
    nry = ry + dry[d]
    if abs(ax - nrx) + abs(ay - nry) != 1: return False

    nxy = [ [ax, ay], [nrx, nry] ]
    if not ok(nxy): return False

    return nxy

def get_a_idx(xy):
    [ax, ay], [rx, ry] = xy
    if ax == rx:
        if ay < ry: return 0    # 축아래
        else: return 1
    if ay == ry:
        if ax < rx: return 2    # 축오른쪽
        else: return 3

from copy import deepcopy
from collections import deque
def solution(board):
    global X, Y
    X = len(board)
    Y = len(board[0])
    A = [ [[INF]*4 for y in range(Y)] for x in range(X) ]
    q = deque()

    xy = [ [0, 0], [1, 0] ]
    a_idx = get_a_idx(xy)
    A[0][0][a_idx] = 0
    q.appendleft(xy)
    while q:
        xy = q.pop()
        a_xy = get_a_idx(xy)
        x, y = xy[0]
        cost = A[x][y][a_xy] + 1

        # 직선 방향으로 움직이는 경우
        for d in range(4):
            nxy = move(xy, d)

            if not nxy: continue
            impossible = False
            for sel in range(2):
                checkx, checky = nxy[sel]
                if board[checkx][checky] == WALL: impossilbe = True
            if impossible: continue

            a_nxy = get_a_idx(nxy)
            nx, ny = nxy[0]
            if cost < A[nx][ny][a_nxy]:
                A[nx][ny][a_nxy] = cost
                q.appendleft(nxy)
            
        # 회전 하는 경우
        for d in range(4):
            for sel in range(2):
                nxy = rotate(xy, sel, d)

                if not nxy: continue
                impossible = False
                for sel in range(2):
                    checkx, checky = nxy[sel]
                    if board[checkx][checky] == WALL: impossilbe = True
                if impossible: continue

                a_nxy = get_a_idx(nxy)
                nx, ny = nxy[0]
                if cost < A[nx][ny][a_nxy]:
                    A[nx][ny][a_nxy] = cost
                    q.appendleft(nxy)
        
        for a_idx in range(4):
            if A[X-1][Y-1][a_idx] != INF:
                return A[X-1][Y-1][a_idx]
        if A[X-1][Y-2][0] != INF: 
            return A[X-1][Y-2][0]
        if A[X-2][Y-1][2] != INF: 
            return A[X-2][Y-1][2]
            
    return -1

# board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
# print( solution(board) )
# # 7