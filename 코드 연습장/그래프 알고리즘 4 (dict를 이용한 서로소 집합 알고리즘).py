# 참고 문제: https://programmers.co.kr/learn/courses/30/lessons/64063
# 노드 번호값의 최대가 매우 큰 경우,
# dict로 부모 노드를 가리키는 방법을 이용해 그래프를 표현하면 된다.

def find(roots, x): # 재귀 거리 단축 find 함수
    if x not in roots.keys():
        return x
    roots[x] = find(roots, roots[x])
    return roots[x]

def union(roots, x, y):
    x = find(roots, x)
    y = find(roots, y)
    if x < y:
        roots[y] = x
    else:
        roots[x] = y

def build_trees(nodes):
    roots = {}
    
    for x, y in nodes:
        union(roots, x, y)
    
    print(roots.items())
    
nodes = [ (1, 5), (3, 2000), (5, 1000), (1000, -4), (5, 12345)]
build_trees(nodes)
