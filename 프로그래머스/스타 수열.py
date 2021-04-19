# https://programmers.co.kr/learn/courses/30/lessons/70130
# 스타 수열
# 걸린 시간: 0:51

def get_num_cnt(a):
    ret = {}
    for n in a:
        if n not in ret.keys():
            ret[n] = 0
        ret[n] += 1
    return ret

def get_star_len(a, num, cnt):
    checked = 0
    i = 1
    while i < len(a):
        if (a[i-1] != a[i]) and (a[i-1] == num or a[i] == num):
            checked += 1
            i += 1
        i += 1
    
    return 2 * checked

def solution(a):
    answer = 0

    num_cnt = get_num_cnt(a)

    num_cnt_list = sorted( [(c, n) for n, c in num_cnt.items()], reverse=True )
    
    for cnt, num in num_cnt_list:
        if cnt * 2 <= answer: break

        star_len = get_star_len(a, num, cnt)
        if answer > star_len: break

        answer = star_len

    return answer

d = [
[0]	#0
,[5,2,3,3,5,3]	#4
,[0,3,3,0,7,2,0,2,2,0]	#8
]

for a in d:
    print( solution(a) )