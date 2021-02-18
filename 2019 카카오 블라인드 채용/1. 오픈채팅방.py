# https://programmers.co.kr/learn/courses/30/lessons/42888
# 1. 오픈채팅방
# 정답률: 59.91% 레벨 2
# 걸린시간: 0:10

ENTER = 1
LEAVE = 2

def solution(record):
    answer = []
    
    names = {}
    history = []

    for line in record:
        line = list(line.split())
        op, uid = line[:2]
        if op == 'Enter':
            names[uid] = line[2]
            history.append( (ENTER, uid) )
        elif op == 'Leave':
            history.append( (LEAVE, uid) )
        elif op == 'Change':
            names[uid] = line[2]
    
    for op, uid in history:
        if op == ENTER:
            msg = names[uid] + '님이 들어왔습니다.'
        elif op == LEAVE:
            msg = names[uid] + '님이 나갔습니다.'
        answer.append(msg)

    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print( solution(record) )