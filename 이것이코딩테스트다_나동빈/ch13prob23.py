# 국영수
# https://www.acmicpc.net/problem/10825

# 국어 x 감소   a[1]   reverse
# 영어 y 증가   a[2]
# 수학 z 감소   a[3]   reverse
# 이름 사전순   a[0]

import sys
N = int( sys.stdin.readline().rstrip() )
A = []
for _ in range(N):
    name, x, y, z = sys.stdin.readline().rstrip().split()
    x = int(x)
    y = int(y)
    z = int(z)
    A.append( (name, x, y, z) )

A.sort(key = lambda a: a[0], reverse = False)
A.sort(key = lambda a: a[3], reverse = True)
A.sort(key = lambda a: a[2], reverse = False)
A.sort(key = lambda a: a[1], reverse = True)

for a in A:
    print(a[0])