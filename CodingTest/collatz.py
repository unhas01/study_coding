def solution(num):
    answer = 0
    temp = num

    while True: 
        if temp == 1:
            break
        if answer == 500:
            answer = -1
            break   

        if temp % 2 == 0:
            temp /= 2
            answer += 1
        else:
            temp = temp * 3 + 1
            answer += 1

    return answer
