# 7-3.py 반복문으로 구현한 이진 탐색
#
# 존 벤틀리("생각하는 프로그래밍")의 말에 따르면 이진 탐색 코드를 작성한 프로그래머는 10% 내외라 할 정도로 실제 구현은 까다롭다. -> 좀 과장임
# 이진 탐색을 활용해야 시간 제한을 맞출수 있는 고난도 문제들도 있음.
# 이진 탐색 코드는 아예 외워두는게 좋음
# 쉬운 코드지만 구현해본 기억없이 시험 시간 내에 구현하는건 엄청 어렵다.
#
# 이진 탐색 트리인지 확인하는 법:
# 입력 데이터가 많거나, 탐색 범위가 매우 넓은 편이다.
# 예) 입력 데이터의 개수 천만개, 탐색 범위 천억 이상
# 물론!) 입력 데이터의 개수가 많은 경우 sys.stdin.readline().rstrip() 사용


# a는 반드시 정렬되어있는 배열이어야한다.
def binary_search(a, target, start, end):
    while True:
        # 원소 없음             
        if end < start:         # 이 조건문이 가장 앞에 있어야 하는 것 중요!
            return None

        mid = (start + end) // 2

        # 일치
        if a[mid] == target:
            return mid

        # 왼쪽 탐색
        if target < a[mid]:
            end = mid - 1       # 1을 빼줘야 하는 것 중요!
            
        # 오른쪽 탐색
        elif a[mid] < target:
            start = mid + 1     # 1을 더해줘야 하는 것 중요!!

a = [ 3, 4, 2, 6, 7, 8, 1, 0, 9, 5 ]
a.sort()

print( binary_search(a, 4, 0, len(a)-1) )
print( binary_search(a, 0, 0, len(a)-1) )
print( binary_search(a, 9, 0, len(a)-1) )
print( binary_search(a, 10, 0, len(a)-1) )



# bisect 모듈 사용하기
print("bisect test")
from bisect import bisect_left, bisect_right
a = [8, 4, 2, 4, 4, 16]
a.sort()
print('i:', [i for i in range(len(a))])
print('a:', a)
print(bisect_left(a, 5))    # "정렬 순서를 지키며 5를 삽입할 가장 왼쪽 인덱스"
print(bisect_right(a, 5))   # "정렬 순서를 지키며 5를 삽입할 가장 오른쪽 인덱스"
print(bisect_left(a, 4))
print(bisect_right(a, 4))