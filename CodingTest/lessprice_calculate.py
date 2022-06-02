def solution(price, money, count):
    answer = -1

    sum = 0
    for i in range(1, count + 1):
        sum += i * price
    
    if money < sum:
        answer = sum - money
    else:
        answer = 0

    return answer