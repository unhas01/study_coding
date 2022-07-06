from collections import deque

N = int(input())

graph = [list(map(int, input())) for _ in range(N)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]
res = []

def bfs(a, b):
    q = deque()
    q.append((a, b))
    graph[a][b] = 0
    cnt = 1

    while q:
        x, y = q.popleft()
        graph[x][y] = 0

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx, ny))
                cnt += 1

    return cnt

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            count = bfs(i, j)
            res.append(count)


res.sort()
print(len(res))
for i in res:
    print(i)
