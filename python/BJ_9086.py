T = int(input())
li = []

for i in range(T):
    s = input()
    if len(s) < 2:
        t = s[0]*2
        li.append(t)
    else:
        t = s[0] + s[-1]
        li.append(t)

for i in li:
    print(i)
