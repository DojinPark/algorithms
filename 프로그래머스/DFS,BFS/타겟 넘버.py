# https://programmers.co.kr/learn/courses/30/lessons/43165
# 타겟 넘버
# 걸린 시간: 0:06

def search(numbers, target, i = 0, num = 0):
    if i == len(numbers):
        if num == target: return 1
        else: return 0
    
    total = 0
    total += search(numbers, target, i + 1, num + numbers[i])
    total += search(numbers, target, i + 1, num - numbers[i])

    return total

def solution(numbers, target):
    answer = 0

    answer = search(numbers, target)

    return answer

print( solution([1, 1, 1, 1, 1], 3) ) # 5