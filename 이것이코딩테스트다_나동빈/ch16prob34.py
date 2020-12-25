# 병사 배치하기
# https://www.acmicpc.net/problem/18353

import sys
N = int( input() )
A = list( map(int, sys.stdin.readline().rstrip().split()) )
d = [0] * N

d[0] = 1
for i in range(1, N):
    cont = False
    for j in range(i-1, -1, -1):
        if A[j] > A[i]:
            # d[i] = d[j] + 1
            d[i] = max(d[i], d[j] + 1)
            cont = True
            # break
    if not cont:
        d[i] = 1
    
# print(d)
answer = N - max(d)
print(answer)