# 개미 전사

N = 4
K = [1, 3, 1, 5]
# 8

# 내 풀이
# - 2차원 행렬은 불필요한 것이었음.
#   2차원 행렬이 반드시 필요한 문제 추후에 노트 하기
m = [ [0] * 2 for _ in range(len(K)) ]
def bottomup():
    m[0][0] = 0
    m[0][1] = K[0]
    for i in range(1, len(K)):
        m[i][0] = max(m[i - 1][1], m[i - 1][0])
        m[i][1] = max(m[i - 1][1], m[i - 1][0] + K[i])
    
    k = len(K) - 1
    return max(m[k][0], m[k][1])

print(bottomup())
print(m)

# 책 풀이
# 점화식: m[i] = max( m[i-1], m[i-2] + K[i] )
m = [0] * len(K)
def bottomup2():
    m[0] = K[0]
    m[1] = max(m[0], K[1])
    for i in range(2, len(K)):
        m[i] = max( m[i-1], m[i-2] + K[i] )
    return m[len(K) - 1]

print(bottomup2())
print(m)