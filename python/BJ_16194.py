N = int(input())
li = [0] + list(map(int, input().split()))

dp = [99999999 for i in range(1001)]
dp[0] = 0

for i in range(1, N+1):
    for j in range(1, N+1):
        dp[i] = min(dp[i], dp[i - j] + li[j])


print(dp[N])