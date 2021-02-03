# https://programmers.co.kr/learn/courses/30/lessons/42860
# 조이스틱
# 그리디 알고리즘

from itertools import permutations

INF = int(1e9)
NUM_ALPHAS = ord('Z') - ord('A') + 1 # 26

def alpha_dist(c1, c2):
    c1 = ord(c1)
    c2 = ord(c2)
    l = min(c1, c2)
    r = max(c1, c2)
    return min(r - l, l - r + NUM_ALPHAS)

def cursor_dist(n, p1, p2):
    if p1 == 0:
        p1 += 1
    if p2 == 0:
        return INF
    l = min(p1, p2)
    r = max(p1, p2)
    return min(r - l, l - r + n)

def solution(name):
    answer = INF

    n = len(name)
    N = n + 1
    name = 'A' + name # 초기상태를 표현하기위해 더미값으로 name의 길이를 1만큼 늘림
    
    dist = [ [INF] * N for _ in range(N) ]
    for i in range(N):
        for j in range(N):
            d = alpha_dist('A', name[j]) + cursor_dist(n, i, j)
            dist[i][j] = d
    # for line in dist:
    #     print(line)

    diff = [i for i in range(1, N) if name[i] != 'A']
    paths = permutations(diff, len(diff))
    for path in paths:
        now = 0
        cost = 0
        for to in path:
            cost += dist[now][to]
            now = to
        # print(path, ':', cost)
        answer = min(answer, cost)

    return answer

print(solution('JAZ')) # 11
print(solution('JEROEN')) # 56
print(solution('JAN')) # 23