from itertools import product

N, M = map(int, input().split())
num = list(map(int, input().split()))
num.sort()

temp = list(product(num, repeat=M))

for i in temp:
    for j in range(M):
        print(i[j], end=' ')

    print()