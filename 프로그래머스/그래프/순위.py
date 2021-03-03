# https://programmers.co.kr/learn/courses/30/lessons/49191
# 순위
# 풀이 시간 초과
#
# 노트: 위상 정렬 문제라고 생각했는데 그렇게 풀 수 없는 문제였다!
#      위상 정렬 문제였으면 노드의 개수가 100개 보다는 훨씬 많아야 했다
#      위상 정렬의 시간복잡도는 O(V + E) 이므로 N = 십만 ~ 백만 정도로 예상

from collections import deque

def count_ancesters(edges, visited, a):
    total = 0
    for b in edges[a]:
        if not visited[b]:
            visited[b] = True
            total += 1
            total += count_ancesters(edges, visited, b)
    return total

def solution(n, results):
    answer = 0

    forwards = [ [] for _ in range(n) ]
    backwards = [ [] for _ in range(n) ]
    for a, b in results:
        forwards[a - 1].append(b - 1)
        backwards[b - 1].append(a - 1)
    
    for x in range(n):
        visited = [False] * n
        a = count_ancesters(forwards, visited, x)
        b = count_ancesters(backwards, visited, x)
        if a + b == n - 1:
            answer += 1

    return answer