# https://programmers.co.kr/learn/courses/30/lessons/64065
# 2. 튜플
# 걸린 시간: 0:15

import re
def solution(s):
    answer = []
    d = []
    pat = re.compile(r'\d+(,\d+)*')

    start = 0
    while start < len(s):
        e = pat.search(s, start)
        if not e: break
        start = e.end()
        
        e = set( map(int, e.group(0).split(',')) )
        d.append(e)
    
    d.sort(key = lambda e: len(e))

    answer += d[0]
    for i in range(1, len(d)):
        answer += d[i] - d[i-1]

    return answer

s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
print( solution(s) )

s = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
print( solution(s) )

s = "{{20,111},{111}}"
print( solution(s) )

s = "{{123}}"
print( solution(s) )

s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"
print( solution(s) )