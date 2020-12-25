# 편집 거리
# 책 문제와는 다른
# https://www.acmicpc.net/problem/7620
# 으로 대체

import sys
from copy import deepcopy

MATCH = 1
DIFF = 0
END = -1

str1 = list(input())
str2 = list(input())
copy = deepcopy(str2)

str1.append(END)
str2.append(END)

i = 0
last_match_j = -1
while i < len(str1) - 1:
    matched = False
    for j in range(last_match_j + 1, len(str2) - 1):
        if str1[i] == str2[j]:
            str1[i] = MATCH
            str2[j] = MATCH
            last_match_j = j
            matched = True
            break
    if not matched:
        str1[i] = DIFF
    i += 1

for j in range(len(str2) - 1):
    if str2[j] != MATCH:
        str2[j] = DIFF

i = 0
j = 0
while str1[i] != END or str2[j] != END:
    if (str1[i] == MATCH or str1[i] == END) and str2[j] == DIFF:
        # sys.stdout.write('a ' + str2[j] + '\n')
        print('a', copy[j])
        j += 1
    elif str1[i] == DIFF and (str2[j] == MATCH or str2[j] == END):
        # sys.stdout.write('d ' + copy[j] + '\n')
        print('d', copy[j])
        i += 1
    elif str1[i] == DIFF and str2[j] == DIFF:
        # sys.stdout.write('m ' + copy[j] + '\n')
        print('m', copy[j])
        i += 1
        j += 1
    elif str1[i] == MATCH and str2[j] == MATCH:
        # sys.stdout.write('c ' + copy[j] + '\n')
        print('c', copy[j])
        i += 1
        j += 1