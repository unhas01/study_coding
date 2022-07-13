import sys
from itertools import combinations

n, s = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

res = 0

for i in range(1, n+1):
    temp = list(combinations(arr, i))
    for j in temp:
        if sum(j) == s:
            res += 1

print(res)