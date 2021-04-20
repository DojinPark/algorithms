# https://programmers.co.kr/learn/courses/30/lessons/12938
# 최고의 집합 (Level 3)
# 프로그래머스에서 풀어본 문제 중 가장 쓸모 없는 듯!
#
# 걸린 시간: 0:08


def solution(n, s):
    answer = []

    base = s // n
    rem = s % n

    if base == 0: return [-1]

    for _ in range(n - rem):
        answer.append(base)
    for _ in range(rem):
        answer.append(base + 1)

    return answer