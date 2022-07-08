def change(num, n):
    numbers = '0123456789ABCDEF'
    r = ''
    if num == 0:
        return '0'
    while num > 0:
        r = numbers[num % n] + r
        num = num // n
    return r

def solution(n, t, m, p):
    tmp = ''
    answer = ''
    
    for i in range(t * m):
        tmp += change(i, n)
        
    for i in range(t):
        answer += tmp[p-1 + m*i]
        
    return answer

print(solution(2,4,2,1))
print(solution(16,16,2,1))
print(solution(16,16,2,2))