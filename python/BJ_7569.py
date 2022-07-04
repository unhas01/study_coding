from collections import deque

m, n, h=map(int,input().split())
a=[[list(map(int,input().split())) for _ in range(n)] for _ in range(h)]

dx=[-1, 0, 1, 0, 0, 0]
dy=[0, 1, 0, -1, 0, 0]
dz=[0, 0, 0, 0, -1, 1]

def bfs():
    while q:
        z, x, y = q.popleft()
    
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h:
                if a[nz][nx][ny] == 0:
                    a[nz][nx][ny] = a[z][x][y] + 1
                    q.append([nz, nx, ny])

q= deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if a[i][j][k] == 1:
                q.append([i, j, k])

bfs()

t = 1
result = -1

for i in a:
    for j in i:
        for k in j:
            if k == 0:
                t = 0

            result=max(result,k)

if t == 0: #모두 익지 못한 상태
    print(-1)
elif result == 1: #모두 익어있던 상태 
    print(0)
else:
    print(result-1)