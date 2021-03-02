# https://www.acmicpc.net/problem/2110

import sys

INF = int(1e10)

def bin_search(X, C):
    a, b = 1, X[-1] - X[0]
    ret = -1

    while a <= b:
        m = (a + b) // 2

        cnt = 1
        min_d = INF
        i, j = 0, 1
        while j < len(X):
            d = X[j] - X[i]
            if d >= m:
                cnt += 1
                i = j
                if min_d > d: min_d = d
            j += 1
        
        if cnt >= C:
            a = m + 1
            if ret < min_d: ret = min_d
        else:
            b = m - 1
    
    return ret

N, C = map(int, input().split())
X = []
for _ in range(N):
    X.append( int(sys.stdin.readline().rstrip()) )

X.sort()

print( bin_search(X, C) )