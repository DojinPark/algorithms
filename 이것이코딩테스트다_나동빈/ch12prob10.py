# 자물쇠와 열쇠
#
# https://programmers.co.kr/learn/courses/30/lessons/60059

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

    for key in keys:
        for R in range(0, M + N):
            for C in range(0, M + N):

                for r in range(0, M):
                    for c in range(0, M):
                        globe[R + r][C + c] ^= key[r][c]

                success = True
                for r in range( max(M, R), min(M + N, R + 1) ):
                    for c in range( max(M, R), min(M + N, R + 1) ):
                        if not globe[r][c]:
                            success = False
                            break
                    if not success: break
                
                if open: return True

                for r in range(0, M):
                    for c in range(0, M):
                        globe[R + r][C + c] ^= key[r][c]
                        
    return False



key = [ [0, 0, 0], 
        [1, 0, 0],
        [0, 1, 1]]

lock = [[1, 1, 1],
        [1, 1, 0],
        [1, 0, 1]]
# true
print( solution(key, lock) )