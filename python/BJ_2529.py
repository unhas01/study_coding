from itertools import permutations
from random import randrange

k = int(input())
sign = input().split()

result = []

for i in permutations([0,1,2,3,4,5,6,7,8,9], k+1):
    flag = True
    for j in range(len(sign)):
        if sign[j] == '<':
            if i[j] < i[j+1]: continue
            else:
                flag = False
                break
        else:
            if i[j] > i[j+1]: continue
            else:
                flag = False
                break
    if flag:
        result.append(i)

print(''.join(map(str,list(max(result)))))
print(''.join(map(str,list(min(result)))))