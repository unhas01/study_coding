def solution(s):
    answer = ''
    t = s.split(' ')
    for i in t:
        for j in range(len(i)):
            if j % 2 == 0:
                answer += i[j].upper()
            else:
                answer += i[j].lower()
        answer+= ' '
    return answer[0:-1]

s = "try hello world"	
print(solution(s))