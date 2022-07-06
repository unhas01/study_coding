from collections import deque

M, N, K = map(int, input().split())

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

graph = [list([0] * N) for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = -1

resultList = []
for i in range(M):
    for j in range(N):
        if graph[i][j] == 0:
            count = 1
            queue = deque([])
            queue.append([i, j])
            graph[i][j] = count

            while queue:
                y, x = queue.popleft()
                for k in range(4):
                    ny = y + dy[k]
                    nx = x + dx[k]

                    if 0 <= nx < N and 0 <= ny < M and graph[ny][nx] == 0:
                        graph[ny][nx] = 1
                        queue.append([ny, nx])
                        count += 1

            resultList.append(count)

print(len(resultList))
resultList.sort()
for num in resultList:
    print(num,end=" ") 