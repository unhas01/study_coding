from collections import deque

T = int(input())

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs():
    while q:
        x, y = q.popleft()

        if visited[x][y] != "FIRE":
            flag = visited[x][y]
        else:
            flag = "FIRE"

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < h and 0 <= ny < w:
                if visited[nx][ny] == -1 and (graph[nx][ny] == "." or graph[nx][ny] == "@"):
                    if flag == "FIRE":
                        visited[nx][ny] = flag
                    else:
                        visited[nx][ny] = flag + 1
                    q.append((nx, ny))
            else:
                if flag != "FIRE":
                    return flag + 1
    
    return "IMPOSSIBLE"

for i in range(T):
    w, h = map(int, input().split())

    graph = [list(map(str, input())) for _ in range(h)]
    visited = [[-1] * w for _ in range(h)]

    q = deque()

    for j in range(len(graph)):
        for k in range(len(graph[j])):
            if graph[j][k] == '*':
                visited[j][k] = "FIRE"
                q.append((j, k))
            elif graph[j][k] == '@':
                visited[j][k] = 0
                start = ((j, k))
        
    q.append(start)
    print(bfs())