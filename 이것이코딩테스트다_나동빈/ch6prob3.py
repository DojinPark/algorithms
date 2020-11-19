# 성적이 낮은 순서로 학생 출력하기
# 3
# 홍길동 99
# 이순신 77
# 강감찬 88

N = 0
a = []

N = int(input())
for _ in range(N):
    temp = tuple(input().split())
    a.append( (temp[0], int(temp[1])) )

a.sort(key = lambda x: x[1])

for i in range(N):
    print(a[i][0], a[i][1], end=' ')