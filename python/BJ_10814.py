import sys

n = int(sys.stdin.readline())
li = []

for i in range(n):
    a, b= map(str, sys.stdin.readline().split())
    a = int(a)
    li.append((a, b))

li.sort(key=lambda x:x[0])

for i in li:
    print(*i)