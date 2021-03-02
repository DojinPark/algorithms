# https://programmers.co.kr/learn/courses/30/lessons/42898
# 등굣길
# 걸린 시간: 0:19

DIV = 1000000007

def solution(m, n, puddles):
    answer = 0

    is_puddle = [ [0] * n for _ in range(m) ]
    dp = [ [0] * n for _ in range(m) ]
    dp[0][0] = 1

    for x, y in puddles:
        is_puddle[x - 1][y - 1] = 1

    for x in range(m):
        for y in range(n):
            if x - 1 >= 0 and not is_puddle[x - 1][y]:
                dp[x][y] += dp[x - 1][y]
                if dp[x][y] > DIV:
                    dp[x][y] %= DIV
            if y - 1 >= 0 and not is_puddle[x][y - 1]:
                dp[x][y] += dp[x][y - 1]
                if dp[x][y] > DIV:
                    dp[x][y] %= DIV

    for y in range(n):
        for x in range(m):
            print(dp[x][y], end=' ')
        print()
    
    answer = dp[m - 1][n - 1]

    return answer

m = 4
n = 3
puddles = [ [2,2] ]
print( solution(m, n, puddles) ) # 4