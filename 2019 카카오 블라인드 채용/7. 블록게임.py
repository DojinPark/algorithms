# https://programmers.co.kr/learn/courses/30/lessons/42894
# 7. 블록게임
# 정답률: 5.85%  레벨 4
# 걸린 시간: 1:26

# 없앨 블록 모양을 찾는 기능을 구현하는게 핵심인 문제 (checks 배열)

N = 0
BLACK = 201

checks = [  [(0,0), (0,1),  (0,2),  (1,0),  (1,1),  (1,2)],\
            [(-1,0),(-1,1), (-1,2), (0,0),  (0,1),  (0,2)], \
            [(0,0), (1,0),  (2,0),  (0,1),  (1,1),  (2,1)], \
            [(0,-1),(1,-1), (2,-1), (0,0),  (1,0),  (2,0)], \
            [(0,-1),(0,0),  (0,1),  (1,-1), (1,0),  (1,1)], \
            [(0,-2),(0,-1), (0,0),  (1,-2), (1,-1), (1,0)] \
         ]
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def printb(board):
    global N
    for r in range(N):
        for c in range(N):
            print(board[r][c], end = '\t')
        print()
    print()

def ok(r, c):
    global N
    return r >= 0 and r < N and c >= 0 and c < N

def __pull_down(board, r, c):
    global N
    
    while ok(r + 1, c) and board[r + 1][c] == 0:
        board[r + 1][c], board[r][c] = board[r][c], board[r + 1][c]

def add_black(board, c):
    global N

    r = 0
    for r in range(N - 1, -1, -1):
        if board[r][c] == BLACK:
            __pull_down(board, r, c)

    if board[r][c] == 0:
        board[r][c] = BLACK
        __pull_down(board, 0, c)
        return True # is_continue
    else:
        return False
    
def check_block(board, r, c):
    for check in checks:
        block_cnt = 0
        black_cnt = 0
        # print(len(check), end = ' ')
        for ddr, ddc in check:
            nr = ddr + r
            nc = ddc + c
            if not ok(nr, nc): break
            if board[nr][nc] == BLACK:
                black_cnt += 1
            if board[nr][nc] == board[r][c]:
                block_cnt += 1
        # print(cnt)
        if black_cnt == 2 and block_cnt == 4:
            # print(board[r][c], 'shape=',check)
            return True
    return False

def remove_block(board, r, c):
    global dr, dc
    num = board[r][c]
    board[r][c] = 0
    for i in range(4):
        nr = dr[i] + r
        nc = dc[i] + c
        if ok(nr, nc) and board[nr][nc] == num:
            remove_block(board, nr, nc)

def solution(board):
    global N
    N = len(board)
    answer = 0

    printb(board)

    is_continue = True
    while is_continue:
        is_continue = False
        # 한 행의 검은 블럭 추가
        for c in range(N):
            is_added = add_black(board, c)
            is_continue = is_continue or is_added
        if not is_continue:
            printb(board)
        
        checked_block = set()
        for r in range(N):
            for c in range(N):
                if board[r][c] > 0 and board[r][c] < BLACK and board[r][c] not in checked_block:
                    checked_block.add(board[r][c])
                    new_score = check_block(board, r, c)
                    if new_score:
                        remove_block(board, r, c)
                        is_continue = True
                        answer += new_score

    # printb(board)
    return answer

board = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,4,0,0,0],[0,0,0,0,0,4,4,0,0,0],[0,0,0,0,3,0,4,0,0,0],[0,0,0,2,3,0,0,0,5,5],[1,2,2,2,3,3,0,0,0,5],[1,1,1,0,0,0,0,0,0,5]]
print( solution(board) )