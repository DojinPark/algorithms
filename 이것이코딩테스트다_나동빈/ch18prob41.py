N, M = 5, 4
data = [
    '0 1 0 1 1',
    '1 0 1 1 0',
    '0 1 0 0 0',
    '1 1 0 0 0',
    '1 0 0 0 0'
]
course = [2, 3, 4, 3]

globe = []
for line in data:
    line = list( map(int, line.split()) )
    globe.append(line)
course = [c - 1 for c in course]

success = True
x = course[0]
for nx in course[1:]:
    if not globe[x][nx]:
        success = False
        break

if success: print('YES')
else: print('NO')