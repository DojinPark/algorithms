# https://programmers.co.kr/learn/courses/30/lessons/64063
# 4. 호텔 방 배정
# 정확성테스트 걸린 시간: 0:40
#
# 노트: union-find 알고리즘 응용 문제
# 노트: 정점의 개수는 적지만 정점 번호의 제한값이 매우 큰 경우
#       dict[정점 번호] = 부모 정점 번호 로 트리 표현

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
    N = len(room_number)
    answer = [0] * N
    parents = {}
    
    for i, n in enumerate(room_number):
        result = add(parents, n)
        answer[i] = result
    
    return answer

k = 10
room_number = [1,3,4,1,3,1]
print( solution(k, room_number) )
# [1,3,4,2,5,6]

k = 9
room_number = [1, 3, 6, 1, 7]
print( solution(k, room_number) )
# [1, 3, 6, 2, 7]
