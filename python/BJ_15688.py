import sys
n = int(sys.stdin.readline())
tmp = []

for i in range(n):
    tmp.append(int(sys.stdin.readline()))

for i in sorted(tmp):
    print(i)