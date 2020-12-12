# 감시 피하기
# https://www.acmicpc.net/problem/18428
#
# (X, Y)
# X 행 -> 아래로 증가
# Y 열 -> 오른쪽으로 증가

TEACHER = 'T'
STUDENT = 'S'
EMPTY = 'X'
OBSTACLE = 'O'

N = int( input() )
globe = []
for i in range(N):
    globe.append( list(input().split()) )

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def ok(nx, ny):
    return 0 <= nx and nx < N and 0 <= ny and ny < N

def look_straight(x, y, dir):
    global globe
    nx = x
    ny = y
    while True:
        nx = nx + dx[dir]
        ny = ny + dy[dir]
        if not ok(nx, ny): return True
        if globe[nx][ny] == OBSTACLE: return True
        if globe[nx][ny] == STUDENT: return False

def watch(x, y):
    for dir in range(4):
        successful = look_straight(x, y, dir)
        if not successful: return False
    return True

###
def check_vision():
    global globe
    for x in range(N):
        for y in range(N):
            if globe[x][y] == TEACHER:
                successful = watch(x, y)
                if not successful: return False
    return True

def is_teacher_near(x, y):
    global globe
    for dir in range(4):
        nx = x + dx[dir]
        ny = y + dy[dir]
        if ok(nx, ny) and globe[nx][ny] == TEACHER:
            return True
    return False
###

for x in range(N):
    for y in range(N):
        if globe[x][y] == TEACHER:
            watch(x, y)

def place_obstacle_rec(X, Y, ob_idx):
    global globe

    if ob_idx == 3:
        successful = check_vision()
        if successful: return True
        else: return False

    x = X
    for y in range(Y + 1, N):
        if globe[x][y] == EMPTY:
            globe[x][y] = OBSTACLE
            successful = place_obstacle_rec(x, y, ob_idx + 1)
            if successful: return True
            globe[x][y] = EMPTY
    
    for x in range(X + 1, N):
        for y in range(N):
            if globe[x][y] == EMPTY:
                globe[x][y] = OBSTACLE
                successful = place_obstacle_rec(x, y, ob_idx + 1)
                if successful: return True
                globe[x][y] = EMPTY

    return False
    
def solve():
    for x in range(N):
        for y in range(N):
            successful = place_obstacle_rec(x, y, 0)
            if successful: return True
    return False

teacher = False
for x in range(N):
    for y in range(N):
        if globe[x][y] == STUDENT:
            teacher = is_teacher_near(x, y)
            if teacher: break
    if teacher: break

successful = False
if not teacher:
    successful = solve()

if successful: print('YES')
else: print('NO')
