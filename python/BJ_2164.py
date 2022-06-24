import sys
from collections import deque

N = int(sys.stdin.readline())
li = [i for i in range(1, N+1)]
q = deque(li)


while len(q) > 1:
    q.popleft()
    temp = q.popleft()
    q.append(temp)
    
print(q[0])