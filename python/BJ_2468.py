from collections import deque

N = int(input())

graph = [ list(map(int, input().split())) for _ in range(N)]

max_num = 0     # 가장 큰 높이 값 

for i in graph:
    for j in i:
        if max_num < j:
            max_num = j

dx = [1,0,-1,0]
dy = [0,1,0,-1]

res = []

def bfs(a, b, rain):
    q = deque()
    q.append((a, b))
    visited[a][b] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] > rain and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                q.append((nx, ny))

for k in range(max_num + 1):
    visited = [[0] * N for _ in range(N)]
    count = 0

    for i in range(N):
        for j in range(N):
            if graph[i][j] > k and visited[i][j] == 0:
                bfs(i,j,k)
                count += 1

    res.append(count)

print(max(res))