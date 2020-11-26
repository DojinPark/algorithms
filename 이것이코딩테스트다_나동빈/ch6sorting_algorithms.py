a = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
print(a)

def selection_sort(a):
    a = list(a) # iterable 인자를 reference로 사용하지 않고 복사하여 사용하는 방법
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
    return a

print( selection_sort(a) )

def insertion_sort(a):
    a = list(a)
    for i in range(1, len(a)):
        j = i-1
        while a[j] > a[j+1] and j >= 0:
            a[j], a[j+1] = a[j+1], a[j]
            j -= 1
    return a

print( insertion_sort(a) )

def _quick_sort(a, s, e):
    if s >= e: return
    p = s
    l = s+1
    r = e
    pivot = a[p]

    while l <= r:
        while l <= e and a[l] <= pivot:
            l += 1
        while r > s and a[r] >= pivot:
            r -= 1
        if l > r:
            a[r], a[p] = a[p], a[r]
        else:
            a[l], a[r] = a[r], a[l]

    _quick_sort(a, s, r-1)
    _quick_sort(a, l, e)
def quick_sort(a):
    a = list(a)
    _quick_sort(a, 0, len(a)-1)
    return a

print( quick_sort(a) )

def quick_sort_py(a):
    if len(a) <= 1: return a
    pivot = a[0]
    l = [x for x in a[1:] if x <= pivot]
    r = [x for x in a[1:] if x > pivot]
    return quick_sort_py(l) + [pivot] + quick_sort_py(r)

print( quick_sort_py(a) )

def count_sort(a):
    a = list(a)
    N = len(a)
    K = max(a)

    cnt = [0] * (K+1)
    for i in range(N):
        cnt[a[i]] += 1
    
    i = 0
    for k in range(K+1):
        for _ in range(cnt[k]):
            a[i] = k
            i += 1
    
    return a

print( count_sort(a) )
