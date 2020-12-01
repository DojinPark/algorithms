# 문자열 뒤집기

# 내 풀이
# 문자열은 왼쪽부터 탐색하면서, 문자가 변하는 횟수 trans를 저장
# 0과 1 군집의 개수가 같은 경우 trans는 홀수이며, 정답은 trans/2 + 1임
# 0과 1 군집의 개수가 하나가 차이 나는 경우 trans는 짝수이며, 정답은 trans/2 임
# 두 경우를 종합하면 trans//2 + trans%2 와 같음
def solve(num_str):
    trans = 0
    prev_c = num_str[0]
    for i in range(1, len(num_str)):
        c = num_str[i]
        if prev_c != c:
            trans += 1
        prev_c = c
    
    return trans//2 + trans%2

num_str = '0001100'
# 1
print(solve(num_str))

num_str = '00011001'
# 2
print(solve(num_str))