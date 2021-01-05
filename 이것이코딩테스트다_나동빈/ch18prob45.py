# 최종 순위
# https://www.acmicpc.net/problem/3665
#
# 위상정렬 알고리즘

NO_ZERO_INDEGREE = -1

import sys
import itertools

# 위상정렬에 필요한 함수
# indegree가 0 이고 아직 방문한 적 없는 노드번호를 반환
def get_zero_indegree(indegree, visited):
    for i in range(len(indegree)):
        indeg = indegree[i]
        visit = visited[i]
        if not visit and indeg == 0:
            return i
    return NO_ZERO_INDEGREE

def solution():
    AB = []

    # 처음 순위를 그래프로 나타내고 indegree 리스트를 초기화함
    n = int(input())
    T = list( map(int, sys.stdin.readline().rstrip().split()) )

    graph = [ [False] * n for _ in range(n) ]
    indegree = [0] * n
    for i in range(n):
        for j in range(i+1, n):
            a, b = T[i] - 1, T[j] - 1
            graph[a][b] = True
            indegree[b] += 1

    # 순위가 뒤바뀐 경우를 그래프와 indegree 리스트에서 업데이트함
    m = int(input())
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        a -= 1
        b -= 1
        AB.append( (a, b) )

    for a, b in AB:
        indegree[a] += 1 - 2*graph[b][a]
        indegree[b] += 1 - 2*graph[a][b]
        graph[b][a] = not graph[b][a]
        graph[a][b] = not graph[a][b]

    # 위상 정렬 알고리즘
    visited = [False] * n
    rating = []
    i = 0
    while True:
        a = get_zero_indegree(indegree, visited)
        if a == NO_ZERO_INDEGREE: break
        visited[a] = True
        rating.append(a+1)

        for b in range(n):
            if graph[a][b]:
                graph[a][b] = False
                indegree[b] -= 1

    # 위상 정렬로 처리된 노드의 개수에 따라 IMPOSSIBLE 혹은 바뀐 순위를 출력
    num_visited = len([v for v in visited if v == True])
    if num_visited == 0: # 위상 정렬 과정에서 모든 노드를 방문하지 못한 체로 indegree가 0인 노드가 없는 경우는 cycle이 존재 하는 경우이며, 위상 정렬을 완료할 수 없다. 따라서 IMPOSSIBLE을 출력한다.
        print('IMPOSSIBLE')
        return
    elif num_visited < n:
        # 순위를 정확히 알 수 없는 경우는 위상 정렬 도중 indegree가 0 인 노드가 한번에 2개 이상 발견되는 경우이다.
        # 그러기 위해선 적어도 노드간 순위 관계가 빠져있는 경우가 있어야한다.
        # 하지만 이 문제는, 작년의 순위 결과에 따라 노드가 순위관계가 완전히 표현된 그래프가 이미 존재하며, 그 순위 관계를 뒤바꾼 결과를 다루므로 '?'를 출력해야하는 경우는 존재하지 않는다.
        # print('?')    # 오답
        print('IMPOSSIBLE')
        return
    else:
        for r in rating:
            print(r, end=' ')
        print()    
    

TEST_CASE = int( input() )
for _ in range(TEST_CASE):
    solution()