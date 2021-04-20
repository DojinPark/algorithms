# https://programmers.co.kr/learn/courses/30/lessons/12907
# 거스름돈 (Level 3)
# 풀이 시간 초과
#
# 노트: 점화식이 덧셈 한번 정도로 단순한 경우,
#       iteration 횟수가 10,000,000(천만)에 달해도 O(N)이므로
#       Memoized DP로 풀어도 1초 이내 실행시킬 수 있다.
# 노트: 재귀 그리디 서치 vs Memoized DP 알고리즘의 실행 시간을
#       탐색 규모를 가로축으로 차트를 그려보면 x자로 교차하는 경우

MOD = int(1e10) + 7

def solution(n, money):
    answer = 0
    d = [0] * (n + 1)

    money.sort()

    # d[money[0]] = 1
    d[0] = 1

    for m in money:
        for i in range(n + 1):
            if i - m >= 0:
                d[i] += d[i - m]
        
    answer = d[n]

    return answer

print( solution(5, [1,2,5]) ) # 4
print( solution(10, [1,2,5]) ) # 10

##### 시간 초과 풀이 2 #####
# knapsack problem을 응용한 top-down dp 알고리즘

# MOD = int(1e10) + 7

# def dfs(n, money):
#     dp = [ [0] * (n + 1) for _ in range( len(money) ) ]

#     def __dfs(i=len(money) - 1, s=n):
        
#         if s < 0: return 0
#         elif s == 0: return 1
#         elif dp[i][s]: return dp[i][s]

#         total = 0
#         for j in range(i + 1):
#             m = money[j]
#             total += __dfs(j, s - m)

#         dp[i][s] = total
        
#         return total

#     ret = __dfs()
#     print(dp)
#     return ret

# def solution(n, money):
#     answer = 0

#     money.sort()

#     answer = dfs(n, money) % MOD

#     return answer

# print( solution(5, [1,2,5]) )


##### 시간 초과 풀이 #####
# 0원 부터 시작하여 모든 경우의 수를 시도해보는 그리디 알고리즘

# MOD = int(1e10) + 7

# def dfs(n, money, s=0, i=0):    
#     if s == n: return 1
#     elif s > n: return 0

#     total = 0
#     for j in range(i, len(money)):
#         total += dfs(n, money, s + money[j], j)
    
#     if total >= MOD: total -= MOD
#     return total

# def solution(n, money):
#     answer = 0

#     money.sort()

#     answer = dfs(n, money)

#     return answer

# print( solution(5, [1,2,5]) )