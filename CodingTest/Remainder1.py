def solution(n):
    answer = 1e9
    for i in range(1, n+1):
        if n % i == 1:
            answer = min(answer, i)
    return answer