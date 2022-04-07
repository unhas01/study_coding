N, K = map(int, input().split())
arr = [[0]*2 for i in range(6)]

#print(arr)

for i in range(N):
    S, Y = map(int, input().split())
    arr[Y-1][S-1] += 1

res = 0
for i in range(6):
    for j in range(2):
        if arr[i][j] % K == 0:
            res += arr[i][j] / K
        else:
            res += arr[i][j] // K +1

print(int(res))