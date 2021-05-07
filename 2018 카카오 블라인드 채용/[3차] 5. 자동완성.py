# https://programmers.co.kr/learn/courses/30/lessons/17685
# 5. 자동완성
#
# 걸린 시간: 0:51

def solution(words):
    answer = 0
    N = len(words)
    MAX_LEN = 0
    mat = [[]]
    start_c = [0] * N

    words.sort()
    MAX_LEN = max(map(len, words))
    mat = [ [0] * MAX_LEN for _ in range(N) ]
    # cnts = [ [0] * MAX_LEN for _ in range(N) ]

    for r in range(N):
        word = words[r]
        for c in range( len(word) ):
            mat[r][c] = word[c]

    for w in range(N):
        
        for c in range(start_c[w], len(words[w])):
            answer += 1
            # cnts[w][c] += 1

            r = w + 1
            stop = True
            while r < N and start_c[w] == start_c[r] and mat[w][c] == mat[r][c]:
                stop = False

                start_c[r] = c + 1

                answer += 1
                # cnts[r][c] += 1

                mat[r][c] = 0
                r += 1

            if not stop: start_c[w] = c + 1
            if stop: break
    
    # for i in range(N):
    #     print(start_c[i], mat[i])
    # for cnt in cnts:
    #     print(cnt)

    return answer

print( solution(["go","gone","guild"]) )
print( solution(["abc","def","ghi","jklm"]) )
print( solution(["word","war","warrior","world"]) )