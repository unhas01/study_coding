import sys

a, b, c = map(int, sys.stdin.readline().split())

def multi(a, n):
    if n == 1:
        return a % c
    else:
        tmp = multi(a, n//2)
        if n % 2 == 0:
            return (tmp * tmp) % c
        else:
            return (tmp * tmp * a) % c

print(multi(a,b))

# 10^11 % 12
# = ((10^5)%12 x (10^5)%12 x 10)% 12
# = ((10^2)%12 x (10^2)%12 x 10) %12 x (10^2)%12 x (10^2)%12 x 10) %12 x 10) %12