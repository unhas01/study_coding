from itertools import permutations
import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

temp = list(permutations(arr, m))
temp = sorted(list(set(temp)))      # 중복 제거 & 정렬

for i in temp:
    for j in range(m):
        print(i[j], end= ' ')

    print()