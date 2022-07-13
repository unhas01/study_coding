import sys
from itertools import combinations

while True:
    s = list(map(int, input().split()))

    if s[0] == 0:
        exit(0)
    
    del s[0]

    temp = list(combinations(s, 6))

    for i in temp:
        for j in i:
            print(j, end =' ')
        print()

    print()