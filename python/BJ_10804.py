li = [i for i in range(1, 21)]

for i in range(10):
    a, b = map(int, input().split())
    t = li[a - 1:b]
    t = reversed(t)
    li[a-1:b] = t

for i in li:
    print(i, end = ' ')