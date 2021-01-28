# 공유기 설치
# https://www.acmicpc.net/problem/2110
#
# Binary Search 응용 문제
#
# 유형 접근법
# 1. x의 제한 조건이 x <= 1,000,000,000 이다
#    -> O(lg x)에서 Binary Search를 유추
# 2. Binary Search의 변수, 범위, 조건을 설정해야함
#    -> 변수: 출력해야하는 정답이 "가장 가까운 두 공유기 사이의 거리의 최대" 이므로 "가장 가까운 두 공유기 사이의 거리" 즉, <두 공유기 사이 최소 거리>를 변수로 설정
#    -> Search 범위: <최소 거리>=1, <최대_거리>=(가장 오른쪽 집 x) - (가장 왼쪽 집 x)
#    -> Search 조건: <두 공유기 사이 최소 거리>를 만족하는 집을 가장 왼쪽 집 부터 골라냈을 때 최소 C개의 집이 나오나?

def solution(N, C, data):
    # N <= 200,000 에서 O(N lgN), 즉 정렬 해야함을 유추
    data.sort()

    max_dist = data[-1] - data[0]
    min_dist = 1
    answer = 0
    while min_dist <= max_dist:
        dist = (max_dist + min_dist) // 2
        # 가장 왼쪽 집은 무조건 포함하여 탐색
        # (가장 왼쪽 집과 가장 오른쪽 집을 포함하는것이 무조건 유리하다)
        prev_x = data[0]
        added = 1
        for x in data:
            if x - prev_x >= dist:
                added += 1
                prev_x = x
        
        if added < C:
            max_dist = dist - 1
        # 기본 Binary Search와 다른 부분
        # added == C 여도 탐색을 계속한다.
        else:
            answer = max(answer, dist)
            min_dist = dist + 1
    
    return answer
                

N, C = map(int, input().split())
data = []
for _ in range(N):
    data.append( int(input()) )

print( solution(N, C, data) )