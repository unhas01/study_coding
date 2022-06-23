import sys

N = int(sys.stdin.readline())

building = []

for i in range(N):
    building.append(int(sys.stdin.readline()))

res = 0
stack = []

for i in range(N):
    while stack and stack[-1] <= building[i]:
        stack.pop()
    
    stack.append(building[i])
    res += len(stack) - 1

print(res)