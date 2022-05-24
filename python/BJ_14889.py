from itertools import combinations

N = int(input())
arr = [i for i in range(N)]
matrix = []
for _ in range(N):
    matrix.append((list(map(int, input().split()))))
res = int(1e9)

for i in combinations(arr, N // 2):
    start, link = 0, 0
    j = list(set(arr) - set(i))
    
    for r in combinations(i, 2):
        start += matrix[r[0]][r[1]]
        start += matrix[r[1]][r[0]]
    for r in combinations(j, 2):
        link += matrix[r[0]][r[1]]
        link += matrix[r[1]][r[0]]

    res = min(res, abs(start - link))

print(res)