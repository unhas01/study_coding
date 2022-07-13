import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

arr.sort()
temp = list(combinations(arr, m))
temp = sorted(list(set(temp)))

for i in temp:
    for j in range(m):
        print(i[j], end= ' ')

    print()