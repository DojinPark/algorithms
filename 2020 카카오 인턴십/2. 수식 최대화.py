# https://programmers.co.kr/learn/courses/30/lessons/67257
# 2. 수식 최대화
# 정확도 63.3 걸린 시간: 1:00
# 정확도 100 걸린 시간: 1:45
#
# 노트: expression 길이가 100 밖에 안된다.
#       절대절대절대 짱구 굴려서 배경 지식 끌고 오는 일 없도록!
#       파이썬의 기본 기능에 집중해서 풀수록 오류 없이 빠르게 풀 수 있다.
#       파이썬 del, permutations 등 시간 복잡도가 큰 기능도 적극 활용!!!!

import re
from itertools import permutations

def solution(expression):
    answer = 0

    for orders in permutations( ['+', '-', '*'] ):
    # for orders in [['*','+','-']]:
        nums = list( re.split(r'\D+', expression) )
        ops = [c for c in re.split(r'\d+', expression) if c != '']

        for order in orders:
            i = 0
            # print(nums)
            # print(ops)
            while True:
                if i == len(ops): break
                if ops[i] == order:
                    nums[i] = str( eval(nums[i] + ops[i] + nums[i+1]) )
                    del nums[i+1]
                    del ops[i]
                else:
                    i += 1
        # print(nums)
        # print(ops)
        
        answer = max(answer, abs(int(nums[0])))

    return answer

expression = "100-200*300-500+20"
print( solution(expression) )
# 60420

expression = "50*6-3*2"
print( solution(expression) )
# 300

expression = "2-990-5+2+32"
print( solution(expression) )

# import re
# from itertools import permutations

# def op_to_int(op):
#     if op == '+':
#         return 0
#     elif op == '-':
#         return 1
#     elif op == '*':
#         return 2

# def order(p, op):
#     return p[ op_to_int(op) ]

# def preprocess(expression, num_in, op_in):
#     num_in += list( re.split(r'\D+', expression) )
#     op_in += list( [op for op in re.split(r'\d+', expression) if op != ''] )

# def eval_same_priority(p, nums, ops):
#     if not ops: return

#     start = len(ops) - 1
#     o = order(p, ops[start])
#     for start in range( len(ops) - 1, -1, -1 ):
#         if order(p, ops[start - 1]) != o: break

#     exp = ''
#     for i in range(start, len(ops)):
#         exp += nums[i] + ops[i]
#     exp += nums[i + 1]
    
#     for i in range(start, len(ops)):
#         ops.pop()
#         nums.pop()
#     nums.pop()

#     nums.append( str( eval(exp) ) )

#     return True

# def get_result(p, num_in, op_in):
#     nums = []
#     ops = []

#     nums.append( num_in[0] )
#     nums.append( num_in[1] )
#     ops.append( op_in[0] )
#     for i in range( 1, len(op_in) ):
#         # print(nums)
#         # print(ops)
#         if order(p, ops[-1]) > order(p, op_in[i]):
#             eval_same_priority(p, nums, ops)
#         nums.append( num_in[i+1] )
#         ops.append( op_in[i] )
    
#     while ops:
#         # print(nums)
#         # print(ops)
#         eval_same_priority(p, nums, ops)
#     # print(nums)
#     # print(ops)

#     result = abs( int(nums[0]) )
#     return result

# def solution(expression):
#     answer = 0

#     num_in = []
#     op_in = []
    
#     preprocess(expression, num_in, op_in)
#     # print(num_in)
#     # print(op_in)
#     # print()

#     for p in permutations( [3, 2, 1] ):
#         print(p)
#         print(get_result(p, num_in, op_in))
#         answer = max(answer, get_result(p, num_in, op_in) )

#     return answer



