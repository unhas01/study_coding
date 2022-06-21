n = int(input())
li = list(map(int, input().split()))
li.sort()
x = int(input())

res = 0
left = 0
right = len(li)-1

while left != right:
    temp = li[left] + li[right]
    if temp == x:
        res += 1
        right -= 1
    else:
        if temp < x:
            left += 1
        else:
            right -= 1

print(res)
