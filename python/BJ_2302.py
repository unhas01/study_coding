import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
vip = [int(sys.stdin.readline()) for _ in range(m)]

dp = [0] * (n + 1)
dp[0] = 1
dp[1] = 1
dp[2] = 2 

for i in range(3, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

answer = 1 

if m > 0:
    t = 0
    for j in range(m):
        answer *= dp[vip[j] - 1 - t]
        t = vip[j]
    answer *= dp[n - t]
else:
    answer = dp[n]

print(answer)

# 1 2 3     4   5 6     7   8 9
# dp[3]  *     dp[2]    * dp[2]