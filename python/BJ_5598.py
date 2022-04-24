s = input()
res = ''

for c in s:
    c = ord(c) - 65
    c = c - 3 + 26
    c = c % 26
    c = c + 65
    res += chr(c)

print(res)