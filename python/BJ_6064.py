T = int(input())

def f(M, N, x, y):
    while x <= M * N:
        if (x - y) % N == 0:
            return x
        x += M
    
    return -1
            

for i in range(T):
    M, N, x, y= map(int, input().split())
    print(f(M,N,x,y))