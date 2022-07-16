n = int(input())
li = []

for _ in range(n):
    a,b,c,d = list(map(str, input().split()))
    li.append([a, int(b), int(c), int(d)])

li.sort(key=lambda x : str(x[0])) 
li.sort(key=lambda x:int(x[3]), reverse = True) 
li.sort(key = lambda x : int(x[2])) 
li.sort(key = lambda x: int(x[1]), reverse = True)

for i in li:
    print(i[0])