# https://programmers.co.kr/learn/courses/30/lessons/17677
# 5. 뉴스 클러스터링
# 정답률: 41.84% (난이도: 중)
# 걸린시간: 0:20

def build_pairs(input):
    ret = []

    for i in range( len(input) - 1 ):
        if not input[i].isalpha(): continue
        if not input[i + 1].isalpha():
            i += 1
            continue
        ret.append( input[i:i+2] )
    
    return ret

def jaccard(pairs1, pairs2):
    pairs1.sort()
    pairs2.sort()

    # last index 선언시 -1 로 초기화하는 것 잊지 말기
    last_j = -1
    match = 0
    for i in range(len(pairs1)):
        # last index를 range에 넣을 때 last index + 1 을 넣는 것 잊지 말기
        for j in range(last_j + 1, len(pairs2)):
            if pairs1[i] == pairs2[j]:
                match += 1
                last_j = j
                break
    
    intersection = match
    union = len(pairs1) + len(pairs2) - match

    return 1 if union == 0 else intersection / union
            
from math import floor

def solution(str1, str2):
    answer = 0

    str1 = str1.lower()
    str2 = str2.lower()

    pairs1 = build_pairs(str1)
    pairs2 = build_pairs(str2)

    score = jaccard(pairs1, pairs2)
    
    answer = int(floor(score * 65536))

    return answer

str1 = "FRANCE"; str2 = "french"	#16384
print( solution(str1, str2) )
str1 = "handshake"; str2 = 	"shake hands"	#65536
print( solution(str1, str2) )
str1 = "aa1+aa2"; str2 = 		"AAAA12"	#43690
print( solution(str1, str2) )
str1 = "E=M*C^2"; str2 = 		"e=m*c^2"	#65536
print( solution(str1, str2) )