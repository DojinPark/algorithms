# https://programmers.co.kr/learn/courses/30/lessons/43238
# 입국심사
# 걸린 시간: 0:22

INF = int(1e15) + 1

def get_output(T, times):
    output = 0
    for time in times:
        output += T // time
    return output

def solution(n, times):
    answer = INF

    l, r = 0, INF
    while l <= r:
        m = (l + r) // 2
        output = get_output(m, times)
        if output >= n:
            answer = min(answer, m)
            r = m - 1
        else:
            l = m + 1

    return answer

print( solution(6, [7, 10]) )