# https://programmers.co.kr/learn/courses/30/lessons/64062
# 5. 징검다리 건너기
# 정확성테스트 걸린 시간: 0:45
# 효율성테스트 걸린 시간: 1:10

MAX = 200000000

def ok(d, k, N, m):
    excluded = [False] * N

    for stone, indices in d:
        if stone > m: break
        for idx in indices:
            excluded[idx] = True

    cnt = 0
    for ex in excluded:
        if ex:
            cnt += 1
            if cnt == k:
                return False
        else:
            cnt = 0
    return True

def solution(stones, k):
    answer = 0
    N = len(stones)
    d = {}

    for i, stone in enumerate(stones):
        if stone not in d.keys():
            d[stone] = []
        d[stone].append(i)
    
    d = sorted(d.items())

    l, r = 0, MAX
    while l <= r:
        m = (l + r) // 2

        if ok(d, k, N, m):
            if answer < m:
                answer = m
            l = m + 1
        else:
            r = m - 1

    return answer + 1

stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3
print( solution(stones, k) )