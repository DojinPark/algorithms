# https://programmers.co.kr/learn/courses/30/lessons/42891#
# 무지의 먹방 라이브(복습)
# 걸린 시간: 0:50

# 노트: 마지막 k % L 인덱스 계산하는게 복잡해서 시간 오래걸림
#       -> 리스트 슬라이싱을 이용해 더 직관적인 코드를 짜서 해결!!!
#       -> 버그 줄이는 법: 내 스스로 이해 하기도 쉬운 코드를 짜기!

def solution(food_times, k):
    answer = -1

    food_times = [ (time, idx + 1) for idx, time in enumerate(food_times) ]
    food_times.sort()

    L = len(food_times)
    i = 0 # index for minimum food time
    m = food_times[i][0] # minimum food time
    p = 0 # previous minimum food time
    while i < len(food_times) and k >= (m - p) * L:
        k -= (m - p) * L
        p = m
        if i + 1 < len(food_times):
            m = food_times[i + 1][0]
        i += 1
        L -= 1

    if i != len(food_times):
        food_times = sorted(food_times[i:], key=lambda x: x[1])
        answer = food_times[k % L][1]

    return answer

food_times = [2, 4, 6, 6, 8]
k = 18
print( solution(food_times, k) ) # 3

food_times = [2, 4, 6, 6, 8]
k = 19
print( solution(food_times, k) ) # 4

food_times = [2, 4, 6, 6, 8]
k = 20
print( solution(food_times, k) ) # 5

food_times = [2, 4, 6, 6, 8]
k = 21
print( solution(food_times, k) ) # 3