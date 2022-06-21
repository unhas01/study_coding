N = int(input())

for i in range(N):
    before, after = map(str, input().split())
    
    before = sorted(before)
    after = sorted(after)

    if before == after:
        print("Possible")
    else:
        print("Impossible")