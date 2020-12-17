# 정렬된 배열에서 특정 수의 개수 구하기

from bisect import bisect_left as left
from bisect import bisect_right as right
def solution(N, x, a):
    l = left(a, x)
    r = right(a, x)
    if l == r: return -1
    else: return r - l

N, x = 7, 2
a = [1, 1, 2, 2, 2, 2, 3]
print(solution(N, x, a))

N, x = 7, 4
a = [1, 1, 2, 2, 2, 2, 3]
print(solution(N, x, a))