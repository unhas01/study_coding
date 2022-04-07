N = int(input())

nums = list(map(int, input().split()))
res = []

for i in range(N):
    res.insert(i - nums[i], i+1)

for i in res:
    print(i,end=' ')
