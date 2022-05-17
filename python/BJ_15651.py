from itertools import product

N, M = map(int, input().split())

li = list(i for i in range(1, N+1))

# product : 중복 순열 구하는 함수 repeat!! 중요
temp = list(product(li, repeat = M))

for i in temp:
    for j in range(M):
        print(i[j], end= ' ')
    print()