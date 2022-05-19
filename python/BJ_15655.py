from itertools import combinations

N, M = map(int, input().split())
num = list(map(int, input().split()))
num.sort()

temp = list(combinations(num, M))

for i in temp:
    for j in range(M):
        print(i[j], end=' ')

    print()