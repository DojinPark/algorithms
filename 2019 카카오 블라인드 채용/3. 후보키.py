# https://programmers.co.kr/learn/courses/30/lessons/42890
# 3. 후보키
# 정답률: 16.09%  레벨 2
# 걸린시간: 0:33
#
# combination과 set을 이용하는 문제

from itertools import combinations
from copy import deepcopy

def solution(relation):
    answer = 0
    
    rows = len(relation)
    cols = len(relation[0])

    keys = []
    for length in range(1, cols + 1):
        keys += combinations(range(cols), length)

    candidates = set()

    # 작은 길이의 키 조합부터 확인
    for key in keys:

        # 데이터의 각 행별
        # key에 해당하는 열을 set 자료형에 모아서
        # set의 크기가 전체 행의 수와 같으면 uniqueness 만족
        uniqueness = set()
        for row in relation:
            uniqueness.add(tuple([row[i] for i in key]))
        if len(uniqueness) != rows: continue

        # 이전에 저장한 candidate key 중 
        # 현재 key의 부분 집합이 있으면 minimality를 만족하지 않음
        not_candidate = False
        for candidate in candidates:
            if set(candidate) & set(key) == set(candidate):
                not_candidate = True
                break
            
        if not_candidate: continue
        candidates.add(key)
    
    answer = len(candidates)

    return answer

relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
print( solution(relation) ) # 2