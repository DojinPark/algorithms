# https://programmers.co.kr/learn/courses/30/lessons/12946
# 하노이의 탑 (Level 3)
# 걸린 시간 1:11
#
# 노트: "다른 언어로 풀었다면 해쉬테이블과 어레이리스트 선언을
#       비교적 자유롭게 사용하지 못해서 못풀지 않았을까" 하는
#       생각을 버리고, 파이썬의 문법적 이점 dict를 자유롭게 활용하자.

to_alpha = {}
to_alpha[1] = 'x'
to_alpha[2] = 'y'
to_alpha[3] = 'z'

to_12 = {}
to_12['x'] = 1
to_12['y'] = 3
to_12['z'] = 2

to_23 = {}
to_23['x'] = 2
to_23['y'] = 1
to_23['z'] = 3

def solution(n):
    answer = []

    d = [[1,3]]

    while n > 1:
        n -= 1

        d_alpha = [ [to_alpha[a], to_alpha[b]] for a, b in d ]
        d12 = [ [to_12[x], to_12[y]] for x, y in d_alpha ]
        d23 = [ [to_23[x], to_23[y]] for x, y in d_alpha ]

        d = d12 + [[1,3]] + d23

    answer = d

    return answer

# print( solution(3) )