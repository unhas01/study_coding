from collections import deque

N = int(input())

graph =[list(map(str, input())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]
cnt1,cnt2 = 0, 0
q = deque()

def bfs(a, b):
    q.append((a,b))
    visited[a][b] = 1 # 방문체크

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            if visited[nx][ny] == 1 or graph[x][y] != graph[nx][ny]:    # 방문 했거나 (x,y)값과 상하좌우(nx,ny)값이 다른 경우 pass
                continue

            visited[nx][ny] = 1
            q.append((nx, ny))
        

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j)
            cnt1 += 1

visited = [[0] * N for _ in range(N)]   # 다시 초기화

for i in range(N):                  # 색약인 경우 초록 == 빨강
    for j in range(N):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'


for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j)
            cnt2 += 1


print(cnt1, cnt2)
