import sys

n = int(sys.stdin.readline())
li = []

for i in range(n):
    li.append(sys.stdin.readline().strip())

set_li = set(li)
li = list(set_li)
li.sort()
li.sort(key = len)

for i in li:
    print(i)