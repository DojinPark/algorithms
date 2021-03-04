# https://programmers.co.kr/learn/courses/30/lessons/67259
# 4. 경주로 건설
# 걸린 시간: 1:21
#
# 노트: 직선도로와 코너 비용에 대한 규칙을 내 맘대로 생각하고 잘못 풀어서
#      시간이 훨씬 많이 듦. 문제를 다시 읽고서야 풀었음
#      카카오 기출은 문제 상황 설정에 디테일이 많다.
#      백준, 프로그래머스 등에 등장하는 문제들과 얼추 비슷해 보이지만
#      가중치 규칙이 다른 경우가 많아서 연습문제 풀던 습관대로 풀면
#      엄청난 시간을 날릴 수도 있다.
#      주어진 설정을 차근차근히 다 일고 이해한 후 풀기

from heapq import heappush as push, heappop as pop

INF = int(1e9)
N = 0
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def ok(x, y):
    return x >= 0 and x < N and y >= 0 and y < N

def solution(board):
    global N
    answer = 0
    N = len(board)

    cost = [ [ [INF] * N for _ in range(N) ] for __ in range(4) ]
    h = []

    push(h, (0, 2, 0, 0) ) # cost, direction, x, y, altered
    push(h, (0, 0, 0, 0) ) # cost, direction, x, y, altered
    cost[2][0][0] = 0
    cost[0][0][0] = 0
        
    while h:
        c, d, x, y = pop(h)

        if cost[d][x][y] < c:
            continue
        
        for i in range(4):

            if i == d:
                nx = x + dx[i]
                ny = y + dy[i]
                if not ok(nx, ny): continue
                nc = c + 100
            else:
                nx = x
                ny = y
                nc = c + 500
            if not board[nx][ny] and cost[i][nx][ny] > nc:
                cost[i][nx][ny] = nc
                push(h, (nc, i, nx, ny))

    answer = min( [ cost[0][N-1][N-1], cost[1][N-1][N-1], cost[2][N-1][N-1], cost[3][N-1][N-1] ] )

    return answer

# board = [[0,0,0],[0,0,0],[0,0,0]]
# print( solution(board) )
# # 900

# board = [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]
# print( solution(board) )
# # 3800

# board = [[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]
# print( solution(board) )
# # 2100

# board = [[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]
# print( solution(board) )
# # 3200