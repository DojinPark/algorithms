# https://programmers.co.kr/learn/courses/30/lessons/64064
# 불량 사용자(복습)
# 걸린 시간: 0:42
#
# 노트: # set에서 다른 container로 변환시 원소 순서 랜덤인것 주의

def dfs(id_lists, i=0, acc=[], combs=set()):
    if i == len(id_lists):
        acc = set(acc)
        if len(acc) == len(id_lists):
            combs.add( tuple(sorted(acc)) ) # set에서 다른 container로 변환시 원소 순서 랜덤인것 주의
        return
    
    for id in id_lists[i]:
        acc.append(id)
        dfs(id_lists, i + 1, acc, combs)
        acc.pop()
    
    return len(combs)

import re
def get_list(user_id, banned):
    banned = banned.replace('*', '.')
    ret = []

    pat = re.compile(banned)
    for user in user_id:
        if len(user) == len(banned) and pat.match(user):
            ret.append(user)
    
    return ret

def solution(user_id, banned_id):
    answer = 0
    id_lists = []

    for banned in banned_id:
        id_lists.append(get_list(user_id, banned))
    
    answer = dfs(id_lists)

    return answer

# user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
# banned_id = ["fr*d*", "abc1**"]
# print( solution(user_id, banned_id) )