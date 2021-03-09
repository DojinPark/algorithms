# https://programmers.co.kr/learn/courses/30/lessons/64064
# 3. 불량 사용자
# 풀이 시간 초과
#
# 노트: set형에서 list나 tuple로 자동 형 변환 시 순서가 랜덤인 것 같음
# 노트: itertools.product에 list of lists 사용시
#       *(asterisk)를 이용한 unpacking 해야 함
#       예) product(*lists)



# # dfs 5번 테스트케이스 시간 초과
# def dfs(matches, combined=[], d=0):
#     if d == len(matches):
#         return [tuple( set(combined) )]
#
#     ret = []
#     for match in matches[d]:
#         combined.append(match)
#         ret += dfs(matches, combined, d + 1)
#         combined.pop()
#
#     return ret

import re
from itertools import product
def solution(user_id, banned_id):
    answer = 0
    N = len(banned_id)
    matches = [ [] for _ in range(N) ]
    results = set()

    for i, ban in enumerate(banned_id):
        s = ban.replace('*', '\w')
        pat = re.compile(s)

        for user in user_id:
            if len(user) != len(ban): continue
            if pat.search(user):
                matches[i].append(user)
        
        # matches[i].sort()

    ret = product(*matches)
    
    for r in ret:
        r = set(r)
        if len(r) == N:
            results.add( tuple(sorted(r)) )
    
    answer = len(results)

    return answer

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "abc1**"]
print( solution(user_id, banned_id) )

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["*rodo", "*rodo", "******"]
print( solution(user_id, banned_id) )

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "*rodo", "******", "******"]
print( solution(user_id, banned_id) )