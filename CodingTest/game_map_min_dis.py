from collections import deque

def solution(maps):
    answer = 0

    dx = [1,0,-1,0]
    dy = [0,1,0,-1]

    len_x = len(maps)
    len_y = len(maps[0])

    q = deque()
    q.append((0, 0))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < len_x and 0 <= ny < len_y and maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                q.append((nx, ny))

    if maps[len_x-1] [len_y-1] == 1:
        answer = -1
    else:
        answer = maps[len_x-1] [len_y-1]
    print(maps)
    return answer

m1 = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
m2 = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]

print(solution(m1))
print(solution(m2))
