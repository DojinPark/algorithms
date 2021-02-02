# https://programmers.co.kr/learn/courses/30/lessons/17679
# 
# 정확성: 90.9  걸린시간: 01:30


# m 높이 (board) (r)
# n 폭 (board[0]) (c)

import sys
sys.setrecursionlimit(10**5)

ERASED = 'e'

dr = [0, 1, 1, 1, 0, -1, -1, -1]
dc = [-1, -1, 0, 1, 1, 1, 0, -1]

def print_board(board):
    m = len(board)
    n = len(board[0])
    for r in range(m):
        for c in range(n):
            print(board[r][c], end = ' ')
        print()
    print()

def __erase(m, n, board, checked, r, c, who):
    global dr, dc

    if r < 0 or c < 0: return False
    if r + 1 >= m or c + 1 >= n: return False
    if board[r][c] == ERASED or board[r][c] != who or checked[r][c]: return False

    checked[r][c] = True

    if board[r + 1][c] == who and board[r][c + 1] == who and board[r + 1][c + 1] == who:
        for i in range(len(dr)):
            nr = r + dr[i]
            nc = c + dc[i]
            __erase(m, n, board, checked, nr, nc, who)
        board[r][c] = ERASED
        board[r + 1][c] = ERASED
        board[r][c + 1] = ERASED
        board[r + 1][c + 1] = ERASED
        return True

def erase(m, n, board):
    checked = [ [False] * n for _ in range(m) ] ###
    is_continue = False
    for r in range(m):
        for c in range(n):
            is_continue = is_continue or __erase(m, n, board, checked, r, c, board[r][c])
    return is_continue

def __pull_down(m, n, board, r, c):
    if r + 1 >= m: return
    if board[r][c] != ERASED and board[r + 1][c] == ERASED:
        board[r][c], board[r + 1][c] = board[r + 1][c], board[r][c]
        __pull_down(m, n, board, r + 1, c)

def pull_down(m, n, board):
    for c in range(n):
        for r in range(m - 2, -1, -1):
            __pull_down(m, n, board, r, c)

def count_erased(m, n, board):
    ret = 0
    for r in range(m):
        for c in range(n):
            if board[r][c] == ERASED: ret += 1
    return ret

def solution(m, n, board):
    answer = 0

    board = [ [c for c in line] for line in board ]

    is_continue = True
    # print_board(board)
    while is_continue:
        is_continue = erase(m, n, board)
        # print_board(board)
        pull_down(m, n, board)
        # print_board(board)

    answer = count_erased(m, n, board)

    return answer


m = 4;	n = 5;	board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]	
print( solution(m, n , board) ) # 14
m = 6;	n = 6;	board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]	
print( solution(m, n , board) ) # 15
m = 6; n = 6; board = ["OXXOXX", "OXXXXX", 'OOXXXX', 'OXXOXX', 'OXXXXX', 'OOXXXX']
print( solution(m, n, board) ) # 30

m = 6; n = 6; board = ['AABBEE','AAAEEE','VAAEEV','AABBEE','AACCEE','VVCCEE' ]
print( solution(m, n, board) ) # 32
print(solution(6,2, ["DD", "CC", "AA", "AA", "CC", "DD"]) )# 12
print(solution(8,2, ["FF", "AA", "CC", "AA", "AA", "CC", "DD", "FF"]) )# 8
print(solution(6,2, ["AA", "AA", "CC", "AA", "AA", "DD"])) # 8

print( solution(3,2, ["AA", "AA", "AB"])) # 4
print( solution(4,2, ["CC", "AA", "AA", "CC"]) )  # 8

print( solution(2,2,["AA", "AA"]) ) # 4
print( solution(2,2, ["AA", "AB"]) ) # 0

print( solution(6,6,['eEeEeE', 'EeEeEe', 'eEeEeE', 'EeEeEe', 'eEeEeE', 'EeEeEe']) ) # 36