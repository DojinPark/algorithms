# https://programmers.co.kr/learn/courses/30/lessons/17684
# 2. 압축
#
# 걸린 시간: 0:18

def solution(msg):
    answer = []

    d = {}
    for idx in range(1, 27):
        d[chr( ord('A') + idx - 1 )] = idx

    i = 0
    while i < len(msg):
        key = msg[i]

        while i + 1 < len(msg):
            longer_key = key + msg[i + 1]
            if longer_key in d.keys():
                key = longer_key
                i += 1
            else:
                idx += 1
                d[longer_key] = idx
                break
        
        answer.append( d[key] )
        i += 1
    
    return answer

print( solution('KAKAO') )