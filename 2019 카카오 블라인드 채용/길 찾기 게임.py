# https://programmers.co.kr/learn/courses/30/lessons/42892
# 길 찾기 게임
# 레벨 3
# 풀이 1 시간 초과
#
# 노트1: 컨디셔 떨어지는 저녁 시간에 풀이 X
# 노트2: 바이너리 트리의 표현법 두가지(리스트, 클래스) 익히기
# 노트3: 바이너리 서치 트리(BST) 구현법 익히기

import sys
sys.setrecursionlimit(10 ** 4)

EMPTY = -1
LIMIT_X = 100000
LIMIT_Y = 1000

class Node:
    def __init__(self, x, num):
        self.key = x
        self.num = num + 1
        self.left = None
        self.right = None

def __add_node(root, node):
    key, _, num = node
    if key < root.key:
        if not root.left:
            root.left = Node(key, num)
        else:
            __add_node(root.left, node)
    else:
        if not root.right:
            root.right = Node(key, num)
        else:
            __add_node(root.right, node)

def build_tree(nodeinfo):
    nodeinfo = [ (x, y, num) for num, (x, y) in enumerate(nodeinfo) ]
    nodeinfo.sort()
    nodeinfo.sort(key=lambda x: x[1], reverse=True)

    y_now = nodeinfo[0][1]
    root = Node(nodeinfo[0][0], nodeinfo[0][2])
    for i in range(1, len(nodeinfo)):
        __add_node(root, nodeinfo[i])
    
    return root

def preorder(root, container):
    container.append( root.num )
    if root.left:
        preorder(root.left, container)
    if root.right:
        preorder(root.right, container)

def postorder(root, container):
    if root.left:
        postorder(root.left, container)
    if root.right:
        postorder(root.right, container)
    container.append( root.num )

def solution(nodeinfo):
    answer = []
    root = build_tree(nodeinfo)

    ret = []
    preorder(root, ret)
    answer.append(ret)

    ret = []
    postorder(root, ret)
    answer.append(ret)

    return answer

nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
# [[7,4,6,9,1,8,5,2,3],[9,6,5,8,1,4,3,2,7]]
ref = [[7,4,6,9,1,8,5,2,3],[9,6,5,8,1,4,3,2,7]]
answer = solution(nodeinfo)
print(answer)
print(f'preorder: {"correct" if answer[0] == ref[0] else "wrong"}')
print(f'postorder: {"correct" if answer[1] == ref[1] else "wrong"}')