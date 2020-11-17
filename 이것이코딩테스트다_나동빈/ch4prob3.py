# 게임 개발
#
# 실수 방지하는 원칙
# 문제에서 설정한 행과 열의 순서를 따르지 말고
# [행][열]의 순서는 항상 일정하게 코딩하기
# 단, 입력의 순서가 그와 다른 경우를 고려해서 입력받기

# 4 4
# 1 1 0
# 1 1 1 1
# 1 0 0 1
# 1 1 0 1
# 1 1 1 1

globe = []
dirs = [(0,1), (1,0), (0,-1), (-1,0)]

N, M = map(int, input().rstrip().split())
R, C, d = map(int, input().rstrip().split())

globe = [ [0]*N for _ in range(M) ]
visited = [ [0]*N for _ in range(M) ]

for r in range(M):
    globe[r] = list(map(int, input().rstrip().split()))

def ok(pos):
    global globe, visited
    global N, M
    r = pos[0]
    c = pos[1]
    if r >= N or r < 0: return False
    if c >= M or c < 0: return False
    if globe[r][c] == 1: return False
    if visited[r][c] == 1: return False
    return True

def is_land(pos):
    global globe
    global N, M
    r = pos[0]
    c = pos[1]
    if r >= N or r < 0: return False
    if c >= M or c < 0: return False
    if globe[r][c] == 1: return False
    return True

def go(pos):
    global dirs
    r = pos[0] + dirs[pos[2]][0]
    c = pos[1] + dirs[pos[2]][1]
    return (r, c, pos[2])

def go_back(pos):
    global dirs
    r = pos[0] - dirs[pos[2]][0]
    c = pos[1] - dirs[pos[2]][1]
    return (r, c, pos[2])

def turn(pos):
    r, c, d = pos
    d = (d + 1)%4
    return (r, c, d)

pos = (R, C, d)
while True:
    moved = False
    for _ in range(4):
        pos = turn(pos)
        if ok(go(pos)):
            pos = go(pos)
            visited[pos[0]][pos[1]] = True
            moved = True
            break
    if not moved:
        if is_land(go_back(pos)):
            pos = go_back(pos)
        else:  
            break

answer = 0
for r in range(N):
    for c in range(M):
        if visited[r][c]:
            answer += 1

print(answer)