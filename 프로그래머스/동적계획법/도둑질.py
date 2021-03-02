# https://programmers.co.kr/learn/courses/30/lessons/42897
# 도둑질
# 걸린 시간 0:38
#
# 노트:
# dp = [ [0] * N for _ in range(2) ] 열이 긴 메모리
# dp = [ [0] * 2 for _ in range(N) ] 열이 짧고 흩어진 메모리
# 속도 차이가 크다! 효율성 테스트 통과를 못하는 겨우 열이 긴 메모리로 변경해보자


def solution(money):
    answer = 0
    N = len(money)

    # dp = [ [0] * 2 for _ in range(N) ]

    # for i in range(0, N):
    #     dp[i][True] = dp[i - 1][False] + money[i]
    #     dp[i][False] = max(dp[i - 1][True], dp[i - 1][False])
    
    # answer = max(answer, dp[N - 1][False])

    # dp[0][True] = 0
    # for i in range(1, N):
    #     dp[i][True] = dp[i - 1][False] + money[i]
    #     dp[i][False] = max(dp[i - 1][True], dp[i - 1][False])
    
    # answer = max(answer, dp[N - 1][True])

    dp = [ [0] * N for _ in range(2) ]

    for i in range(0, N):
        dp[True][i] = dp[False][i - 1] + money[i]
        dp[False][i] = max(dp[False][i - 1], dp[True][i - 1])
    
    answer = dp[False][N - 1]

    dp[True][0] = 0
    for i in range(1, N):
        dp[True][i] = dp[False][i - 1] + money[i]
        dp[False][i] = max(dp[False][i - 1], dp[True][i - 1])

    answer = max(answer, dp[True][N - 1])

    return answer

money = [1, 2, 3, 1]
print( solution(money) ) # 4