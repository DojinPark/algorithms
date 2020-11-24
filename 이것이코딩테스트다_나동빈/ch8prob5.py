# 효율적인 화폐 구성
INF_COINS = 10001

def solve(N, M, a):
    d = [0] * (M + 1)
    d[M] = -1
    a.sort()

    for i in range(N):  # 초기화 작업을 해주지 않은 경우 예시) 3원 짜리가 있고, 목표 총액이 4원일 때, 총액에 도달할 수 없다는 것이 정답임. (아래주석참조)
        if a[i] <= M: 
            d[a[i]] = 1

    for total in range(1, M+1):
        min_coins = INF_COINS
        for i in range(N):
            if total - a[i] >= 1 and d[total - a[i]]: # 해당 DP테이블 원소가 초기화 되었는지 확인하지 않으면 총액이 4원일때 3원을 추가하게 됨. 하지만 그렇게 동작하려면 1원을 추가한 적이 있어야 하므로 오답임.
                min_coins = min(min_coins, d[total - a[i]])
        if min_coins != INF_COINS:
            d[total] = min_coins + 1
    print(d)
    return d[M]

N, M = 2, 15
a = [2, 3]
# 5
print(solve(N, M, a))

N, M = 3, 4
a = [3, 5, 7]
# -1
print(solve(N, M, a))