# https://programmers.co.kr/learn/courses/30/lessons/43105
# 정수 삼각형
# 걸린 시간: 0:08

def solution(triangle):
    answer = 0
    H = len(triangle)

    dp = [ [0] * h for h in range(1, H + 1) ]
    dp[0][0] = triangle[0][0]

    for h in range(H - 1):
        for i in range(h + 1):
            if dp[h + 1][i] < dp[h][i] + triangle[h + 1][i]:
                dp[h + 1][i] = dp[h][i] + triangle[h + 1][i]
            if dp[h + 1][i + 1] < dp[h][i] + triangle[h + 1][i + 1]:
                dp[h + 1][i + 1] = dp[h][i] + triangle[h + 1][i + 1]

    answer = max(dp[H - 1])

    return answer

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print( solution(triangle) )