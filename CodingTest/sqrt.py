import math

def solution(n):
    answer = 0
    t = math.sqrt(n)
    if t % 1 == 0:
        answer = (t + 1) ** 2
    else:
        answer = -1
    return answer