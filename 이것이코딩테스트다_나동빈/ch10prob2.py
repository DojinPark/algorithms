# 팀 결성

N, M = 7, 8
commands_str = [
    '0 1 3',
    '1 1 7',
    '0 7 6',
    '1 7 1',
    '0 3 7',
    '0 4 2',
    '0 1 1',
    '1 1 1'
]
# NO
# NO
# YES

def find_root(root, a):
    if root[a] != a:
        root[a] = find_root(root, root[a])
    return root[a]

def union_team(root, a, b):
    a = find_root(root, a)
    b = find_root(root, b)
    if a < b:
        root[b] = a
    else:
        root[a] = b

def is_same_team(root, a, b):
    return root[a] == root[b]

root = [i for i in range(N + 1)]

for i in range(M):
    command, a, b = map(int, commands_str[i].split())
    if command == 0:
        union_team(root, a, b)
    if command == 1:
        answer = is_same_team(root, a, b)
        if answer == True:
            print('YES')
        else:
            print('NO')
