import sys

n = int(sys.stdin.readline())

li = []
cnt = 1
res = ''
b = True

for i in range(n):
    number = int(sys.stdin.readline())

    while cnt <= number:
        li.append(cnt)
        cnt += 1
        res += '+\n'

    if li[-1] != number:
        b = False

    li.pop()
    res += '-\n'

if b == False:
    print('NO')
else:
    print(res)