# 기둥과 보 설치
# https://programmers.co.kr/learn/courses/30/lessons/60061

GI = 0
BO = 1

REMOVE = 0
INSTALL = 1

def solution(n, build_frame):
    answer = []

    gi = [ [0] * (n + 1) for _ in range(n + 1) ]
    bo = [ [0] * (n + 1) for _ in range(n + 1) ]

    def gibo_ok(x, y, a):
        ok = False

        if a == GI:
            if y == 0: ok = True
            elif bo[x][y]: ok = True
            elif x-1 <= n and bo[x-1][y]: ok = True
            elif y-1 >= 0 and gi[x][y-1]: ok = True
            
        elif a == BO:
            if y-1 >= 0 and gi[x][y-1]: ok = True
            elif x+1 <= n and y-1 >= 0 and gi[x+1][y-1]: ok = True
            elif x-1 >= 0 and x+1 <= n and bo[x-1][y] and bo[x+1][y]: ok = True

        return ok

    def ok():   # 이 함수를 기둥이나 보가 있는 위치에 대해서만 동작하도록 DFS 코드를 짜려고 시도했으나 너무 복잡해서 포기함. 시뮬레이션/구현 문제는 절대 효율성을 따져서는 안되고, 빠르고 간단하게 코드를 구현하는 것을 목표로 해야한다.
        for x in range(n+1):
            for y in range(n+1):
                if gi[x][y]:
                    ok = gibo_ok(x, y, GI)
                    if not ok: return False
                if bo[x][y]:
                    ok = gibo_ok(x, y, BO)
                    if not ok: return False
        return True

    for build in build_frame:
        x, y, a, b = build
        
        if a == GI:
            gi[x][y] = b
            if not ok():
                if b == INSTALL:
                    gi[x][y] = 0
                if b == REMOVE:
                    gi[x][y] = 1
        if a == BO:
            bo[x][y] = b
            if not ok():
                if b == INSTALL:
                    bo[x][y] = 0
                if b == REMOVE:
                    bo[x][y] = 1

    for x in range(n+1):
        for y in range(n+1):
            if gi[x][y]:
                answer.append( [x,y,GI] )
            if bo[x][y]:
                answer.append( [x,y,BO] )
    
    answer.sort(key = lambda x: x[2])
    answer.sort(key = lambda x: x[1])
    answer.sort()

    return answer

n = 5
build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
print( solution(n, build_frame) )
# [[1,0,0],[1,1,1],[2,1,0],[2,2,1],[3,2,1],[4,2,1],[5,0,0],[5,1,0]]

n = 5
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
print( solution(n, build_frame) )
# [[0,0,0],[0,1,1],[1,1,1],[2,1,1],[3,1,1],[4,0,0]]