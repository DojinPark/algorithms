# https://programmers.co.kr/learn/courses/30/lessons/42892
# 길 찾기 게임(복습)
# 걸린 시간: 0:36

import sys
sys.setrecursionlimit(int(1e9))

class Node:
    def __init__(self, key, number):
        self.key = key
        self.number = number
        self.left = False
        self.right = False

def __add_child(root, node):
    if node.key <= root.key:
        if not root.left:
            root.left = node
        else:
            __add_child(root.left, node)
    else:
        if not root.right:
            root.right = node
        else:
            __add_child(root.right, node)

def get_bst(nodeinfo):
    nodes = sorted( [(-level, x, number + 1) for number, (x, level) in enumerate(nodeinfo)] )
    root = Node(nodes[0][1], nodes[0][2])

    for i in range(1, len(nodes)):
        __add_child(root, Node(nodes[i][1], nodes[i][2]))

    return root


def get_preorder(root, ret=[]):
    if not root: return
    ret.append( root.number )
    get_preorder(root.left, ret)
    get_preorder(root.right, ret)
    return ret

def get_postorder(root, ret=[]):
    if not root: return
    get_postorder(root.left, ret)
    get_postorder(root.right, ret)
    ret.append( root.number )
    return ret

def solution(nodeinfo):
    answer = [[]]
    N = len(nodeinfo)

    root = get_bst(nodeinfo)
    preorder = get_preorder(root)
    postorder = get_postorder(root)

    answer = [preorder, postorder]

    return answer

nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
print( solution(nodeinfo) )