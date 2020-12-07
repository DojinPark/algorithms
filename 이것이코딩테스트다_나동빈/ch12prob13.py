# 치킨 배달
# https://www.acmicpc.net/problem/15686

INF = int(1e9)

from itertools import combinations

def solution(N, M, globe):
    A = []  # 집들 좌표
    B = []  # 치킨집들 좌표
    
    for r in range(len(globe)):
        for c in range(len(globe[0])):
            if globe[r][c] == 1:
                A.append( (r, c) )
            elif globe[r][c] == 2:
                B.append( (r, c) )
    
    combs = combinations(B, M)

    def score(C):
        total_score = 0
        for a in A: # 모든 집들에 대하여
            min_score = INF # 최소 치킨 거리를 구하기 위해
            for c in C: # 모든 집들 확인
                score = abs(a[0] - c[0]) + abs(a[1] - c[1])
                min_score = min(min_score, score)
            total_score += min_score
        return total_score
    
    answer = INF
    for C in combs:
        s = score(C)
        answer = min(answer, s)
    
    return answer                 
    
import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
globe = []
for _ in range(N):
    globe.append( list(map(int, sys.stdin.readline().rstrip().split())) )

print(solution(N, M, globe))
