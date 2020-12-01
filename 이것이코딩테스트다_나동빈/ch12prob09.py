# 문자열 압축
#  https://programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    answer = len(s)

    for L in range(1, len(s)//2 + 1):
        prev_str = ''
        comp = []

        a = 0
        while a < len(s) - len(s) % L:
            # b = min(a + L, len(s))
            b = a + L
            now_str = s[a:b]
            if prev_str != now_str:
                comp.append(1)
            else:
                comp[-1] += 1
            prev_str = now_str
            a += L

        length = 0
        for c in comp:
            if c == 1:
                length += L
            else:
                length += L + len(str(c))
        length += len(s) % L

        answer = min(answer, length)
    
    return answer

# s = 'aabbaccc' # 7
# print( solution(s) )
# s = 'ababcdcdababcdcd' # 9
# print( solution(s) )
# s = 'abcabcdede' # 8
# print( solution(s) )
# s = 'abcabcabcabcdededededede' # 14
# print( solution(s) )
# s = 'xababcdcdababcdcd' # 17
# print( solution(s) )
# s = 'aaaaaaaabb' # 8a2b 4
# print( solution(s) )