
NOT_FOUND = -1

N = 0
# Binrary Search 응용
# 내 풀이가 틀린 점: 모든 수가 서로 다르다는 전제와 상관 없는 코드임
# 중복된 수가 있는 경우 중간점중 하나를 출력할수는 있음
# 서로 다른 수만 주어지는 경우 시간 복잡도가 logN 이상임
def solution(a, l, r):
    global N
    if l > r: return NOT_FOUND

    m = (l + r) // 2

    if a[m] == m: return m

    if m < a[m]:
        ret = solution(a, l, m - 1)
        if ret == NOT_FOUND:
            ret = solution(a, a[m] + 1, r)

    elif a[m] < m:
        ret = solution(a, m + 1, r)
        if ret == NOT_FOUND:
            ret = solution(a, l, a[m] - 1)
    
    return ret

def solution_text_book(a, l, r):
    global N
    if l > r: return NOT_FOUND

    m = (l + r) // 2

    if a[m] == m: return m

    if m < a[m]:
        return solution(a, l, m - 1)

    elif a[m] < m:
        return solution(a, m + 1, r)


N = 5
a = [-15, -6, 1, 3, 7]
print( solution(a, 0, len(a)-1) )
print( solution_text_book(a, 0, len(a) - 1) )
# 3

N = 7
a = [-15, -4, 2, 8, 9, 13, 15]
print( solution(a, 0, len(a)-1) )
print( solution_text_book(a, 0, len(a) - 1) )
# 2

N = 7
a = [-15, -4, 3, 8, 9, 13, 15]
print( solution(a, 0, len(a)-1) )
print( solution_text_book(a, 0, len(a) - 1) )
# -1