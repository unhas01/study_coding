
li = []

for i in range(10):
    li.append(int(input()))

print(sum(li)//10)
print(max(li, key = li.count))