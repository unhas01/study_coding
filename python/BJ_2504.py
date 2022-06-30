s = input()

stack = []
res = 0
mul = 1

for i in range(len(s)):
    if s[i] == '(':
        stack.append(s[i])
        mul *= 2

    elif s[i] == '[':
        stack.append(s[i])
        mul *= 3

    elif s[i] == ')':
        if not stack or stack[-1] != '(':
            res = 0
            break

        if s[i-1] == '(':
            res += mul

        stack.pop()
        mul /= 2

    elif s[i] == ']':
        if not stack or stack[-1] != '[':
            res = 0
            break

        if s[i-1] == '[':
            res += mul

        stack.pop()
        mul /= 3

if stack:       print(0)
else:           print(int(res))