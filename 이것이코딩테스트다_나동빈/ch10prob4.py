# 커리큘럼
N = 5
works_str = [
    '10 -1',
    '10 1 -1',
    '4 1 -1',
    '4 3 1 -1',
    '3 3 -1'
]
# 10 20 14 18 17

from collections import deque

graph = [ [] for _ in range(N + 1) ]
costs = [0] * (N + 1)
indegree = [0] * (N + 1)
prev_works = [ set() for _ in range(N + 1) ]

for work in range(1, N + 1):
    work_data = list(map(int, works_str[work - 1].split()))
    costs[work] = work_data[0]

    for prev in work_data[1:-1]:    # 슬라이싱으로 마지막 원소를 제외하는 방법
        graph[prev].append(work)
    indegree[work] = len(work_data) - 2

q = deque()
for work in range(1, len(indegree)):
    if indegree[work] == 0:
        q.append(work)


# work마다 모든 이전 work를 set에 저장 한 뒤 cost를 마지막에 계산하는 내 풀이
while q:
    work = q.pop()

    for next_work in graph[work]:
        prev_works[next_work].add(work)
        prev_works[next_work].update(prev_works[work])
        indegree[next_work] -= 1
        if indegree[next_work] == 0:
            q.append(next_work)

#total_costs = [c for c in costs]
from copy import deepcopy
total_costs = deepcopy(costs)       # total_costs = costs 라고 하면 오브젝트 복사가 되어서 동일한 자료에 대해 변수 이름만 두개가 된다!

for work in range(1, N + 1):
    for prev_work in prev_works[work]:
        total_costs[work] += costs[prev_work]

print(total_costs[1:])




# 책풀이
from copy import deepcopy
total_costs = deepcopy(costs)

while q:
    work = q.pop()

    for next_work in graph[work]:
        indegree[next_work] -= 1
        total_costs[next_work] = max(total_costs[next_work], total_costs[work] + costs[next_work])      # 잠깐 이게 맞나??
        if indegree[next_work] == 0:
            q.append(next_work)


for work in range(1, N + 1):
    for prev_work in prev_works[work]:
        total_costs[work] += costs[prev_work]

print(total_costs[1:])