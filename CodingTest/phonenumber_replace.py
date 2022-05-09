def solution(phone_number):
    answer = ''
    n = len(phone_number)
    back = phone_number[-4:]
    answer = '*'*(n-4) + back
    
    return answer
