# https://programmers.co.kr/learn/courses/30/lessons/67256
# 1. 키패드 누르기
# 걸린 시간: 0:22

key_coord = [
    (3, 1),
    (0, 0),
    (0, 1),
    (0, 2),
    (1, 0),
    (1, 1),
    (1, 2),
    (2, 0),
    (2, 1),
    (2, 2)
]

def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def solution(numbers, hand):
    answer = []
    hands = ['L', 'R']

    L = (3, 0)
    R = (3, 2)

    coords = [key_coord[num] for num in numbers]

    for coord in coords:
        if coord[1] == 0:
            L = coord
            answer.append(0)
        elif coord[1] == 2:
            R = coord
            answer.append(1)
        else:
            L_d = dist(L, coord)
            R_d = dist(R, coord)
            if hand == 'left':
                if L_d <= R_d:
                    L = coord
                    answer.append(0)
                else:
                    R = coord
                    answer.append(1)
            elif hand == 'right':
                if L_d >= R_d:
                    R = coord
                    answer.append(1)
                else:
                    L = coord
                    answer.append(0)
    
    answer = ''.join( [hands[idx] for idx in answer] )

    
    return answer

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = 'right'
print( solution(numbers, hand) )
# "LRLLLRLLRRL"

numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = 'left'
print( solution(numbers, hand) )
# "LRLLRRLLLRR"

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
hand = 'right'
print( solution(numbers, hand) )
# "LLRLLRLLRL"