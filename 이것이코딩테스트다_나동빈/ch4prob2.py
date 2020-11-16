# 왕실의 나이트

COLS = 8
ROWS = 8
board = [ [0]*ROWS for _ in range(COLS) ]   # board[col][row]
dirs = [ (1,2), (2,1), (2,-1), (1,-2), (-1,-2), (-2,-1), (-2,1), (-1,2) ]

answer = 0

init_pos = input()
init_pos = (ord(init_pos[0]) - ord('a'), int(init_pos[1])-1)

def ok(pos, dir):
    new_pos = (pos[0] + dir[0], pos[1] + dir[1])
    for i in range(2):
        if new_pos[i] >= 8 or new_pos[i] < 0: return False
    return True

for dir in dirs:
    if ok(init_pos, dir):
        answer += 1

print(answer)