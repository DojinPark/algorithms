# 부품 찾기

N, M = 0, 0
a, b = [], []

N = 5
a = [8, 3, 7, 9, 2]
M = 3
b = [5, 7, 9]
# no
# yes
# yes

# 이진 탐색 풀이
def search(a, v):
    l = 0
    r = len(a)-1
    while True:
        if r < l:
            return None
        mid = (r + l) // 2
        if a[mid] == v:
            return v
        if a[mid] < v:
            l = mid + 1
        elif v < a[mid]:
            r = mid - 1

for target in b:
    result = search(a, target)
    if result == None:
        print("no")
    else:
        print("yes")

# 계수 정렬 풀이
#
# 행렬 a의 원소 값(부품번호)의 최대 = 1,000,000 -> 행렬 만들만 함
radix = [0] * 1000001
for v in a:
    radix[v] += 1

for t in b:
    if radix[t]:
        print('yes')
    else:
        print('no')

# 파이썬 set을 이용한 풀이
check = set()
for v in a:
    check.add(v)

for t in b:
    if t in check:
        print('yes')
    else:
        print('no')