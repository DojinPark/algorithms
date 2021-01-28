# 공유기 설치
# https://www.acmicpc.net/problem/2110

def solution(N, C, data):
    data.sort()

    max_dist = data[-1] - data[0]
    min_dist = 1
    answer = 0
    while min_dist <= max_dist:
        dist = (max_dist + min_dist) // 2
        added = 1
        prev_x = data[0]
        for x in data:
            if x - prev_x >= dist:
                added += 1
                prev_x = x
        
        if added < C:
            max_dist = dist - 1
        else:
            answer = max(answer, dist)
            min_dist = dist + 1
    
    return answer
                

N, C = map(int, input().split())
data = []
for _ in range(N):
    data.append( int(input()) )

print( solution(N, C, data) )