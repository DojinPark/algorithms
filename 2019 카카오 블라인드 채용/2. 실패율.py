# https://programmers.co.kr/learn/courses/30/lessons/42889
# 2. 실패율  레벨 1
# 정답률: 55.57%  걸린 시간: 0:30

def solution(N, stages):
    answer = []

    fail = [0] * (N + 2)

    for stage in stages:
        fail[stage] += 1
    
    passed = fail[N + 1]
    for i in range(N, 0, -1):
        curr_stage = fail[i]
        if passed + curr_stage == 0:
            fail[i] = 0
        else:
            fail[i] = curr_stage / (curr_stage + passed)
        passed += curr_stage
    
    fail = [ (f, stage) for stage, f in enumerate( fail ) ]
    answer = [ e[1] for e in sorted(fail[1:N+1], key=lambda x:x[0], reverse=True) ]

    return answer


N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print( solution(N, stages) )
# [3,4,2,1,5]

N = 4
stages =  	[4,4,4,4,4]
print( solution(N, stages) )
# [4,1,2,3]
