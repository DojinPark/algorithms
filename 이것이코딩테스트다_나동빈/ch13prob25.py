# 실패율
# https://programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):

    instage = [0] * (N + 2)
    for stage in stages:
        instage[stage] += 1
    
    passed = instage[N + 1]
    for i in range(N, 0, -1):
        passed_temp = instage[i]
        if passed != 0:
            instage[i] = instage[i] / (instage[i] + passed)
        passed += passed_temp

    a = [(instage[i], i) for i in range(1, N+1)]

    # 스테이지 번호 먼저 오름차순으로 정렬
    # a.sort(key = lambda x: x[1])
    # 실패율을 내림차순으로 정렬
    a.sort(key = lambda x: x[0], reverse = True)

    answer = [ e[1] for e in a ]

    return answer

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print( solution(N, stages) )
# [3,4,2,1,5]

N = 4
stages = [4,4,4,4,4]
print( solution(N, stages) )
# [4,1,2,3]