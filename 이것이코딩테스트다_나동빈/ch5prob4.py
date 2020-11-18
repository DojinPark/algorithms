# 미로 탈출

# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111
#
# 10

N, M = 0, 0
globe = [[]]
steps = [[]]

N, M = map(int, input().split())
globe = [ [] for _ in range(N) ]
for r in range(N):
    globe[r] = [int(c) for c in input()]
steps = [ [0]*M for _ in range(N) ]

def bound(rc):
    global N, M
    r, c = rc
    return (0 <= r and r < N) and (0 <= c and c < M)

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
def next(rc, i):
    global dr, dc
    r, c = rc
    return r + dr[i], c + dc[i]

from collections import deque
def bfs(rc):
    global globe
    r, c = rc
    q = deque()
    steps[r][c] = 1 # steps count
    q.appendleft(rc)
    while len(q):
        rc = q.pop()
        r, c = rc  # 이거 안해서 실수냈다!
        for i in range(4):
            n_rc = next(rc, i)
            n_r, n_c = n_rc
            if bound(n_rc) and globe[n_r][n_c] and not steps[n_r][n_c]:
                steps[n_r][n_c] = steps[r][c] + 1
                q.appendleft(n_rc)
        if steps[N-1][M-1]:
            break
    return steps[N-1][M-1]

answer = bfs( (0,0) )
print(answer)