import sys
from collections import deque

N, L = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
d = deque()

for i in range(N):
    while d and d[-1][1] > arr[i]:
        d.pop()

    d.append((i, arr[i]))

    while d and d[0][0] < i - L + 1:
        d.popleft()
    
    print(d[0][1], end=' ') 