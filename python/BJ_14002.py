N = int(input())
li = list(map(int, input().split()))

dp = [1] * N

for i in range(N):
    for j in range(i):
        if li[j] < li[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))

res = []
t = max(dp)

# t에 max(dp)값을 저장하고 역순으로 돌면서 리스트에 저장하고 출력
for i in range(N - 1, -1, -1):
    if dp[i] == t:
        res.append(li[i])
        t -= 1

res.reverse()

print(*res)