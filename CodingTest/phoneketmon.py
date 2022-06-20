def solution(nums):
    answer = 0
    pick = len(nums) / 2
    nums = list(set(nums))

    if len(nums) >= pick:
        answer = pick
    elif len(nums) < pick:
        answer = len(nums)
        
    return int(answer)

n = [3,1,2,3]
print(solution(n))