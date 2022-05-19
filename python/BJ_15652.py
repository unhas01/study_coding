from itertools import combinations_with_replacement

N, M = map(int, input().split())

li = list(i for i in range(1, N+1))

# combinations_with_replacement : 중복 조합 return 함수
temp = list(combinations_with_replacement(li, M))

for i in temp:
    for j in range(M):
        print(i[j], end= ' ')
    print()