# https://programmers.co.kr/learn/courses/30/lessons/60059
# 자물소외 열쇠
# 걸린 시간: 0:27

def rotated(board):
    N = len(board)
    ret = [ [0] * N for _ in range(N) ]

    for r in range(N):
        for c in range(N):
            ret[r][c] = board[N - 1 - c][r]
    
    return ret

def get_pos_set(board, mark):
    ret = set()
    N = len(board)

    for r in range(N):
        for c in range(N):
            if board[r][c] == mark:
                ret.add( (r,c) )

    return ret

def try_key(M, N, key, lock, forbidden):
    for off_r in range(1 - M, N):
        for off_c in range(1 - M, N):
            offset_key = set( [(r + off_r, c + off_c) for (r, c) in key] )
            if forbidden & offset_key: continue
            if not lock - offset_key: return True
    
    return False

def solution(key, lock):
    M = len(key)
    N = len(lock)
    rotated_keys = [key]
    lock_set = set()
    forbidden_set = set()
    rotated_key_sets = []

    for _ in range(3):
        k = rotated_keys[-1]
        rotated_keys.append( rotated(k) )
    
    lock_set = get_pos_set(lock, 0)
    forbidden_set = get_pos_set(lock, 1)
    rotated_key_sets = [ get_pos_set(k, 1) for k in rotated_keys ]

    for key_set in rotated_key_sets:
        if try_key(M, N, key_set, lock_set, forbidden_set): return True
    
    return False

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print( solution(key, lock) )