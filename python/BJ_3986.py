N = int(input())
cnt = 0

for i in range(N):
    stack = []
    str = input()

    for j in str:
        if stack and stack[-1] == j:
            stack.pop()
        else:
            stack.append(j)

    if stack:
        continue
    else:
        cnt += 1

print(cnt)