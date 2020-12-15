# 안테나
# https://www.acmicpc.net/problem/18310

N = int(input())
A = list( map(int, input().split()) )

A.sort()

m = (N - 1) // 2

print(A[m])