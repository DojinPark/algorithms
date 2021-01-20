# 가사 검색
# https://programmers.co.kr/learn/courses/30/lessons/60060

from bisect import bisect_left
from bisect import bisect_right
from copy import deepcopy

def solution(words, queries):
    answer = []
    words_reversed = [ word[::-1] for word in words ]

    words.sort()
    # words_reversed.sort(reverse=True)
    words_reversed.sort()

    words_by_len = [ [] for _ in range(10001) ]
    words_reversed_by_len = [ [] for _ in range(10001) ]

    for word in words:
        words_by_len[ len(word) ].append(word)
    for word in words_reversed:
        words_reversed_by_len[ len(word) ].append(word)

    for query in queries:

        if query[0] == '?':    # '?'가 왼쪽에 위차한 경우 뒤집어진 word와 비교
            l = bisect_left(words_reversed_by_len[len(query)], query[::-1].replace('?', 'a'))
            r = bisect_right(words_reversed_by_len[len(query)], query[::-1].replace('?', 'z'))
        else:               # '?'가 오른쪽에 위치한 경우 정방향 word와 비교
            l = bisect_left(words_by_len[len(query)], query.replace('?', 'a'))
            r = bisect_right(words_by_len[len(query)], query.replace('?', 'z'))

        answer.append(r-l)
        
    return answer

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
print( solution(words, queries) )
