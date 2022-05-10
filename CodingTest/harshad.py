def solution(x):
    sum = 0
    answer = True
    for i in str(x):
        sum += int(i)
        
    if x % sum == 0:
        return True
    else:
        return False