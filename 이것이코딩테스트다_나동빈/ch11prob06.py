# 무지의 먹방 라이브
#
# https://programmers.co.kr/learn/courses/30/lessons/42891

# 시간 초과 뜸
# min_t 를 구하는 과정을 heapq 로 구현해보자
# C++ 로 옮겨도 안되는 코드임
from collections import deque

def solution(food_times, k):
    q = deque()
    for i, t in enumerate(food_times):
        q.append( (t, i+1) )

    while q:
        L = len(q)
        min_t = min(q)[0]
        
        if k >= L * min_t:
            sub = min_t
        else:
            sub = 1
            
        for i in range(len(q)):
            now_t, now_i = q.popleft()
            
            if k == 0:
                return now_i
                
            now_t -= sub
            k -= sub
            if now_t:
                q.append( (now_t, now_i) )

    return -1

food_times = [3, 1, 2]
k = 5
# 1
print( solution(food_times, k) )


# heapq를 이용한 풀이
from heapq import heappush as push
from heapq import heappop as pop

def solution(food_times, k):
    q = []
    total_t = 0
    for i, t in enumerate(food_times):
        push(q, (t, i+1))
        total_t += t
    if total_t <= k: return -1

    sub = 0
    while q:
        L = len(q)
        min_t, min_num = pop(q)

        if k >= L * min_t:
            k -= L * min_t
            sub += min_t
        else:
            push(q, (min_t, min_num))
            foods = [t for t in q]
            foods.sort(key=lambda x: x[1])

            for i in range(len(foods)):
                t, num = foods[i]
                t -= sub
                foods[i] = (t, num)

            while True:
                for i in range(len(foods)):
                    t, num = foods[i]
                    if t == 0:
                        continue
                    if k == 0:
                        return num
                    t -= 1
                    k -= 1
                    foods[i] = (t, num)
    
    return -1
                
food_times = [3, 1, 2]

k = 5
# 1
print( solution(food_times, k) )



# 이 책으로 공부하기 전의 내 풀이
from heapq import heappush, heappop

def solution(food_times, k):
    answer = -1

    q = []
    for i in range(len(food_times)):
        heappush(q, (food_times[i], i+1))

    prev_min_time = 0
    while len(q):
        foods_left = len(q)
        min_foods = []
        min_foods.append(heappop(q))
        while len(q):
            next_food = heappop(q)
            if min_foods[0][0] == next_food[0]:
                min_foods.append(next_food)
            else:
                heappush(q, next_food)
                break

        sub = foods_left * (min_foods[0][0] - prev_min_time)

        if k >= sub:
            k -= sub
        else:
            rest_foods = sorted( [a[1] for a in min_foods + q] )
            k %= foods_left
            answer = rest_foods[k]
            break

        prev_min_time = min_foods[0][0]

    return answer