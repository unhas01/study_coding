from itertools import combinations 

def isPrime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    
    li = list(combinations(nums, 3))
    
    for i in li: 
        sum = i[0] + i[1] + i[2]
        if isPrime(sum):
            answer += 1

    return answer