from collections import deque

T = int(input())

dx = [-1, 1, 2, 2, 1, -1, -2, -2]
dy = [2, 2, 1, -1, -2, -2, -1, 1]

def bfs(a, b):
    q = deque()
    q.append((a,b))

    while q:
        x, y = q.popleft()  

        if x == ga and y == gb:
            return graph[x][y] - 1

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx < n and 0 <= ny < n and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))


for i in range(T):
    n = int(input())
    graph = [[0] * n for _ in range(n)]
    
    pa, pb = map(int, input().split())
    ga, gb = map(int, input().split())

    graph[pa][pb] = 1

    print(bfs(pa, pb))
