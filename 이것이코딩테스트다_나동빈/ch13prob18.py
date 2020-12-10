# 괄호변환
# https://programmers.co.kr/learn/courses/30/lessons/60058
#
# 카카오 기출 중에 이렇게 구현법을 다 알려주는 경우
# -> 깔끔한 코드로 빠르게 풀어서 다른 문제를 풀 시간 확보

def ok(p):
    balance = 0
    for i, c in enumerate(p):
        if c == '(': balance += 1
        elif c == ')': balance -= 1
        if balance < 0: return False
    return True

def solution(p):
    answer = ''

    if len(p) == 0:
        return ''

    ### 이 부분도 함수로 구현했으면 더 좋았을뻔! ###
    l, r = 0, 0
    cut = 0
    for i, c in enumerate(p):
        if c == '(': l += 1
        elif c == ')': r += 1
        if l == r: 
            cut = i
            break
    
    u = p[:cut+1]
    v = p[cut+1:]
    ##############################################

    v = solution(v)
    if ok(u): return u + v
    else:
        rest = u[1:-1]
        nrest = ''
        for c in rest:
            if c == '(':
                nrest += ')'
            elif c == ')':
                nrest += '('
        answer = '(' + v + ')' + nrest

    return answer
      b                                  