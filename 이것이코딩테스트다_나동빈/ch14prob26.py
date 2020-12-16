# 카드 정렬하기
# https://www.acmicpc.net/problem/1715

import sys
from heapq import heappush as push
from heapq import heappop as pop

N = int( sys.stdin.readline() )
q = []
for _ in range(N):
    num = int(sys.stdin.readline())
    push(q, num)

answer = 0
if len(q) >= 2:
    while True:
        a = pop(q)
        if not q: break
        b = pop(q)
        answer += a + b
        push(q, a + b)

print(answer)
