# https://programmers.co.kr/learn/courses/30/lessons/17682
# 다트 게임 (2018 카카오 블라인드 채용 1차)
# 
# 걸린 시간: 0:19
# 복습: RegEx로 다시 풀기 도전
# 노트: 걸린 시간이 동일함,.!!!

import re

def solution(dartResult):
    answer = 0
    pat = re.compile(r'(\d+)([SDT])([\*#])*')
    results = []
    points = [0] * 3

    i = 0
    while True:
        match = pat.search(dartResult, i)
        if not match: break

        p, m, o = match.groups()
        results.append( (p, m, o) )

        i = match.end()

    for i in range(3):
        p, m, o = results[i]

        points[i] = int(p)

        if m == 'D': points[i] **= 2
        elif m == 'T': points[i] **= 3

        if o == '*':
            points[i] *= 2
            if i > 0:
                points[i - 1] *= 2
        elif o == '#':
            points[i] *= -1
    
    for i in range(3):
        answer += points[i]

    return answer


d = [['1S2D*3T'	,37	    ]
,['1D2S#10S'	,9	    ]
,['1D2S0T'	,3]
,['1S*2T*3S'	,23]
,['1D#2S*3S'	,5]
,['1T2D3D#'	,-4]
,['1D2S3T*'	,59]]
for dartResult, answer in d:
    print(solution(dartResult))
