# 곱하기 혹은 더하기


# 나눗셈 등의 더 다양한 연산이 있을 때 일반적인 해법이 되는 내 풀이
# O(2^N)
def search(digit, num = 0, i = 0):
    ret = num
    if i == len(digit):
        return ret
    
    ret = max( ret, search(digit, num + digit[i], i + 1) )
    ret = max( ret, search(digit, num * digit[i], i + 1) )

    return ret

num_str = '02984'
# 576
digit = [int(d) for d in num_str]
print( search(digit) )

num_str = '567'
# 210
digit = [int(d) for d in num_str]
print( search(digit) )


# 0 또는 1만 더하기를 하는 책 풀이
# O(N)
# 그리디 문제는 구현이나 알고리즘 보단 브레인 티저 처럼 생각하고 풀자
def search(digit):
    ret = digit[0]

    for i in range(1, len(digit)):
        d = digit[i]
        if d <= 1 or ret <= 1:      # ret <= 1 조건으로 0과 1이 처음에 연속해서 등장하는 경우를 처리
            ret += d
        else:
            ret *= d

    return ret

num_str = '02984'
# 576
digit = [int(d) for d in num_str]
print( search(digit) )

num_str = '567'
# 210
digit = [int(d) for d in num_str]
print( search(digit) )