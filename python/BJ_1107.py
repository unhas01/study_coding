N = int(input())
M = int(input())

if M != 0:
    broken = list(map(int, input().split()))

res = abs(100 - N)

for i in range(1000001):
    i = str(i)
    
    for j in range(len(i)):
        if int(i[j]) in broken:
            break
        elif j == len(i) - 1:
            res = min(res, abs(int(i) - N) + len(i))

print(res)
