from itertools import permutations

N, M = map(int, input().split())

li = list(i for i in range(1, N+1) )

# permutations : 중복제외한 순열 
temp = list(permutations(li, M))
for i in temp:
    for j in range(M):
        print(i[j], end= ' ')

    print()
    