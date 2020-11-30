# 만들 수 없는 금액

# 수의 조합을 모두 구한 내 풀이
# O(N^2 + NlogN)
def solve(N, nums):
    results = set()

    def search(i, num = 0):
        # if i >= len(nums):
        #     return
        num += nums[i]
        results.add(num)

        for next in range(i+1, len(nums)):
            search(next, num)
    
    for i in range(len(nums)):
        search(i)

    results = list(results)
    results.sort()

    print(results)
    
    answer = 0
    for result in results:
        if result != answer + 1:
            return answer + 1
        else:
            answer += 1
    return answer

N = 5
nums = [3, 2, 1, 1, 9]
# 8
print(solve(N, nums))



# 책 풀이
# 이게 맞는건가...?
nums.sort()
target = 1
for x in nums:
    if target < x:
        break
    target += x
print(target)