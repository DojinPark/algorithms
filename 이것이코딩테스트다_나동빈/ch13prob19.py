# 연산자 끼워넣기
# https://www.acmicpc.net/problem/14888
#
# 파이썬에서 음수를 양수로 나눈 몫
# 을 C++ 와 같게 하려면
# -> a // b      (X)
# -> int(a / b)  (O)
#
# 2 <= N <= 11
# 연산자 1 <= N - 1 <= 10
# 10P10 = 3,628,800
# N <= 10 (11, 12 안됨. 10 까지만 가능) -> O(N!)

INF = int(1e9)
ADD = 0
SUB = 1
MUL = 2
DIV = 3

N = int( input() )
a = list( map(int, input().split()) )
b = list( map(int, input().split()) )

# itertools.permutations 를 이용한 풀이
# PyPy3 를 이용하지 않으면 시간 초과 걸림
def solution1():
    def calc(a, ops):
        ret = a[0]
        for i, op in enumerate(ops):
            if op == ADD:
                ret += a[i+1]
            elif op == SUB:
                ret -= a[i+1]
            elif op == MUL:
                ret *= a[i+1]
            elif op == DIV:
                ret = int(ret / a[i+1])
        return ret

    # 연산자 배열 처음으로 만들기
    op_seq = []
    for op, num in enumerate(b):
        op_seq += [op] * num

    # 연산자 배열의 순열 만들기
    from itertools import permutations
    op_perm = permutations(op_seq)

    # 연산자 배열에 대한 결과를 하나씩 확인하기
    min_result = INF
    max_result = -INF
    for ops in op_perm:
        result = calc(a, ops)
        min_result = min(min_result, result)
        max_result = max(max_result, result)

    print(max_result)
    print(min_result)


# 재귀 함수를 이용한 풀이
min_num = INF
max_num = -INF
def search(num, idx = 1): # 첫 호출에 num에 a[0]을 입력해야함
    global a
    global b
    global min_num, max_num

    if idx == N:
        min_num = min(min_num, num)
        max_num = max(max_num, num)

    if b[ADD]:
        b[ADD] -= 1
        search(num + a[idx], idx + 1)
        b[ADD] += 1

    if b[SUB]:
        b[SUB] -= 1
        search(num - a[idx], idx + 1)
        b[SUB] += 1

    if b[MUL]:
        b[MUL] -= 1
        search(num * a[idx], idx + 1)
        b[MUL] += 1

    if b[DIV]:
        b[DIV] -= 1
        search( int(num / a[idx]), idx + 1)
        b[DIV] += 1

    return min_num, max_num

search(a[0])
print(max_num)
print(min_num)