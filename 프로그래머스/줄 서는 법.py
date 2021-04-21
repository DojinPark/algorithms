# https://programmers.co.kr/learn/courses/30/lessons/12936
# 줄 서는 법 (Level 3)
# 걸린 시간: 0:54
#
# 노트: iteration 구현 문제 풀 때 아직 헷갈리고 시간이 많이 든다.

def solution(n, k):
    answer = []
    nums = list( range(1, n+1) )

    k -= 1

    div = 1
    for f in range(1, n+1):
        div *= f
    
    while nums:
        div //= n
        i = k // div
        k %= div
        n -= 1
        
        answer.append(nums[i])
        del nums[i]

    return answer

print( solution(4, 8) ) # 2, 1, 4, 3
# print( solution(10, 100) )