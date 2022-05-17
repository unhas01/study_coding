from itertools import combinations

N, M = map(int, input().split())

li = list(i for i in range(1, N+1))

# combinations : 중복 제외 순서 상관없는 조합
temp = list(combinations(li, M))

for i in temp:
    for j in range(M):
        print(i[j], end= ' ')
    print()