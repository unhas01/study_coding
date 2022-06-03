N = int(input())

dp = [[0] * 10 for i in range(N + 1)]

for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, N + 1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i - 1][1]
        elif j == 9:
            dp[i][j] = dp[i - 1][8]
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]

print(sum(dp[N]) % 1000000000)

# 앞 숫자 = 0 
# -> dp[자리수 - 1][1]

# 앞 숫자 = 1 ~ 8
# -> 자리수 - 1의 앞 뒤 숫자

# 앞 숫자 = 9
# -> 자리수 - 1[8]