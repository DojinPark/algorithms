# 어두운 길
#
# Kruskal's 알고리즘
# 한줄 설명: 비용이 작은 간선 순서로, 사이클을 형성하지 않을 때 마다 연결하여 총 N-1 개의 간선을 연결
# 시간 복잡도: O(E logE) (간선 정렬 시간)
# 
# Kruskal vs Prim
# O(E logE) vs O(V^2) ( O(V logE) )
# Sparse Graph vs Dense Graph

N, M = 7, 11
Mstr = [
    '0 1 7',
    '0 3 5',
    '1 2 8',
    '1 3 9',
    '1 4 7',
    '2 4 5',
    '3 4 15',
    '3 5 6',
    '4 5 8',
    '4 6 9',
    '5 6 11'
]
E = [ list(map(int, line.split())) for line in Mstr ]


from heapq import heappush as push
from heapq import heappop as pop

def find_set_root(r, node):
    if r[node] != node:
        r[node] = find_set_root(r, r[node])
    return r[node]

def union(r, a, b):
    a = find_set_root(r, a)
    b = find_set_root(r, b)
    if a < b:
        r[b] = a
    else:
        r[a] = b

r = [i for i in range(N)]
h = []
for e in E:
    x, y, z = e
    push(h, (z, x, y))

total_saved = 0
for e in h:
    z, x, y = e
    if find_set_root(r, x) == find_set_root(r, y):
        total_saved += z
        continue
    union(r, x, y)

print(total_saved)