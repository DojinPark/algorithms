# 도시 분할 계획

V, E = 7, 12
edges_str = [
    '1 2 3',
    '1 3 2',
    '3 2 1',
    '2 5 2',
    '3 4 4',
    '7 3 6',
    '5 1 5',
    '1 6 2',
    '6 4 1',
    '6 5 3',
    '4 5 3',
    '6 7 4'
]
# Expected Output: 8

def find_root(root, a):
    if root[a] != a:
        root[a] = find_root(root, root[a])
    return root[a]

def is_cycle(root, a, b):
    return find_root(root, a) == find_root(root, b)

def union_root(root, a, b):
    a = find_root(root, a)
    b = find_root(root, b)
    if a < b:
        root[b] = a
    else:
        root[a] = b

root = [ i for i in range(V + 1) ]
edges = []
for edge_str in edges_str:
    a, b, c = map(int, edge_str.split())
    edges.append( (c, a, b) )

edges.sort()


total_cost = 0
connected = 0
for edge in edges:
    c, a, b = edge
    if is_cycle(root, a, b):
        continue
    
    union_root(root, a, b)
    total_cost += c

    connected += 1
    if connected == V - 2:
        break

print(total_cost)