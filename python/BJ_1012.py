from collections import deque

T = int(input())

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(graph, a, b):
    q = deque()
    q.append((a, b))
    graph[a][b] = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx, ny))
    
    return

for i in range(T):
    N, M, K = map(int, input().split())

    graph = [[0] * M for _ in range(N)]

    for j in range(K):
        x, y = map(int, input().split())
        graph[x][y] = 1

    cnt = 0
    
    for j in range(N):
        for k in range(M):
            if graph[j][k] == 1:
                bfs(graph, j, k)
                cnt += 1

    print(cnt)
