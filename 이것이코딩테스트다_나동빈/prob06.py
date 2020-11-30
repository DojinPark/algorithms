# 무지의 먹방 라이브

def solve(food_times, k):
    while True:
        L = len(food_times) - food_times.count(0)
        min_t = min(food_times)
        print(food_times)
        print(k)
        if k >= L * min_t:
            sub = min_t
        else:
            sub = 1
        for i in range(len(food_times)):
            if k == 0:
                return i
            if food_times[i]:
                food_times[i] -= sub
                k -= sub

food_times = [3, 1, 2]
k = 5
# 1
solve(food_times, k)