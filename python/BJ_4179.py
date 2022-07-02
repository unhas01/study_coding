from collections import deque

R, C = map(int, input().split())

graph = [list(map(str, input())) for _ in range(R)]

F = []         # 불
J = None       # 지훈
res = 0
dx = [1,0,-1,0]
dy = [0,1,0,-1]

for i in range(R):
    for j in range(C):
        if graph[i][j] == 'F':  F.append((i,j))
        if graph[i][j] == 'J':  J = (i, j)

q = deque([J])
q_fire = deque(F)

b = False

while q:
    res += 1

    for i in range(len(q_fire)):
        x, y = q_fire.popleft()

        for j in range(4):
            ny = y + dy[j]
            nx = x + dx[j]

            if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] != '#' and graph[nx][ny] != 'F':
                graph[nx][ny] = 'F'
                q_fire.append((nx, ny))

    for i in range(len(q)):
        x, y = q.popleft()

        for j in range(4):
            ny = y + dy[j]
            nx = x + dx[j]

            if 0 <= nx < R and 0 <= ny < C:
                if graph[nx][ny] == '.':
                    graph[nx][ny] = 'J'
                    q.append((nx, ny))
            else:
                b = True
                break

        if b: break
    if b: break

    if len(q) == 0:
        res = 'IMPOSSIBLE'
        break

print(res)