# https://programmers.co.kr/learn/courses/30/lessons/42891
# 무지의 먹방 라이브
# 레벨 4
# 정확성 테스트 통과 걸린 시간: 0:37
# 호율성 테스트 통과 걸린 시간: 1:15

def solution(food_times, k):
    # print()
    answer = 0

    N = len(food_times)
    food_times = [ [time, idx + 1] for idx, time in enumerate(food_times) ]
    food_times.sort()

    k_used = 0
    time, x, time_each = food_times[0][0], 0, 0
    # print(food_times)
    while x < N:
        time = food_times[x][0]
        k_use = (time - time_each) * (N - x)
        time_each += (time - time_each)

        if k_used + k_use > k:
            break
        else:
            k_used += k_use

        while x < N and time == food_times[x][0]:
            x += 1
        # print(x, time_each, k_used)
    
    if x == N and k >= k_used:
        return -1
    
    food_times = sorted(food_times[x:], key = lambda e: e[1])
    # print(food_times)
    # print('answer', x, k, k_used)
    answer = food_times[ (k - k_used) % len(food_times) ][1]

    return answer

food_times = [3, 1, 2]
k = 5
print( solution(food_times, k) ) # 1

food_times =	[4, 5]
k = 9
print( solution(food_times, k) ) # -1

food_times = 	[1, 0, 4, 5]
k = 3
print( solution(food_times, k) ) # 3

food_times =	[1, 1, 1]
k = 4
print( solution(food_times, k) ) # -1


# 시간 초과된 풀이
def solution(food_times, k):
    N = len(food_times)
    food_times = [ [time, idx] for idx, time in enumerate(food_times) ]
    food_times.sort()
    while food_times and food_times[0][0] == 0:
        del food_times[0]

    k_subtracted_each = 0

    # print(food_times, k, k_subtracted_each)
    while k >= len(food_times):
        k_subtract = (food_times[0][0] - k_subtracted_each) * len(food_times)
        k_subtracted_each += food_times[0][0] - k_subtracted_each

        if k < k_subtract:
            k = k % len(food_times)
        else:
            k -= k_subtract
            while food_times and food_times[0][0] == k_subtracted_each:
                del food_times[0]
            if not food_times:
                # print(food_times,  k, k_subtracted_each, 'not food_tiems')
                return -1
        # print(food_times, k, k_subtracted_each)


    food_times.sort(key = lambda x: x[1])
    answer = food_times[k][1] + 1

    return answer