from collections import deque

def BFS():
    day = 0
    
    while queue:
        day += 1
        
        for i in range(len(queue)):
            x, y = queue.popleft() 
            
            for i in range(4):
                nx = x + dx[i] 
                ny = y + dy[i] 

                if -1 < nx < N and -1 < ny < M:
                    if graph[nx][ny] == 0:
                        graph[nx][ny] = 1
                        queue.append((nx, ny))

    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] == 0:
                return -1

    return day - 1

M, N = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]

queue = deque([])

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for i in range(len(graph)):
    for j in range(len(graph[i])):
        if graph[i][j] == 1:
            queue.append((i, j))

print(BFS())