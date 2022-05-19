from itertools import combinations_with_replacement

N, M = map(int, input().split())
num = list(map(int, input().split()))
num.sort()

temp = list(combinations_with_replacement(num, M))

for i in temp:
    for j in range(M):
        print(i[j], end=' ')
    print()