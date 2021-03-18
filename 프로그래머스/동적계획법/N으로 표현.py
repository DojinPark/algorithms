# https://programmers.co.kr/learn/courses/30/lessons/42895
# N으로 표현
# 걸린 시간: 0:50

MAX_NUM = 32000
MAX_STEPS = 8

def solution(N, number):
    answer = 0
    
    dp = [MAX_STEPS + 1] * (MAX_NUM + 1)
    
    def search(x = 0, repeat = 1, steps = 0):
        if steps > MAX_STEPS: return
        # if x < 0: return

        # Early stop
        if x <= MAX_NUM and x >= 0 and dp[x] < steps and repeat == 1:
            return
        
        if x <= MAX_NUM and x >= 0 and dp[x] > steps:
            dp[x] = steps

        repeated = int(str(N) * repeat)
        
        search(x + repeated, 1, steps + 1)
        search(x - repeated, 1, steps + 1)
        search(x * repeated, 1, steps + 1)
        search(x // repeated, 1, steps + 1)
        search(x, repeat + 1, steps + 1)

    search()
    if dp[number] > MAX_STEPS: answer = -1
    else: answer = dp[number]

    return answer

# print( solution(5, 12) ) # 4
# print( solution(2, 11) ) # 3

# NUM_MAX = 32000
# INF_STEPS = 9

# from heapq import heappush as push, heappop as pop

# def solution(N, number):

#     d = [INF_STEPS] * (NUM_MAX + 1)
#     h = []
#     repeated = [0]
#     for repeat in range(1, 9):
#         NN = int( str(N) * repeat )
#         if NN <= NUM_MAX:
#             repeated.append(NN)

#     for repeat in range(1, len(repeated)):
#         NN = repeated[repeat]
#         d[NN] = repeat
#         push(h, (repeat, NN))

#     while h:
#         steps, n = pop(h)
#         for repeat in range(1, min(len(repeated), INF_STEPS - steps)):
#             NN = repeated[repeat]
#             new_steps = steps + repeat

#             new_n = n - NN
#             if new_n >= 1 and d[new_n] > new_steps:
#                 d[new_n] = new_steps
#                 if new_steps < INF_STEPS - 1:
#                     push(h, (new_steps, new_n) )

#             new_n = n + NN
#             if new_n <= NUM_MAX and d[new_n] > new_steps:
#                 d[new_n] = new_steps
#                 if new_steps < INF_STEPS - 1:
#                     push(h, (new_steps, new_n) )

#             new_n = n * NN
#             if new_n <= NUM_MAX and d[new_n] > new_steps:
#                 d[new_n] = new_steps
#                 if new_steps < INF_STEPS - 1:
#                     push(h, (new_steps, new_n) )

#             new_n = n // NN
#             if new_n >= 2 and d[new_n] > new_steps:
#                 d[new_n] = new_steps
#                 if new_steps < INF_STEPS - 1:
#                     push(h, (new_steps, new_n) )

#     if d[number] < INF_STEPS: return d[number]
#     else: return -1

# print( solution(5, 12) ) # 4
# print( solution(2, 11) ) # 3