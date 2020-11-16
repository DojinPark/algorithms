# 큰 수의 법칙
data = []
answer = 0

N, M, K = map(int, input().rstrip().split())
data = list( map(int, input().rstrip().split()) )

data.sort()
first = data[-1]
second = int()
first_cnt = 0
for i in range(-1, -len(data), -1):
    if first == data[i]:
        first_cnt += 1
    else:
        second = data[i]
        break
K *= first_cnt

# Solution #1
# M 이 큰 경우 시간초과
kcnt = 0
for _ in range(M):
    if kcnt == K:
        answer += second
        kcnt = 0
    else:
        answer += first
        kcnt += 1

print(answer)

# Solution #2
# "반복되는 수열" 원리로 풀기
X = first_cnt * K + 1   # [first, first, ... , second] 수열의 반복 횟수
answer = (M // X) * (first * first_cnt * K + second) + (M % X) * (first) # (수열 전체가 반복되는 횟수) * (수열 안의 수 전체 합) + (잘린 수열의 길이) * (최대인 수)     참고: 차최대인 수는 잘린 수열에 포함 될 수 없다
print(answer)