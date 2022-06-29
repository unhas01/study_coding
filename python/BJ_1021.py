from collections import deque
import sys

N, M = map(int, sys.stdin.readline().split())

li = list(map(int, sys.stdin.readline().split()))
d = deque([i for i in range(1, N+1)])

cnt = 0

for i in li:
    while True:
        if d[0] == i:
            d.popleft()
            break
        else:
            if d.index(i) <= len(d) // 2:
                d.rotate(-1)
                cnt += 1
            else:
                d.rotate(1)
                cnt += 1

print(cnt)