# https://programmers.co.kr/learn/courses/30/lessons/64061
# 1. 크레인 인형뽑기 게임
# 걸린 시간: 0:19

def solution(board, moves):
    answer = 0
    N = len(board)
    top = [0] * N
    stack = []

    for c in range(N):
        for r in range(N - 1, -1, -1):
            if board[r][c] == 0:
                top[c] = r + 1
                break

    for m in moves:
        m -= 1
        if top[m] < N:
            stack.append( board[top[m]][m] )
            top[m] += 1

            if len(stack) >= 2 and stack[-1] == stack[-2]:
                answer += 2
                stack.pop()
                stack.pop()

    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print( solution(board, moves) ) # 4