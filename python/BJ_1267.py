N = int(input())

phone = list(map(int, input().split()))

y, m = 0, 0

for i in range(N):
    y += ((phone[i] // 30) + 1) * 10
    m += ((phone[i] // 60) + 1) * 15

if y < m:
    print('Y', y)
elif y > m:
    print('M', m)
else:
    print('Y M', y)