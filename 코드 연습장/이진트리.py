# Complete Binary Tree
#            0
#    1             2
#  3     4       5   6
# 7 8   9 10   11
EMPTY = -1
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, EMPTY, EMPTY, EMPTY]

def left_child(a, parent):
    i = parent*2 + 1
    if i >= len(a) or a[i] == EMPTY: return None
    return a[i]

def right_child(a, parent):
    i = parent*2 + 2
    if i >= len(a) or a[i] == EMPTY: return None
    return a[i]

def parent(a, child):
    i = (child - 1) >> 1
    if i >= len(a) or a[i] == EMPTY: return None
    return a[i]

# Works only with indices
def least_common_ancestor(a, l, r):
    l_ancestors = []
    r_ancestors = set()

    i = l
    l_ancestors.append(i)
    while i != 0:
        i = (i-1) >> 1
        l_ancestors.append(i)

    i = r
    r_ancestors.add(i)
    while i != 0:
        i = (i-1) >> 1
        r_ancestors.add(i)
    
    for ancestor in l_ancestors:
        if ancestor in r_ancestors: return ancestor
    
    return None

print(f'left child of 5 is {left_child(a, 5)}')
print(f'right child of 3 is {right_child(a, 3)}')
print(f'parent of 11 is {parent(a, 11)}')
print(f'parent of 10 is {parent(a, 10)}')
print(f'LCA of 9 and 3 is {least_common_ancestor(a, 9, 3)}')

# ↙
def preorder(a, i = 0):
    if i == None: return
    print(a[i], end=' ')
    preorder(a, left_child(a, i))
    preorder(a, right_child(a, i))

# →
def inorder(a, i = 0):
    if i == None: return
    inorder(a, left_child(a, i))
    print(a[i], end=' ')
    inorder(a, right_child(a, i))

# ↑
def postorder(a, i = 0):
    if i == None: return
    postorder(a, left_child(a, i))
    postorder(a, right_child(a, i))
    print(a[i], end=' ')

# ↓
from collections import deque
def level_order(a, i = 0):
    q = deque()
    q.append(i)
    while q:
        i = q.popleft()
        if i == None: continue
        
        print(a[i], end=' ')
        q.append( left_child(a, i) )
        q.append( right_child(a, i) )

preorder(a); print()
inorder(a); print()
postorder(a); print()
level_order(a); print()