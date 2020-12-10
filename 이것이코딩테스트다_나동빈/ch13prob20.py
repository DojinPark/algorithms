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
        if not ok(nx, ny): return False
        if globe[nx][ny] == OBSTACLE: return False
        if globe[nx][ny] == STUDENT: return True

def watch(x, y):
    for dir in range(4):
        fail = look_straight(x, y, dir)
        if fail: return True
    return False

###
def check_vision():
    global globe
    for x in range(N):
        for y in range(N):
            if globe[x][y] == TEACHER:
                fail = watch(x, y)
                if fail: return True
    return False

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

teacher = False
for x in range(N):
    for y in range(N):
        if globe[x][y] == STUDENT:
            teacher = is_teacher_near(x, y)
            if teacher: break
    if teacher: break

def solve(X = 0, Y = 0, ob_idx = 1):
    global globe

    if ob_idx == 3:
        fail = check_vision()
        if not fail: return True
        else: return False

    x = X
    for y in range(Y + 1, N):
        if globe[x][y] == EMPTY:
            globe[x][y] = OBSTACLE
            fail = solve(x, y, ob_idx + 1)
            if not fail: return True
            globe[x][y] = EMPTY
    
    for x in range(x + 1, N):
        for y in range(N):
            if globe[x][y] == EMPTY:
                globe[x][y] = OBSTACLE
                fail = solve(x, y, ob_idx + 1)
                if not fail: return True
                globe[x][y] = EMPTY

    return False

successful = False
if not teacher:
    successful = solve()

if successful: print('YES')
else: print('NO')