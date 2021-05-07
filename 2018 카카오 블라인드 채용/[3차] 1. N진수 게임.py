# https://programmers.co.kr/learn/courses/30/lessons/17687?language=python3
# 1. N 진수 게임
#
# 걸린 시간: 0:28

def get_num_str(n, num):
    num_str = ''
    while num:
        d = num % n
        num //= n
        if d == 10:
            num_str += 'A'
        elif d == 11:
            num_str += 'B'
        elif d == 12:
            num_str += 'C'
        elif d == 13:
            num_str += 'D'
        elif d == 14:
            num_str += 'E'
        elif d == 15:
            num_str += 'F'
        else:
            num_str += str(d)
    return num_str[::-1]

def solution(n, t, m, p):
    answer = ''
    whole_str = '0'

    num = 1
    while len(whole_str) <= t * m:
        whole_str += get_num_str(n, num)
        num += 1
    
    for i in range(0, t * m, m):
        answer += whole_str[i + p - 1]

    return answer

print( solution(2, 4, 2, 1) )