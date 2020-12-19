# 금광

def solution(N, M, a):
    d = [ [0] * M for _ in range(N) ]

    for r in range(N):
        for c in range(M):
            d[r][c] = a[r*M + c]
    
    print('initial map')
    for r in range(N):
        for c in range(M):
            print( d[r][c], end=' ')
        print()

    answer = 0
    for c in range(1, M):
        for r in range(N):
            mx = 0
            if r >= 1:
                mx = max(mx, d[r-1][c-1])
            if r <= N - 2:
                mx = max(mx, d[r+1][c-1])
            mx = max(mx, d[r][c-1])
            d[r][c] += mx
            answer = max(answer, d[r][c])
    
    print('memoized')
    for r in range(N):
        for c in range(M):
            print( d[r][c], end=' ')
        print()

    return answer

N, M = 3, 4
a = [1, 3, 3, 2, 2, 1, 4, 1, 0, 6, 4, 7]
print( 'answer:', solution(N, M, a), end='\n\n' )
# 19

N, M = 4, 4
a = [1, 3, 1, 5, 2, 2, 4, 1, 5, 0, 2, 3, 0, 6, 1, 2]
print( 'answer:', solution(N, M, a) )
# 16