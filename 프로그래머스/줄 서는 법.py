# https://programmers.co.kr/learn/courses/30/lessons/12936
# 줄 서는 법 (Level 3)
# 걸린 시간: 0:54
#
# 노트: iteration 구현 문제 풀 때 아직 헷갈리고 시간이 많이 든다.

def solution(n, k):
    answer = []
    nums = list( range(1, n+1) ) # nums: 순열에 들어갈 자연수 리스트

    k -= 1 # 인덱스 계산을 위해 k에서 1을 빼고 시작

    div = 1
    for f in range(1, n+1):
        div *= f
    
    while nums:
        div //= n # div: 오른쪽에서 n번째 수가 같은 경우의 수
        
        i = k // div # nums에서 남은 수
        
        answer.append(nums[i])
        del nums[i]
        
        k %= div
        n -= 1

    return answer

print( solution(4, 8) ) # 2, 1, 4, 3
# print( solution(10, 100) )