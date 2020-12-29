# 서로소 집합을 이용한 트리 표현

V, E = 6, 4
parent_str = [
    '1 4',
    '2 3',
    '2 4',
    '5 6'
]
# 각 원소가 속한 집합:  1 1 1 1 5 5
# 부모 테이블:          1 1 2 1 5 5

# worst case: O(V)  --> 비효율적이다 > 이후 등작하는 개선된 find_parent 참조
def find_parent(parent, x):
    if parent[x] == x:
        return x
    return find_parent(parent, parent[x])

# 두 노드 각각의 루트 노드를 찾은 뒤, 두 루트 노드간 부모 관계를 "a < b 이면 a 가 부모" 이라는 규칙에 따라 정한다.
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 자기 자신을 부모로 초기화
parent = [i for i in range(V+1)]

# 입력받은 부모 관계를 적용
# 이후에도 자기 자신이 부모인 노드는 루트 노드이다.
for i in range(E):
    a, b = map(int, parent_str[i].split())
    union_parent(parent, a, b)

print('서로소 집합 알고리즘 1')
print('각 원소가 속한 집합')
for i in range(1, V + 1):
    print(i, end=' ')
print()
for i in range(1, V + 1):
    print(find_parent(parent, i), end=' ')
print()

print('부모 테이블')
for i in range(1, V + 1):
    print(i, end=' ')
print()
for i in range(1, V + 1):
    print(parent[i], end=' ')
print()




# "경로 압축 기법"을 적용한 find_parent 함수
#
# 참고: 직계 부모 노드가 아닌 루트 노드를 찾는 함수임
# 원리: 재귀 함수 호출의 끝에서 찾은 루트 노드를 반환받아 부모 리스트에 저장한다. 부모 리스트의 모든 엔트리는 루트 노드만을 저장하게 된다.
def find_parent(parent, x):
    # if parent[x] == x:                            # NoneType 이 반환되는 경우가 발생한다. parent[x] != x 일때 반환값이 없기 때문!
    #     return parent[x]                          # 파이썬 함수 작성시 NoneType 이 반횐되는 경우 모든 케이스에 대하여 반환값을 지정해두었는지 확인하자.
    # parent[x] = find_parent(parent, parent[x])
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

parent = [i for i in range(V+1)]


for i in range(E):
    a, b = map(int, parent_str[i].split())
    union_parent(parent, a, b)

print('\n서로소 집합 알고리즘 2')
print('각 원소가 속한 집합')
for i in range(1, V + 1):
    print(i, end=' ')
print()
for i in range(1, V + 1):
    print(find_parent(parent, i), end=' ')
print()

print('부모 테이블')
for i in range(1, V + 1):
    print(i, end=' ')
print()
for i in range(1, V + 1):
    print(parent[i], end=' ')
print()







# 서로소 집합 알고리즘을 이용한 사이클 판별
# 원리: 두 노드를 새롭게 연결 할 때 마다 두 노드의 루트 노드(find_parent 함수 리턴값)를 확인하는데, 같으면 사이클이 존재하는 것이다.
# ! 무향성 간선 그래프에만 사용 가능
V, E = 3, 3
parent_str = [
    '1 2',
    '1 3',
    '2 3'
]

parent = [i for i in range(V+1)]

print('\n사이클 검출 알고리즘')
for i in range(E):
    a, b = map(int, parent_str[i].split())

    # parent 리스트에 서로소 집합을 표현하는 방식으로는
    # 말단 노드간의 연결 관계는 입력을 통해서만 알 수 있다.
    # 따라서 입력을 받는 동시에 사이클을 검출해야함.
    if find_parent(parent, a) == find_parent(parent, b):
        print('Detected a cycle containing node', a, 'and', b) 
    union_parent(parent, a, b)