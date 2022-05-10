# MAX = 1000000

# dp = [1] * (MAX + 1)
# s = [0] * (MAX + 1)

# for i in range(2, MAX + 1):
#     j = 1
#     while i*j <= MAX:
#         dp[i*j] += i
#         j += 1

# for i in range(1, MAX + 1):
#     s[i] = s[i - 1] + dp[i]

# T = int(input())
# res = []

# for i in range(T):
#     n = int(input())
#     res.append(s[n])

# print('\n'.join(map(str, res)) + '\n')
# 시간초과

# pypy3로 제출
import sys
ans = [0]*10000001
tc = int(sys.stdin.readline())
for i in range(1, 1000001):
    for j in range(i, 1000001, i):
        ans[j] += i
    ans[i] += ans[i-1]
for _ in range(tc):
    sys.stdout.write("{}\n".format(ans[int(sys.stdin.readline())]))