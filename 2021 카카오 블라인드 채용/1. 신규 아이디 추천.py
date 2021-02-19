# https://programmers.co.kr/learn/courses/30/lessons/72410
# 1. 신규 아이디 추천
# 걸린 시간 0:25

import re

def solution(new_id):
    # print()
    # print()
    new_id = new_id.lower()
    # print(new_id)

    new_id = re.sub('[^a-z0-9-_.]', '', new_id)
    # print(new_id)

    new_id = re.sub(r'\.+', '.', new_id)
    # print(new_id)

    new_id = re.sub(r'\A\.', '', new_id)
    new_id = re.sub(r'\.\Z', '', new_id)
    # print(new_id)

    if not new_id: new_id = 'a'
    # print(new_id)

    if len(new_id) >= 16:
        new_id = new_id[:15]
        new_id = re.sub(r'\A\.', '', new_id)
        new_id = re.sub(r'\.\Z', '', new_id)
    elif len(new_id) <= 2: new_id += new_id[-1] * (3 - len(new_id))
    # print(new_id)

    return new_id

new_id = "...!@BaT#*..y.abcdefghijklm"
print( solution(new_id) )  # "bat.y.abcdefghi"

new_id = "z-+.^."
print( solution(new_id) )  # "z--"

new_id = "=.="
print( solution(new_id) )  # "aaa" 

new_id = "123_.def"
print( solution(new_id) )  # 	"123_.def"

new_id = "abcdefghijklmn.p"
print( solution(new_id) )  # 	"abcdefghijklmn"

