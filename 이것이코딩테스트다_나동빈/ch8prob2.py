# 1로 만들기
#
# Bottom-Up | DP 테이블
# Top-Down | 메모아이제이션
#
# setrecursionlimit() 재귀 호출 횟수 제한 해제

INF = 30001
X = 26
# 3

m = [INF] * (X+1)
def topdown(num, step = 0):
    global m

    if num % 5 == 0 and m[num // 5] > step :
        m[num // 5] = step + 1
        topdown(num // 5, step + 1)
    if num % 3 == 0 and m[num // 3] > step:
        m[num // 3] = step + 1
        topdown(num // 3, step + 1)
    if num % 2 == 0 and m[num // 2] > step:
        m[num // 2] = step + 1
        topdown(num // 2, step + 1)
    if num > 1 and m[num - 1] > step:
        m[num - 1] = step + 1
        topdown(num - 1, step + 1)

    return m[1]

print(topdown(X))
print(m)

dp = [INF] * (X+1)
def bottomup(x, num = 1, step = 0):
    global dp
    dp[num] = step
    
    if num * 5 <= x and dp[num * 5] > step:
        bottomup(x, num * 5, step + 1)
    if num * 3 <= x and dp[num * 3] > step:
        bottomup(x, num * 3, step + 1)
    if num * 2 <= x and dp[num * 2] > step:
        bottomup(x, num * 2, step + 1)
    if num + 1 <= x and dp[num + 1] > step:
        bottomup(x, num + 1, step + 1)
    
    return dp[x]

print(bottomup(X))
print(dp)

dp = [0] * (X+1)
def bottomup2(x):
    global dp
    dp[1] = 0
    
    for i in range(2, x+1):
        minstep = INF
        if minstep > dp[i-1] + 1:
            minstep = dp[i-1] + 1
        if i % 2 == 0 and minstep > dp[i // 2] + 1:
            minstep = dp[i // 2] + 1
        if i % 3 == 0 and minstep > dp[i // 3] + 1:
            minstep = dp[i // 3] + 1
        if i % 5 == 0 and minstep > dp[i // 5] + 1:
            minstep = dp[i // 5] + 1
        dp[i] = minstep
    
    return dp[x]

print(bottomup2(X))
print(dp)