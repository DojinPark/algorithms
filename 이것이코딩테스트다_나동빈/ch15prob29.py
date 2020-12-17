# 공유기 설치
# https://www.acmicpc.net/problem/2110

INF = int(1e9)

import sys
N, C = map(int, sys.stdin.readline().rstrip().split())
a = [0] * N
for i in range(N):
    a[i] = ( int( sys.stdin.readline().rstrip() ) )

a.sort()

M = N - C
b = [ a[i+1] - a[i] for i in range(N - 1) ]
for _ in range(M):
    min_pos = b.index( min(b) )
    l, r = INF, INF
    if min_pos - 1 >= 0:
        l = b[min_pos - 1]
    if min_pos + 1 < len(b):
        r = b[min_pos + 1]

    if l < r:
        b[min_pos] += b[min_pos - 1]
        del b[min_pos - 1]  ##
    else:
        b[min_pos] += b[min_pos + 1]
        del b[min_pos + 1]

print( min(b) )
