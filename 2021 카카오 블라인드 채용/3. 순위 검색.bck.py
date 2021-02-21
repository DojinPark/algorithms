# https://programmers.co.kr/learn/courses/30/lessons/72412
# 3. 순위 검색
# 정확성 통과 걸린 시간 0:25

from bisect import bisect_left
from bisect import bisect_right

feature_set = [ ['cpp', 'java', 'python'], \
    ['backend', 'frontend'], \
    ['junior', 'senior'], \
    ['chicken', 'pizza']
    ]

def build_tree(tree, i = 0):
    global feature_set

    if i == 4: return
    elif i == 3:
        for f in feature_set[i]:
            tree[f] = []
    elif i < 3:
        for f in feature_set[i]:
            tree[f] = {}
            build_tree(tree[f], i + 1)

def insert_to_tree(tree, person, i = 0):
    if i == 4:
        score = person[i]
        tree.append(score)
    else:
        select = person[i]
        insert_to_tree(tree[select], person, i + 1)

# 함수 인자로 받은 리스트를 sort 할 시 데이터가 없어지는 문제
# 왜 그런지 모르겠음! 풀이 중단
def sort_tree(tree, i = 0):
    global feature_set

    # if i == 4:
    #     tree.sort()
    if i == 3:
        for f in feature_set[i]:
            tree[f] = sorted(tree[f])
    else:
        for f in feature_set[i]:
            build_tree(tree[f], i + 1)

def search_tree(tree, q, i = 0):
    global feature_set

    select = q[i]
    
    if i == 4:
        x, y = 0, len(tree)
        x = bisect_left(tree, select, x, y)
        y = bisect_right(tree, select, x, y)
        return y - x
    elif i < 4:
        if select == '-':
            ret = 0
            for f in feature_set[i]:
                ret += search_tree(tree[f], q, i + 1)
            return ret
        else:
            return search_tree(tree[select], q, i + 1)

def printt(tree, stack = [], i = 0):
    global feature_set

    if i == 4:
        stack.append( tree )
        print(stack)
    elif i < 4:
        for f in feature_set[i]:
            printt(tree[f], stack + [f], i + 1)

def solution(info, query):
    answer = []

    N = len(info)
    Q = len(query)

    tree = {}
    build_tree(tree)

    for i, person in enumerate(info):
        a, b, c, d, e = person.split()
        e = int(e)
        insert_to_tree(tree, (a, b, c, d, e))

    printt(tree)
    sort_tree(tree)
    print()
    printt(tree)
    
    for i, q in enumerate(query):
        a, b, c, de = q.split(' and ')
        d, e = de.split()
        e = int(e)
        query[i] = (a, b, c, d, e)

    for q in query:
        cnt = search_tree(tree, q)
        answer.append(cnt)

    return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print( solution(info, query) )
# [1,1,1,1,2,4]