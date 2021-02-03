# https://programmers.co.kr/learn/courses/30/lessons/17681
# 비밀지도
# 정답률: 81.78% (난이도: 하)
# 걸린시간: 0:20

def __to_bin_arr(n, dec):
    bins = []
    for _ in range(n):
        bins.append( dec % 2 )
        dec //= 2
    return bins[::-1]

def build_mat(arr):
    n = len(arr)
    ret = []

    for num in arr:
        ret.append( __to_bin_arr(n, num) )
    return ret

def combine_mat(mat1, mat2):
    n = len(mat1)
    ret = [ [0] * n for _ in range(n) ]
    for i in range(n):
        for j in range(n):
            ret[i][j] = mat1[i][j] or mat2[i][j]
    return ret

def mat_to_str(mat):
    ret = []
    for row in mat:
        line = ''
        for bit in row:
            if bit:
                line += '#'
            else:
                line += ' '
        ret.append(line)
    return ret

def solution(n, arr1, arr2):
    answer = []

    mat1 = build_mat(arr1)
    mat2 = build_mat(arr2)

    mat = combine_mat(mat1, mat2)

    answer = mat_to_str(mat)

    return answer


n =	5
arr1 =	[9, 20, 28, 18, 11]
arr2 =	[30, 1, 21, 17, 28]
print( solution(n, arr1, arr2) )

n =	6
arr1 =	[46, 33, 33 ,22, 31, 50]
arr2 =	[27 ,56, 19, 14, 14, 10]
print( solution(n, arr1, arr2) )