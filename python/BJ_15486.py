import sys
input = sys.stdin.readline

N = int(input().rstrip())
T= []
P= []
dp=[0]*(N+1)

for _ in range(N):
	time, price = map(int, input().split())
	T.append(time)
	P.append(price)

max_value=0
for i in range(N):
    max_value = max(max_value, dp[i])
    if i+T[i] >N:
        continue
    dp[i+T[i]] = max(dp[i+T[i]], max_value+P[i])


#print(dp)
print(max(dp))