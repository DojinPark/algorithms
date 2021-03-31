# https://programmers.co.kr/learn/courses/30/lessons/12902
# 3 x n 타일링 (Level 4)
# 걸린 시간: 0:30
#
# 질문 본 부분: 주석 참고

DIV = int(1e9) + 7

def solution(n):
    answer = 0
    dp = [0] * (n + 1)

    dp[2] = 3
    dp[4] = 11

    for i in range(6, n + 1, 2):
        for j in range(2, i - 3, 2):
            added = dp[i] + 2*dp[j]
            if added >= DIV:
                added -= DIV
            dp[i] = added

        # 이전 dp값과 상관없이 i자리가 가질 수 있는 고유의 경우의 수가 상수값으로 더해지는 경우. DP 문제 풀 때 이 부분을 빼먹어서 문제를 틀리는 경우가 많음.
        added = dp[i] + 3*dp[i - 2] + 2
        if added >= DIV:
            added -= DIV
        dp[i] = added
        
    
    answer = dp[n] % DIV

    # print(dp)

    return answer

print( solution(10) )