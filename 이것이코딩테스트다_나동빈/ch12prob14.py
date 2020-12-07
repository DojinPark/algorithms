# 외벽 점검
# https://programmers.co.kr/learn/courses/30/lessons/60062

from itertools import permutations, combinations
from copy import deepcopy

def solution(n, weak, dist):
    N = n

    wall = [0] * n

    def fill_wall():
        for w in weak:
            wall[w] = 1

    def covered(D, W):
        for i in range(len(D)):
            d = D[i] + 1
            x = W[i]
            while d:
                if wall[x]:
                    wall[x] -= 1
                d -= 1
                x = (x + 1) % N
        for i in range(N):
            if wall[i]:
                return False
        return True

    for i in range(1, len(weak)+1):
        dist_s = list(permutations(dist, i))
        weak_s = list(combinations(weak, i))
        for D in dist_s:
            for W in weak_s:
                fill_wall()
                if covered(D, W): return i
    return -1

n = 12
weak = [1, 5, 6, 10]
dist = [1, 2, 3, 4]
print( solution(n, weak, dist) )

n = 12 
weak = [1, 3, 4, 9, 10]
dist = [3, 5, 7]
print( solution(n, weak, dist) )