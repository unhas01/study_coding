li_l = list(input())
li_r = []
N = int(input())

for i in range(N):
    command = input().split()

    if command[0] == 'L' and li_l:
        li_r.append(li_l.pop())
    elif command[0] == 'D' and li_r:
        li_l.append(li_r.pop())
    elif command[0] == 'B' and li_l:
        li_l.pop()
    elif command[0] == 'P':
        li_l.append(command[1])

print(''.join(li_l + list(reversed(li_r))))