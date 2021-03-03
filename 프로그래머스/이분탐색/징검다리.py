# https://programmers.co.kr/learn/courses/30/lessons/43236
# 징검다리
# 걸린 시간: 0:29
#
# 출발점 부터 첫번째 바위까지의 거리를 지점이라고 고려하지 않아서 오래 걸림
# 노트: l = m + 1 과 r = m - 1 의 위치가 뒤바뀌진 않았는지 확인하기

INF = int(1e9) + 1

def check(rocks, m, n):
    i, j = 0, 1
    while j < len(rocks):
        if rocks[j] - rocks[i] < m:
            if not n: return False
            j += 1
            n -= 1
        else:
            i = j
            j += 1
    return True

def solution(distance, rocks, n):
    answer = 0

    rocks.append(0)
    rocks.sort()

    l, r = 0, distance
    while l <= r:
        m = (l + r) // 2
        if check(rocks, m, n):
            answer = max(answer, m)
            l = m + 1
        else:
            r = m - 1

    return answer

distance = 25
rocks = 	[2, 14, 11, 21, 17]
n = 2
print( solution(distance, rocks, n) )