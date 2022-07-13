import sys
from itertools import combinations_with_replacement

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

temp = list(combinations_with_replacement(arr, m))
temp = sorted(list(set(temp)))

for i in temp:
    for j in range(m):
        print(i[j], end= ' ')

    print()