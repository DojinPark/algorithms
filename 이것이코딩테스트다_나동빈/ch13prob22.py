# 블록 이동하기
# https://programmers.co.kr/learn/courses/30/lessons/60063

# EMPTY = 0
# WALL = 1
# INF = int(1e9)

# X, Y = 0, 0
# dx = [0, 1, 0, -1]
# dy = [-1, 0, 1, 0]
# drx = [1, -1, -1, 1]
# dry = [1, 1, -1, -1]

# def ok(nxy):
#     global X, Y
#     (nx1, ny1), (nx2, ny2) = nxy 
#     return (0 <= nx1 and nx1 < X and 0 <= ny1 and ny1 < Y) \
#     and (0 <= nx2 and nx2 < X and 0 <= ny2 and ny2 < Y)


# def move(xy, d):
#     (x1, y1), (x2, y2) = xy
#     nxy = [x1 + dx[d], y1 + dy[d]], [x2 + dx[d], y2 + dy[d]]
#     if not ok(nxy): return False

#     return nxy

# def rotate(xy, sel, d):
#     [ax, ay], [rx, ry] = xy[sel], xy[not sel]
#     nrx = rx + drx[d]
#     nry = ry + dry[d]
#     if abs(ax - nrx) + abs(ay - nry) != 1: return False

#     nxy = [ [ax, ay], [nrx, nry] ]
#     if not ok(nxy): return False

#     return nxy

# def get_a_idx(xy):
#     [ax, ay], [rx, ry] = xy
#     if ax == rx:
#         if ay < ry: return 0    # 축아래
#         else: return 1
#     if ay == ry:
#         if ax < rx: return 2    # 축오른쪽
#         else: return 3

# from copy import deepcopy
# from collections import deque
# def solution(board):
#     global X, Y
#     X = len(board)
#     Y = len(board[0])
#     A = [ [[INF]*4 for y in range(Y)] for x in range(X) ]
#     q = deque()

#     xy = [ [0, 0], [1, 0] ]
#     a_idx = get_a_idx(xy)
#     A[0][0][a_idx] = 0
#     q.appendleft(xy)
#     while q:
#         xy = q.pop()
#         a_xy = get_a_idx(xy)
#         x, y = xy[0]
#         cost = A[x][y][a_xy] + 1

#         # 직선 방향으로 움직이는 경우
#         for d in range(4):
#             nxy = move(xy, d)

#             if not nxy: continue
#             impossible = False
#             for sel in range(2):
#                 checkx, checky = nxy[sel]
#                 if board[checkx][checky] == WALL: impossilbe = True
#             if impossible: continue

#             a_nxy = get_a_idx(nxy)
#             nx, ny = nxy[0]
#             if cost < A[nx][ny][a_nxy]:
#                 A[nx][ny][a_nxy] = cost
#                 q.appendleft(nxy)
            
#         # 회전 하는 경우
#         for d in range(4):
#             for sel in range(2):
#                 nxy = rotate(xy, sel, d)

#                 if not nxy: continue
#                 impossible = False
#                 for sel in range(2):
#                     checkx, checky = nxy[sel]
#                     if board[checkx][checky] == WALL: impossilbe = True
#                 if impossible: continue

#                 a_nxy = get_a_idx(nxy)
#                 nx, ny = nxy[0]
#                 if cost < A[nx][ny][a_nxy]:
#                     A[nx][ny][a_nxy] = cost
#                     q.appendleft(nxy)
        
#         for a_idx in range(4):
#             if A[X-1][Y-1][a_idx] != INF:
#                 return A[X-1][Y-1][a_idx]
#         if A[X-1][Y-2][0] != INF: 
#             return A[X-1][Y-2][0]
#         if A[X-2][Y-1][2] != INF: 
#             return A[X-2][Y-1][2]
            
#     return -1

# # board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
# # print( solution(board) )
# # # 7

from collections import deque

INF = int(1e9)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
N = 0
rotate_to_vertical_dx = [0, 0, 1, 1]
rotate_to_vertical_dy = [-1, 0, -1, 0]
check_board_to_vertical_dx = [1, 1, 0, 0]
check_board_to_vertical_dy = [-1, 1, -1, 1]
rotate_to_horizontal_dx = [0, 0, -1, -1]
rotate_to_horizontal_dy = [0, 1, 0, 1]
check_board_to_horizontal_dx = [1, 1, -1, -1]
check_board_to_horizontal_dy = [1, 0, 1, 0]

def ok(nx, ny):
    return nx >=0 and nx < N and ny >= 0 and ny < N

def get_other_xy(x, y, vertical):
    if vertical:
        return x, y + 1
    else:
        return x + 1, y

def get_move(board, x, y, vertical):
    ret = []

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        other_x, other_y = get_other_xy(nx, ny, vertical)
        if ok(nx, ny) and ok(other_x, other_y) and not board[nx][ny] and not board[other_x][other_y]:
            ret.append( (nx, ny, vertical) )
    
    return ret

def get_rotate(board, x, y, vertical):
    ret = []
    
    new_direction = not vertical
    for i in range(4):
        if vertical:
            nx = x + rotate_to_horizontal_dx[i]
            ny = y + rotate_to_horizontal_dy[i]
            check_x = x + check_board_to_horizontal_dx[i]
            check_y = y + check_board_to_horizontal_dy[i]
        else:
            nx = x + rotate_to_vertical_dx[i]
            ny = y + rotate_to_vertical_dy[i]
            check_x = x + check_board_to_vertical_dx[i]
            check_y = y + check_board_to_vertical_dy[i]
        other_x, other_y = get_other_xy(nx, ny, new_direction)
        if ok(nx, ny) and ok(other_x, other_y) and ok(check_x, check_y) and not board[nx][ny] and not board[other_x][other_y] and not board[check_x][check_y]:
            ret.append( (nx, ny, new_direction) )
    
    return ret

def solution(board):
    global N
    N = len(board)

    steps = [ [[INF] * 2 for _ in range(N)] for _ in range(N) ]
    q = deque()

    steps[0][0][0] = 0
    q.append( (0, 0, 0) )

    while q:
        x, y, vertical = q.popleft()
        steps_now = steps[x][y][vertical]

        nex = get_move(board, x, y, vertical)
        nex += get_rotate(board, x, y, vertical)

        for nx, ny, nvertical in nex:
            if steps[nx][ny][nvertical] > steps_now + 1:
                steps[nx][ny][nvertical] = steps_now + 1
                q.append( (nx, ny, nvertical) )
        
        if steps[N-2][N-1][0] != INF:
            return steps[N-2][N-1][0]
        if steps[N-1][N-2][1] != INF:
            return steps[N-1][N-2][1]