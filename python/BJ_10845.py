from sys import stdin

N = int(stdin.readline())

li = []

for i in range(N):
    command = stdin.readline().split()

    if 'push' in command[0]:
        li.append(int(command[1]))
    elif command[0] == 'pop':
        if len(li) == 0:    print(-1)
        else:               print(li.pop(0))
    elif command[0] == 'size': 
        print(len(li))
    elif command[0] == 'empty':
        if len(li) == 0:    print(1)
        else:               print(0)
    elif command[0] == 'front':
        if len(li) == 0:    print(-1)
        else:               print(li[0])
    elif command[0] == 'back':
        if len(li) == 0:    print(-1)
        else:               print(li[len(li) - 1])