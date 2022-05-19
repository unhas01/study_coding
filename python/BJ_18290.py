def dfs(x,y,d,s):
    global ans

    if d == K:
        ans = max(ans, s)
        return
    else:
        for i in range(x, N):
            for j in range(y if i == x else 0, M):
                if[i, j] not in q:
                    if ([i + 1, j] not in q) and ([i - 1, j] not in q) and ([i, j + 1] not in q) and ([i, j - 1] not in q):
                        q.append([i, j])
                        dfs(i, j, d + 1, s + a[i][j])
                        q.pop()


N, M, K = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(N)]
# 리스트 q : visit 체크용 리스트
q = []
ans = -1e10
dfs(0,0,0,0)
print(ans)