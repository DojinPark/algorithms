# https://programmers.co.kr/learn/courses/30/lessons/72411
# 2. 메뉴 리뉴얼
# 걸린 시간: 0:25

from itertools import combinations

def solution(orders, course):
    answer = []

    courses_by_size = [ {} for _ in range(11) ]

    for order in orders:
        menus = list(order)
        menus.sort()
        for size in range(2, len(menus) + 1):
            courses = combinations(menus, size)
            for c in courses:
                c = ''.join(c)
                if c not in courses_by_size[size].keys():
                    courses_by_size[size][c] = 0
                courses_by_size[size][c] += 1
    
    for size in course:
        candidates = sorted(courses_by_size[size].items(), key=lambda item: item[1], reverse=True)
        if not candidates: continue
        max_orders = candidates[0][1]
        if max_orders < 2: continue
        for candidate in candidates:
            if candidate[1] == max_orders:
                # print(candidate, max_orders)
                answer.append(candidate[0])

    answer.sort()
    return answer


orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]	
print( solution(orders, course) ) # ["AC", "ACDE", "BCFG", "CDE"]

orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course = [2,3,5]	
print( solution(orders, course) ) # ["ACD", "AD", "ADE", "CD", "XYZ"]

orders = ["XYZ", "XWY", "WXA"]
course = [2,3,4]
print( solution(orders, course) ) # ["WX", "XY"]