# 바닥 공사

N = 3
# 5

# Bottom-Up
# 점화식: m[i] = m[i-1] + 2*m[i-2]
m = [0] * N
m[0] = 1
m[1] = 3
for i in range(2, N):
    m[i] = (m[i - 1] + 2*m[i - 2]) % 796796

print(m[-1])