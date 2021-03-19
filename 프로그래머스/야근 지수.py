# https://programmers.co.kr/learn/courses/30/lessons/12927?language=python3
# 야근 지수
# 걸린 시간: 0:50

# 노트: 처음에 works 메모리를 전혀 건드리지 않는 방법을 구현하려는데 너무 복잡했음
#       -> 그정도로 복잡한 문제는 잘 출제되지 않음! 너무 어렵게 생각하고 있을 확률이 높음
#       -> 뻔한 구현이라도 복잡도가 수백만 이하면 일단 구현해본다

def solution(n, works):
    answer = 0
    L = len(works)
    works_dict = {}

    works.sort(reverse=True)

    i = 0
    w = works[0]
    while n and w:
        while n and i < L and works[i] == w:
            works[i] -= 1
            n -= 1
            i += 1
        i = 0
        w = works[0]
    
    for work in works:
        if work not in works_dict.keys():
            works_dict[work] = 0
        works_dict[work] += 1

    for work, cnt in works_dict.items():
        answer += work * work * cnt

    return answer

works = [4, 3, 3]
n = 4
print(solution(n, works))

works = [2, 1, 2]
n = 1
print(solution(n, works))

works = [1, 1]
n = 3
print(solution(n, works))

works = [5, 5, 4, 4, 4, 2, 2, 1, 1]
n = 18
print(solution(n, works))
