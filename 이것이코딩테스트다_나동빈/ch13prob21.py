# 인구 이동
# https://www.acmicpc.net/problem/16234

# DFS 탐색 최대 limit
# N 이 최대 50 이고,
# 각 칸에서 최대 세칸 씩 recursion 이 일어나는 경우
# 3 * 50 ** 2 = 7,500
import sys
sys.setrecursionlimit(10**4)

# 입력
N, L, R = map(int, input().split())
A = [ [] for _ in range(N) ]
for i in range(N):
    A[i] = list( map(int, input().split()) )

# 좌표 관련 선언
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def ok(nx, ny):
    global N
    return 0 <= nx and nx < N and 0 <= ny and ny < N


# DFS를 통해 인구 이동 조건에 따라 그룹을 만들고
# 엔트리가 [그룹 내의 총 인구수, [그룹에 속한 도시의 좌표 튜플]] 인 리스트를 반환
def get_group_list():
    global N, L, R
    global A
    # N x N 크기의 배열에 도시가 속한 그룹의 번호 group_id 를 표시
    # 어떤 그룹에도 속하지 않은 경우: 0
    group = [ [0] * N for _ in range(N) ]
    # 반환될 리스트
    group_list = [ [0, []] ]

    def dfs(x, y, group_id):
        # 현재 도시를 그룹에 포함시키고 반환할 리스트에 정보 저장
        group[x][y] = group_id
        pop = A[x][y]
        group_list[group_id][0] += pop
        group_list[group_id][1].append( (x, y) )
        
        # 현재 도시에 인접한 도시 확인
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if not ok(nx, ny): continue
            if group[nx][ny]: continue
            npop = A[nx][ny]
            diff = abs(pop - npop)
            # 인구 이동 조건
            if L <= diff and diff <= R:
                dfs(nx, ny, group_id)

    # 모든 도시에 대해 탐색
    # 어떤 그룹에도 속하지 않은 경우 DFS로 그룹에 포함시킴
    group_id = 0
    for x in range(N):
        for y in range(N):
            if not group[x][y]:
                group_list.append([0, []])
                group_id += 1
                dfs(x, y, group_id)
    
    return group_list

# get_group_list() 가 반환한 group_list를 토대로 인구 이동을 반영하는 함수
def move_people(group_list):
    global N, L, R
    global A

    # get_group_list() 가 그룹 크기가 1인 그룹만 반환한 경우
    # 인구이동이 일어나지 않으므로 moved = False 를 반환하여 알고리즘을 종료시킴
    moved = False

    for g in group_list:
        total_pop, cities = g
        # 그룹의 크기가 1 인 경우 -> 인구 이동이 없음
        # 그룹의 크기가 0 인 경우 -> group_id 를 위해 더미 값으로서 삽입한 첫번째 항
        if len(cities) <= 1: continue
        else: moved = True

        # 인구 이동 계산 조건
        pop = total_pop // len(cities)
        # 그룹에 속한 도시들에 대하여 인구 이동 업데이트
        for city in cities:
            x, y = city
            A[x][y] = pop

    return moved

# Main
def solution():
    global N, L, R
    global A

    answer = 0
    while True:
        group_list = get_group_list()
        moved = move_people(group_list)
        if not moved: break
        answer += 1
    
    return answer

print( solution() )
