def sum_num(s):
    res = 0
    for i in s:
        if i.isdigit():
            res += int(i)
    return res

n = int(input())
li = [input() for _ in range(n)]
li.sort(key= lambda x:(len(x), sum_num(x), x))

for s in li:
    print(s)