from itertools import combinations

L, C = map(int, input().split())
li = list(map(str, input().split()))
li.sort()

temp = list(combinations(li, L))

for i in temp:
    cnt = 0

    for j in i:
        if j in 'aeiou':
            cnt += 1

    if cnt >= 1 and L - cnt >= 2:
        print(''.join(i))
