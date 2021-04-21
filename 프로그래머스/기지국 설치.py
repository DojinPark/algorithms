# https://programmers.co.kr/learn/courses/30/lessons/12979
# 기지국 설치 (Level 3)
# 걸린 시간: 0:45
#
# 노트: 풀이 시간이 너무 오래 걸렸음.
#       iteration 구현 문제 풀이력은 아직 컨디션에 많이 좌우돼서
#       더 많이 풀어보며 심플하게 구현하는 법을 익힐 수 밖에 없음.

def solution(n, stations, w):
    answer = 0
    cover_len = []

    stations.append( - w )
    stations.append( n + w + 1 )
    stations.sort()

    L = 2*w + 1
    for i in range(len(stations) - 1):
        a = stations[i]
        b = stations[i + 1]
        if b - a > L:
            left = a + w + 1
            right = b - w - 1
            cover_len.append(right - left + 1)

    for length in cover_len:
        n = length // L
        if length > L * n: n += 1
        answer += n

    return answer

print( solution(11, [4, 11], 1) )
print( solution(16, [9], 2) )