# 크루스칼 vs 프림
# 간선 vs 정점

V = 7
edges_str = [
    '1 2 29',
    '1 5 75',
    '2 3 35',
    '2 6 34',
    '3 4 7',
    '4 6 23',
    '4 7 13',
    '5 6 53',
    '6 7 25'
]
# Expected Output: 159

def get_root(roots, i):
    if roots[i] == i: return i
    else:
        roots[i] = get_root(roots, roots[i])
        return roots[i]

def union(roots, i, j):
    i = get_root(roots, i)
    j = get_root(roots, j)
    if i < j:
        roots[j] = i
    else:
        roots[i] = j

def is_cycle(roots, i, j):
    return get_root(roots, i) == get_root(roots, j)

# 크루스칼 알고리즘의 코드 바디 자체는 간단하다.
# 힙에다 간선을 싹 다 넣은 뒤
# 다시 하나 씩 힙에서 빼면서
# 사이클이 형성 되지 않는 간선이면 추가한다.
from heapq import heappush as push, heappop as pop
def kruskal(V, edges_str):
    edges = [ map(int, e.split()) for e in edges_str ]

    roots = [ i for i in range(V + 1) ]
    h = []
    sum = 0
    cnt = 0 # Early-Stop

    for a, b, c in edges:
        push(h, (c, a, b))
    
    while h:
        c, a, b = pop(h)
        if not is_cycle(roots, a, b):
            sum += c
            cnt += 1                # Early-
            if cnt == V - 1: break  # -Stop
            union(roots, a, b)

    return sum

print( kruskal(V, edges_str) )