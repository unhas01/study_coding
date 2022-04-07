T = int(input())

def c2017(n):
    if n == 1:
        return 5000000
    elif n > 1 and n < 4:
        return 3000000
    elif n >= 4 and n < 7:
        return 2000000
    elif n >= 7 and n < 11:
        return 500000
    elif n >= 11 and n < 16:
        return 300000
    elif n >= 16 and n < 22:
        return 100000
    else:
        return 0

def c2018(n):
    if n == 1:
        return 5120000
    elif n > 1 and n < 4:
        return 2560000
    elif n >= 4 and n < 8:
        return 1280000
    elif n >= 8 and n < 16:
        return 640000
    elif n >= 16 and n < 32:
        return 320000
    else:
        return 0

for i in range(T):
    a, b = map(int, input().split())
    print(c2017(a) + c2018(b))