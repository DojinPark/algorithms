# 탑승구
# https://www.acmicpc.net/problem/10775  (공항)

LIMIT = 100003
import sys
sys.setrecursionlimit(LIMIT)

G = int( input() )
P = int( input() )
a = []
for _ in range(P):
    a.append( int(sys.stdin.readline().rstrip()) )


def find_root(root, x):
    if root[x] != x:
        root[x] = find_root(root, root[x])
    return root[x]

def union(root, x, y):
    rx = find_root(root, x)
    ry = find_root(root, y)
    if rx < ry:
        root[ry] = rx
    else:
        root[rx] = ry

root = [ i for i in range(G+1) ]  # root는 g 번째 이하의 게이트 중 다음으로 비행기를 도킹시 킬 게이트 번호를 의미한다.
answer = 0
for g in a:
    if find_root(root, g) == 0:    # 다음으로 도킹시킬 게이트번호가 1 이하인 경우 자리가 없는 것이므로 루프를 종료하고 여태 도킹한 비행기 수를 출력
        break
    union(root, root[g] - 1, g)
    answer += 1

print(answer)