# 두 배열의 원소 교체

A, B = [], []
N, K = 0, 0

N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort(reverse = True)
B.sort(reverse = True)

r = N-1
k = 0
# while r >= 0 and k < K:   # k <= K 로 쓰는 실수
                            # while 문의 조건은 언더플로, 오버플로만을 방지하고
                            # 이외의 조건은 while 문 안에서 break 하기
while r >= 0:
    if k == K:
        break
    if A[r] < B[0]:
        r -= 1
        k += 1
    else:
        break

X = A[:r+1] + B[:k]

print(A)
print(B)
print(r, k)
print(sum(X))
print(X)

# 5 3
# 1 2 5 4 3
# 5 5 6 6 5
#
# 26