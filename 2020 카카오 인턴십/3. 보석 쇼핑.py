# https://programmers.co.kr/learn/courses/30/lessons/67258
# 3. 보석 쇼핑
# 0:47

def solution(gems):
    answer = [1, len(gems)]

    all_gems = set()
    kind_gems = set()
    
    for gem in gems:
        all_gems.add(gem)

    i = 0
    kind_gems.add( gems[i] )
    if len(kind_gems) == len(all_gems):
        answer = [1, 1]

    for j in range(1, len(gems)):
        gem = gems[j]
        kind_gems.add(gem)

        while i + 1 <= j and gems[i] == gem:
            i += 1
        
        while i + 1 <= j and gems[i] == gems[i + 1]:
            i += 1
        
        if kind_gems == all_gems:
            if j - i < answer[1] - answer[0]:
                answer = [i + 1, j + 1]

    return answer

# gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
# print( solution(gems) )

# gems = ["AA", "AB", "AC", "AA", "AC"]
# print( solution(gems) )

# gems = ["XYZ", "XYZ", "XYZ"]
# print( solution(gems) )

# gems = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
# print( solution(gems) )