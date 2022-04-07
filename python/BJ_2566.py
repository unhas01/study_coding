res = 0

for i in range(9):
    garo = list(map(int, input().split()))
    if max(garo) > res:
        res = max(garo)
        x = i + 1
        y = garo.index(res) + 1
    
print(res)
print(x, y)

