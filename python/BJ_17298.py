n = int(input())
nums = list(map(int, input().split()))
stack = []

ans = [-1 for _ in range(n)]

for i in range(len(nums)):
    while stack and nums[stack[-1]] < nums[i]:
        ans[stack.pop()] = nums[i]
    stack.append(i)
print(*ans)
