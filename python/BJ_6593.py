import sys
from collections import deque

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

def bfs():
    queue = deque()
    queue.append((sz, sy, sx))

    while queue:
        z, y, x = queue.popleft()

        if x == ex and y == ey and z == ez:
            return "Escaped in {0} minute(s).".format(visited[z][y][x])

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nx < c and 0 <= ny < r and 0 <= nz < l and visited[nz][ny][nx] == 0:
                if graph[nz][ny][nx] == "." or graph[nz][ny][nx] == "E":
                    visited[nz][ny][nx] = visited[z][y][x] + 1
                    queue.append((nz, ny, nx))

    return "Trapped!"

while True:
    l, r, c = map(int, sys.stdin.readline().split())

    if l == 0 and r == 0 and c == 0:
        break

    graph = [[] * r for _ in range(l)]
    visited = [[[0 for _ in range(c)] for _ in range(r)] for _ in range(l)]

    for i in range(l):
        for _ in range(r):
            graph[i].append(list(map(str, sys.stdin.readline().strip())))
        sys.stdin.readline()

    for i in range(l):
        for j in range(r):
            for k in range(c):
                if graph[i][j][k] == "S":
                    sx, sy, sz = k, j, i
                elif graph[i][j][k] == "E":
                    ex, ey, ez = k, j, i

    print(bfs())