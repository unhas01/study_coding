import sys

N = int(input()) 

rope = [int(sys.stdin.readline()) for i in range(N)] 

rope.sort()

result=0

for i in range(len(rope)):
    if result < N * rope[i]:
        result = N * rope[i]
        N -= 1
    else:
        N -= 1

print(result)