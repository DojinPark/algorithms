# https://programmers.co.kr/learn/courses/30/lessons/43163
# 단어 변환
# 걸린 시간 0:10

def is_near(wordA, wordB):
    diff = False
    for i in range(len(wordA)):
        if wordA[i] != wordB[i]:
            if not diff:
                diff = True
            else:
                return False
    return True

from collections import deque
def solution(begin, target, words):
    answer = 0

    q = deque()
    steps = {}
    for word in words:
        steps[word] = 0

    q.append(begin)
    steps[begin] = 1
    while q:
        now = q.popleft()
        for word in steps.keys():
            if not steps[word] and is_near(now, word):
                steps[word] = steps[now] + 1
                if word == target:
                    return steps[word] - 1
                q.append(word)

    return answer