import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    li = list(map(int, input().split()))

    li.reverse()

    res = 0
    temp = 0

    for i in li:
        if temp > i:
            res += (temp - i)
        else:
            temp = i
    
    print(res)