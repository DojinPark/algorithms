# 자물쇠와 열쇠

from copy import deepcopy

def rotate_key(key):
    M = len(key)
    ret = [ [0] * M for _ in range(M) ]
    offset = [ [ (M - 1 - r - c, r - c)  for c in range(M)] for r in range(M)]

    for r in range(M):
        for c in range(M):
            ret[r + offset[r][c][0]][c + offset[r][c][1]] = key[r][c]

    return ret

def solution(key, lock):
    N = len(lock)
    M = len(key)
    L = N + 2*M
    globe = [ [0] * L for _ in range(L) ]
    
    # 지도 위에 lock 복사
    for r in range(M, M + N):
        for c in range(M, M + N):
            globe[r][c] = lock[r-M][c-M]
    
    keys = []
    keys.append(key)
    keys.append( rotate_key(keys[0]) )
    keys.append( rotate_key(keys[1]) )
    keys.append( rotate_key(keys[2]) )

    for r in range(



key = [ [0, 0, 0], 
        [1, 0, 0],
        [0, 1, 1]]

lock = [[0, 0, 0],
        [1, 0, 0],
        [0, 1, 1]]
# true
print( solution(key, lock) )