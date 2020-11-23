# 떡볶이 떡 만들기
#
# 조건에 맞는 최적값 찾기 "파라메트릭 서치" 문제
# 파라메트릭 서치 문제는 보통 이진 탐색을 사용하는 유형으로 출제됨

N, M = 4, 6
a = [19, 15, 10, 17]
# 15

answer = 0
low, high = min(a), max(a)

while True:
    if high < low:
        break

    mid = (low + high) // 2
    m = 0
    for v in a:
        m += max(v - mid, 0)

    # 기본 이진 탐색코드와는 달리 조금 더 생각해서 코딩해야하는 부분
    # 책 내용의 "떡의 양 m 이 목표량 M 보다 부족한 경우, 더 많이 자르기(high 를 더 작게 탐색)"와 같이 직관적으로 생각하면 대소관계를 막힘없이 구현할 수 있다.
    if m < M:
        high = mid - 1
    elif m >= M:
        low = mid + 1
        answer = mid

print(answer)