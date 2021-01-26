# 편집 거리
# 책 문제와는 다른
# https://www.acmicpc.net/problem/7620
# 으로 대체

INF = int(1e9)
CPY = 0
ADD = 1
DEL = 2
MOD = 3

from collections import deque

str1 = input()
str2 = input()

len1 = len(str1)
len2 = len(str2)

str1 = ' ' + str1
str2 = ' ' + str2

q = deque()
dp = [ [ [INF] * 4 for _ in range(len1 + 1) ] for __ in range(2) ]
sel = True

dp[sel][0][CPY] = 0
dp[sel][0][ADD] = 0
dp[sel][0][DEL] = 0
for i in range(len1 + 1):
    dp[sel][0][MOD] = i

for i2 in range(1, len2 + 1):
    sel = not sel
    dp[sel][0][ADD] = i2
    for i1 in range(1, len1 + 1):

        if str1[i1] == str2[i2]:
            min_cost = min( dp[not sel][i1 - 1] )
            if min_cost != INF:
                dp[sel][i1][CPY] = min_cost

        min_cost = min(dp[not sel][i1])
        if min_cost != INF:
            dp[sel][i1][ADD] = min_cost + 1

        min_cost = min(dp[sel][i1 - 1])
        if min_cost != INF:
            dp[sel][i1][DEL] = min_cost + 1

        min_cost = min(dp[not sel][i1 - 1])
        if min_cost != INF:
            dp[sel][i1][MOD] = min_cost + 1
        
print('min_cost:', min(dp[sel][len1])

# trace minimum cost script
def find_script_op(script_ops, dp, i):
    dp


script_ops = []