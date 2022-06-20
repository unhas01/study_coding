A, B = map(int, input().split())

n1 = min(A, B)
n2 = max(A, B)

cnt = n2 - n1 - 1

if n2 - n1 <= 1:
    cnt = 0

li = [i for i in range(n1 + 1, n2)]
print(cnt)
print(' '.join(map(str, li)))