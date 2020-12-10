# 경쟁적 전염
# https://www.acmicpc.net/problem/18405
#
# X 행 아래로
# Y 열 오른쪽으로
# index 1 부터 -> 0 부터로 수정

# 입력
import sys
N, K = map(int, sys.stdin.readline().rstrip().split())
globe = [ [] for _ in range(N) ]
for i in range(N):
    globe[i] = list( map(int, sys.stdin.readline().rstrip().split()) )
S, X, Y = map(int, sys.stdin.readline().rstrip().split())
X -= 1
Y -= 1

# 큐 초기화
from collections import deque
q = [deque(), deque()]
sel = 0

initial = []
for x in range(N):
    for y in range(N):
        if globe[x][y]:
            initial.append( (globe[x][y], x, y) )
initial.sort()

for init in initial:
    k, x, y = init
    q[sel].appendleft( (k, x, y) )


# BFS
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def ok(nx, ny):
    return 0 <= nx and nx < N and 0 <= ny and ny < N

s = 0
while s < S and globe[X][Y] == 0:
    while q[sel]:
        k, x, y = q[sel].pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if ok(nx, ny) and globe[nx][ny] == 0:
                globe[nx][ny] = k
                q[not sel].appendleft( (k, nx, ny) )
    sel = not sel
    s += 1

print(globe[X][Y])

