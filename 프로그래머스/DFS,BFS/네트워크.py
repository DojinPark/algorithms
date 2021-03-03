# https://programmers.co.kr/learn/courses/30/lessons/43162
# 네트워크
# 걸린 시간: 0:21
#
# 노트: union을 다 한 뒤에도 roots 어레이를 그대로 사용해서는 안되며,
#  적어도 한번은 모든 원소에 대해서 get_root()를 시행한 후에 사용할 수 있음

def get_root(roots, x):
    if roots[x] != x:
        roots[x] = get_root(roots, roots[x])
    return roots[x]

def union(roots, x, y):
    x = get_root(roots, x)
    y = get_root(roots, y)
    if x < y:
        roots[y] = x
    else:
        roots[x] = y

def solution(n, computers):
    answer = 0

    roots = [i for i in range(n)]
    for i in range(n - 1):
        for j in range(i + 1, n):
            if computers[i][j]:
                union(roots, i, j)
    
    networks = set()
    for i in range(n):
        networks.add( get_root(roots, i) )
    
    answer = len(networks)

    return answer

n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print( solution(n, computers) ) # 2

n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
print( solution(n, computers) ) # 1