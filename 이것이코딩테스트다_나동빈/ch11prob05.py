# 볼링공 고르기
#
# 책 풀이는 좀 다른데,
# 고등학교 순열 조합 개념으로 풀수 있는거면 그냥 그렇게 풀자!
# 다른 알고리즘을 체화하는데 시간을 더 투자하는게 좋을거같다.

def solve(N, M, K):
    W = [0] * (M + 1)
    for k in K:
        W[k] += 1
    
    answer = N * (N-1) // 2
    for w in W:
        if w > 1:
            answer -= w * (w-1) // 2
    
    return answer

N, M = 5, 3
K = [1, 3, 2, 3, 2]
# 8
print(solve(N, M, K))

N, M = 8, 5
K = [1, 5, 4, 3, 2, 4, 5, 2]
# 25
print(solve(N, M, K))