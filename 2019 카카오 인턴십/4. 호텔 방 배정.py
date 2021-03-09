# https://programmers.co.kr/learn/courses/30/lessons/64063
# 4. 호텔 방 배정
# 정확성테스트 걸린 시간: 0:40
#
# 노트: union-find 알고리즘 응용 문제
#       - union 할 노드 pair가 직접적으로 주어지지 않고,
#         방 번호가 겹치는 경우에 해당함
#       - union 해야할 필요가 없는 새 노드를 추가할 때는,
#         (자신의 노드 번호 + 1)을 부모 노드 번호 디폴트 값으로 지정해야함
# 노트: 정점의 개수는 적지만 노드 번호의 제한값이 매우 큰 경우
#       dict[노드 번호] = 부모 노드 번호 로 트리 표현

import sys
sys.setrecursionlimit(10**9)

def find(parents, x):
    if x not in parents.keys():
        return x
    parents[x] = find(parents, parents[x])
    return parents[x]

def add(parents, x):
    x = find(parents, x)
    parents[x] = x + 1
    return x

def solution(k, room_number):
    parents = {}
    
    for i, n in enumerate(room_number):
        room_number[i] = add(parents, n)
    
    return room_number

k = 10
room_number = [1,3,4,1,3,1]
print( solution(k, room_number) )
# [1,3,4,2,5,6]

k = 9
room_number = [1, 3, 6, 1, 7]
print( solution(k, room_number) )
# [1, 3, 6, 2, 7]
