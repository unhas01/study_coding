li1 = [0] * 26
li2 = [0] * 26

s1 = input()
s2 = input()

for i in s1:
    li1[ord(i) - 97] += 1

for i in s2:
    li2[ord(i) - 97] += 1

res = 0

for i in range(26):
    res += abs(li1[i] - li2[i])

print(res)