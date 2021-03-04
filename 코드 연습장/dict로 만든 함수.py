def calc(op, a, b):
    switcher = {
        '+': a + b,
        '-': a - b,
        '*': a * b,
        '/': a / b
    }
    return switcher[op]

print( calc('*', 123, 2) )
print( calc('/', 369, 3) )