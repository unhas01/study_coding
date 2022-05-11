li = []

for i in range(9):
    li.append(int(input()))

n1 = 0
n2 = 0

for i in range(9):
    for j in range(i+1, 9):
        if sum(li) - (li[i] + li[j]) == 100:
            n1 = li[i]
            n2 = li[j]

            break

li.remove(n1)
li.remove(n2)
li.sort()

for i in li:
    print(i)
