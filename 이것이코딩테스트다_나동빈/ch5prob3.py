# 음료수 얼려먹기

# 4 5
# 00110
# 10001
# 01011
# 00100
#
# 5

from collections import deque

globe = []
N, M = 0, 0

N, M = map(int, input().split())
# [] * N 으로 하면 [] obj 가 복사되지 않음.
# [ [] for _ in range(N) ] 으로 선언해야만 이중 리스트가 생성된다
globe = [0] * N

for r in range(N):
    globe[r] = [c for c in input()]

# 이차원 좌표 처럼 함수간 전달할 정보의 개수가 두개 이상인 경우
# - 항상 튜플로 전달하기
# - 전달 받은 뒤 튜플에서 꺼내서 쓰기
# >>> 함수 안이 아니라 밖에서 더 간결한 코드를 쓰고 실수를 방지하기 위해서!
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

# dfs, bfs 구현 시 실수 주의!
# 1. dfs 구현시 stack에서 꺼낼 때 방문 했음을 표시
# 2. bfs 구현시 queue에 넣을 때 방문 했음을 표시
def bfs(rc):
    global globe
    r, c = rc
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
            bfs((r,c))
            answer += 1

print(answer)

