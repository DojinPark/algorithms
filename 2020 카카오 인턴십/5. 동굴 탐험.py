# https://programmers.co.kr/learn/courses/30/lessons/67260
# 5. 동굴 탐험
# 풀이 시간 초과

import sys
sys.setrecursionlimit(200009)

class Node:
    def __init__(self, val):
        self.val = val
        self.children = []

def dfs_tree(tree, path_dict, visited, x = 0):
    visited[x] = True
    for y in path_dict[x]:
        if not visited[y]:
            tree[y] = x
            dfs_tree(tree, path_dict, visited, y)

def dfs_cycle(root, visited):
    if visited[ root.val ]: return True
    else:
        visited[ root.val ] = True
        for child in root.children:
            if dfs_cycle(child, visited):
                return True
        return False
        
from collections import deque
def solution(n, path, order):
    answer = True

    tree = [i for i in range(n)]
    roots = {}
    path_dict = {}
    afters = set()
    befores = set()
    starts = set()

    for x, y in path:
        if x not in path_dict.keys():
            path_dict[x] = []
        if y not in path_dict.keys():
            path_dict[y] = []
        path_dict[x].append(y)
        path_dict[y].append(x)
    
    dfs_tree(tree, path_dict, [False] * n)

    for x, y in order:
        roots[x] = Node(x)
        roots[y] = Node(y)
        roots[x].children.append(roots[y])
        befores.add(x)
        afters.add(y)
    
    for x in befores:
        i = x
        while i != 0:
            i = tree[i]
            if i in afters:
                roots[i].children.append(roots[x])
                starts.add(i)
    
    visited = [False] * n
    for x in starts:
        # if visited[x]: continue
        if dfs_cycle(roots[x], [False] * n):
            return False
            # continue

    return True

n = 9
path = 	[[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]]
order = [[8,5],[6,7],[4,1]]
print( solution(n, path, order) )
# true

n = 9
path = [[8,1],[0,1],[1,2],[0,7],[4,7],[0,3],[7,5],[3,6]]
order = [[4,1],[5,2]]
print( solution(n, path, order) )
# true

n = 9
path = 	[[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]]
order = [[4,1],[8,7],[6,5]]	
print( solution(n, path, order) )
# false