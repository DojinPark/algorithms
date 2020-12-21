# 정수 삼각형
# https://www.acmicpc.net/problem/1932

N = int( input() )
a = []
for _ in range(N):
    a.append( list( map(int, input().split())) )

for i in range(1, N):
    for j in range(i + 1):
        mx = 0
        if j >= 1:
            mx = max(mx, a[i-1][j-1])
        if j <= i - 1:
            mx = max(mx, a[i-1][j])
        a[i][j] += mx

print( max(a[N-1]) )

# 5
# 7
# 3 8
# 8 1 0
# 2 7 4 4
# 4 5 2 6 5