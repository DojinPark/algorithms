# 1이 될 떄까지
# N, K <= 100,000 이므로 시간복잡도 O(X lgX) 예상

N, K = map(int, input().rstrip().split())

# 내 풀이
# > 이 풀이가 필요한 경우
# 1. 나눗셈 할 수 있는 수가 2개 이상
# 이 경우는 아님
# 1. 뺄셈 할 수 있는 수가 2개 이상
#
# d의 각 원소를 그래프의 정점으로, 나눗셈 또는 뺄셈으로 수가 변화하는 것을 간선으로 생각하면, 최적 경로를 구하는데 memoization, 재귀함수, for반복문 등 요소 중 무엇이 필요한 지 알 수 있다.
d = [0]*(N + 1)
def rec(n, step=0):
    global K
    global d
    d[n] = step
    if n == 1:
        return step
    if N % K == 0:
        return rec(n // K, step + 1)
    return rec(n - 1, step + 1)

    return -1

print(rec(N))

# 책 풀이
# 탐색하지 않고 1. K로 나누기 2. 1 뺴기 우선순위로 연산을 하면 "최적의 해를 보장" 한다.
answer = 0

while N != 1:
    if N % K == 0:
        N //= K
    else:
        N -= 1
    answer += 1

print(answer)