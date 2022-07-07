from collections import deque

f, s, g, u, d = map(int, input().split())

dp = [0] * (f+1)

def bfs(start):
    q = deque()
    q.append(start)

    while q:
        now = q.popleft()

        if now == g:
            return dp[now]
        
        for i in (now + u, now - d):
            if 0 < i <= f and dp[i] == 0 and i != start:
                dp[i] = dp[now] + 1
                q.append(i)

    return "use the stairs"

print(bfs(s))