# 뱀
# https://www.acmicpc.net/submit/3190
#
# 구현문제 풀 떄 실 수 막고 빠르게 코딩하는 법
# 종이 위에 두가지를 직접 써보기
# 1. 주어진 모든 예시 직접 시뮬레이션 해보기. (모든 숫자를 정확히 기록하면서 해보기)
# 2. 슈도 코드를 한국어로 쓰고 나서 코딩하기 (동작의 순서나 제약조건 등 모두 명확히 생각하면서 해보기)

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

BODY = 1
APPLE = 2

from collections import deque

def test(globe):
    for r in range(1, len(globe)):
        for c in range(1, len(globe[0])):
            print(globe[r][c][1], end=' ')
        print()

def dir_turned(turn_dir, dir):
    if turn_dir == 'L':
        return (dir + 3) % 4
    elif turn_dir == 'D':
        return (dir + 1) % 4

def moved(body, dir):
    if dir == UP:
        return (body[0] - 1, body[1])
    elif dir == RIGHT:
        return (body[0], body[1] + 1)
    elif dir == DOWN:
        return (body[0] + 1, body[1])
    elif dir == LEFT:
        return (body[0], body[1] - 1)

def solution():
    N, K, L = 0, 0, 0
    apples, turns = [], deque()

    N = int(input())
    K = int(input())
    for _ in range(K):
        apples.append( tuple(map(int, input().split())) )
    L = int(input())
    for _ in range(L):
        t = input().split()
        turns.appendleft( (int(t[0]), t[1]) )
    
    globe = [ [(0, RIGHT)] * (N + 1) for _ in range(N + 1) ]
    head = (1, 1)
    tail = (1, 1)
    T = 0

    # 사과 놓기
    for r, c in apples:
        globe[r][c] = (APPLE, RIGHT)

    def ok(body):
        return (1 <= body[0] and body[0] <= N) and (1 <= body[1] and body[1] <= N) and (globe[body[0]][body[1]][0] != BODY)

    while True:
        if turns:
            turn_t, turn_dir = turns.pop()
        while True:
            T += 1

            is_apple = False
            
            head_dir = globe[head[0]][head[1]][1]
            tail_dir = globe[tail[0]][tail[1]][1]

            head = moved(head, head_dir)
            if not ok(head):
                return T
            if globe[head[0]][head[1]][0] == APPLE: is_apple = True
            globe[head[0]][head[1]] = (BODY, head_dir)

            if not is_apple:
                globe[tail[0]][tail[1]] = (0, tail_dir)
                tail = moved(tail, tail_dir)
            
            if T == turn_t:
                break

        head_dir = dir_turned(turn_dir, head_dir)
        globe[head[0]][head[1]] = (BODY, head_dir)

    return T

print(solution())