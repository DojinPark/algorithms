# 퇴사
# https://www.acmicpc.net/problem/14501
#
# 점화식
# 1. A[i + T[i] - 1] = max( A[i + T[i] - 1], A[i - 1] + P[i] )
# 2. A[i] = max(A[i - 1], A[i])
# 점화식이 이렇게 특이한 경우도 있다고 알아두기!

N = int( input() )
A = [0] * (N + 1)
T = [0] * (N + 1)
P = [0] * (N + 1)

for i in range(1, N+1):
    t, p = map(int, input().split())
    T[i] = t
    P[i] = p

for d in range(1, N + 1):
    finish_d = d + T[d] - 1
    if finish_d <= N:
        A[finish_d] = max(A[finish_d], A[d-1] + P[d])
    A[d] = max(A[d-1], A[d])

print(A[N])