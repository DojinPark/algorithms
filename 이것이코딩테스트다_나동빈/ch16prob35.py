# 못생긴 수

## 틀린 풀이 ##

# TIMES = 30 # 30 = 2 * 3 * 5

# def mark_A(digits, A, a):
#     if a >= len(A): return
#     if A[a]: return

#     A[a] = True

#     for digit in digits:
#         mark_A(digits, A, a * digit)

# def find_pattern():
#     A = [False] * (TIMES + 1)
#     digits = [2, 3, 5]

#     mark_A(digits, A, 1)

#     pattern = [i for i, a in enumerate(A) if A[i] == True]
#     period = len(pattern)
    
#     return pattern, period

# def solution(n):
#     ret = 0

#     pattern, period = find_pattern()

#     q = n // period
#     i = n % period - 1

#     ret = pattern[i]
#     for _ in range(q):
#         ret *= TIMES

#     return ret

# n = 10
# print( solution(n) )
# # 12

# n = 4
# print( solution(n) )
# # 4