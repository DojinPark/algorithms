# https://programmers.co.kr/learn/courses/30/lessons/72412
# 3. 순위 검색
# 정확성 통과 걸린 시간: 0:25
# 효율성 통과 시도 2회
#
# 효율성 통과하려고 트리를 구성하려다 구현이 힘들어서 풀이 시간 초과
# 다시 생각하여 dict 형에 모든 조건 조합을 key로 구성하여 풀었음
#
# 노트: dict 타입의 key 를 복잡한 것이더라도 자유롭게 사용하기!
# (C++ 코딩을 잊어도 좋다!)

from bisect import bisect_left as left

def build_keys(org_key, keys, key = [], i = 0):
    if i == 4:
        keys.append( tuple(key) )
    else:
        build_keys(org_key, keys, key + [org_key[i]], i + 1)
        build_keys(org_key, keys, key + ['-'], i + 1)

def solution(info, query):
    answer = []

    N = len(info)
    Q = len(query)

    db = {}

    for i, person in enumerate(info):
        a, b, c, d, e = person.split()
        e = int(e)

        keys = []
        build_keys((a, b, c, d), keys)

        for key in keys:
            if not key in db.keys():
                db[key] = []
            db[key].append(e)
    
    for k, v in db.items():
        db[k].sort()
    
    for i, q in enumerate(query):
        a, b, c, de = q.split(' and ')
        d, e = de.split()

        key = (a, b, c, d)
        score = int(e)

        if key in db.keys():
            cnt = len(db[key]) - left(db[key], score)
        else:
            cnt = 0
        answer.append(cnt)

    return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print( solution(info, query) )
# [1,1,1,1,2,4]