# 음료수 얼려먹기

from collections import deque

globe = []
N, M = 0, 0

N, M = map(int, input().split())
globe = [0] * N

for r in range(N):
    globe[r] = [c for c in input()]

def bound(rc):
    global N, M
    r, c = rc
    return (0 <= r and r < N) and (0 <= c and c < M)

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
def adj_rc(rc, dir):
    global dr, dc
    r, c = rc
    return r + dr[dir], c + dc[dir]

def bfs(r, c):
    global globe
    q = deque()
    globe[r][c] = '0'
    q.appendleft( (r, c) )
    while len(q):
        rc = q.pop()
        for i in range(4):
            next_rc = adj_rc(rc, i)
            next_r, next_c = next_rc
            if bound(next_rc) and globe[next_r][next_c] == '1':
                globe[next_r][next_c] = '0'
                q.appendleft(next_rc)

answer = 0
for r in range(N):
    for c in range(M):
        if globe[r][c] == '1':
            bfs(r,c)
            answer += 1

print(answer)