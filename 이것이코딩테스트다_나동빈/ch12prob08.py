# 문자열 재정렬

def alpha_ord(c):
    return ord(c) - ord('A')

def get_alpha(n):
    return chr(n + ord('A'))

def solution(in_str):
    alpha = [0] * 26
    digit_sum = 0
    for c in in_str:
        if c.isalpha():
            alpha[ alpha_ord(c) ] += 1
        else:
            digit_sum += int(c)
    
    ret = ''
    for asci, cnt in enumerate(alpha):
        ret += get_alpha(asci) * cnt
    ret += str(digit_sum)

    return ret


in_str = 'K1KA5CB7'
# ABCKK13
print( solution(in_str) )

in_str = 'AJKDLSI412K4JSJ9D'
# ADDIJJJKKLSS20
print( solution(in_str) )