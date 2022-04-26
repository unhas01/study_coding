s = list(input())

a = "CAMBRIDGE"

for i in a:
    for j in range(len(s)):
        if i == s[j]:
            s[j] = ''

for i in s:
    print(i, end='')