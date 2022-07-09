def solution(s):
    answer = ''
    li = list(map(int, s.split()))
    
    answer += str(min(li)) + ' '
    answer += str(max(li))
    
    return answer