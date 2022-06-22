T = int(input())

for i in range(T):
    L = input()

    left = []
    right = []
    for j in L:
        if j == '<':
            if left:
                right.append(left.pop())
        elif j == '>':
            if right:
                left.append(right.pop())
        elif j == '-':
            if left:
                left.pop()
        else:
            left.append(j)

    print(''.join(left + list(reversed(right))))