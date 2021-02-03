# https://programmers.co.kr/learn/courses/30/lessons/17682
# 2. 다트 게임
# 정답률: 73.47% (난이도: 하)
# 걸린시간: 0:19
#
# 한글자씩 떼어 해석하기. 10점 주의
# 또는 regex을 이용한 tokenization

def solution(dartResult):
    answer = 0

    points = []

    ten_flag = False
    for i in range( len(dartResult) ):
        c = dartResult[i]
        if c.isnumeric():
            if ten_flag:
                ten_flag = False
                continue
            if c == '1' and dartResult[i + 1] == '0':
                points.append(10)
                ten_flag = True
                continue
            points.append( int(c) )
        elif c.isalpha():
            if c == 'S':
                points[-1]
            elif c == 'D':
                points[-1] **= 2
            elif c == 'T':
                points[-1] **= 3
        else:
            if c == '*':
                if len(points) == 1:
                    points[0] *= 2
                else:
                    points[-1] *= 2
                    points[-2] *= 2
            elif c == '#':
                points[-1] *= -1

    # print(points) ###
    answer = sum(points)

    return answer

# dartResult = '1S2D*3T'
# print( solution(dartResult) )
# dartResult = '1D2S#10S'
# print( solution(dartResult) )
# dartResult = '1D2S0T'
# print( solution(dartResult) )
# dartResult = '1S*2T*3S'
# print( solution(dartResult) )
# dartResult = '1D#2S*3S'
# print( solution(dartResult) )
# dartResult = '1T2D3D#'
# print( solution(dartResult) )
# dartResult = '1D2S3T*'
# print( solution(dartResult) )
dartResult = '10D0D*1T*'
print( solution(dartResult) )

# 37
# 9
# 3
# 23
# 5
# -4
# 59