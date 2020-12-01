# 럭키 스트레이트

def solution(N_str):
    if sum( [int(n) for n in N_str[:len(N_str)//2]] ) == sum( [int(n) for n in N_str[len(N_str)//2:]] ):
        return "LUCKY"
    else:
        return "READY"


N_str = '123402'
# LUCKY
print( solution(N_str) )

N_str = '7755'
# READY
print( solution(N_str) )