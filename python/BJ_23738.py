s = input()

if 'B' in s:
    s = s.replace('B', 'v')

if 'E' in s:
    s = s.replace('E', 'ye')

if 'H' in s:
    s = s.replace('H', 'n')

if 'P' in s:
    s = s.replace('P', 'r')

if 'C' in s:
    s = s.replace('C', 's')

if 'Y' in s:
    s = s.replace('Y', 'u') 

if 'X' in s:
    s = s.replace('X', 'h')

print(s.casefold())