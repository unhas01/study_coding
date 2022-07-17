n, m = map(int, input().split())
li = list(map(int, input().split()))

for i in range(n-1):
    li[i+1] += li[i]

li = [0] + li

for i in range(m):
    a, b = map(int, input().split())

    print(li[b] - li[a-1])