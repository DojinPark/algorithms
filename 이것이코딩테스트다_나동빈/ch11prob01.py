# 모험가 길드

N = 5
a = [2, 3, 1, 2, 2]
# 2



# 모든 모험가를 그룹에 포함해야한다고 잘못 이해한 내 코드
a.sort(reverse=True)

answer = 0
i = 0
while i < len(a):
    answer += 1
    i += a[i]

print(answer)


# 모든 모험가를 그룹에 포함할 필요가 없는 코드
a.sort()
