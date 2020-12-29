# 숨바꼭질

INF = int(1e9)
N, M = 6, 7
data = [
    [3, 6],
    [4, 3],
    [3, 2],
    [1, 3],
    [1, 2],
    [2, 4],
    [5, 2]
]

from heapq import heappush as push
from heapq import heappop as pop

e = [ [] for _ in range(N+1) ]
cost = [INF] * (N+1)
h = []

for d in data:
    x, y = d
    e[x].append(y)
    e[y].append(x)

c = 0
x = 1
cost[1] = 0
push(h, (c, x))

while h:
    c, x = pop(h)
    for y in e[x]:
        if c + 1 < cost[y]:
            cost[y] = c + 1
            push(h, (cost[y], y))

def filter(x):
    if x == INF: return 0
    else: return x

print(cost)
cost = list( map(filter, cost) )
max_c = max(cost)
max_i = -1
cnt = 0
for i in range(1, N+1):
    if cost[i] == max_c:
        if max_i == -1:
            max_i = i
        cnt += 1

print(cost)

print(max_i, max_c, cnt)