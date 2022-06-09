def solution(answers):
    answer = []
    
    a1 = [1, 2, 3, 4, 5]
    a2 = [2, 1, 2, 3, 2, 4, 2, 5]
    a3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    r1, r2, r3 = 0, 0, 0

    for i in range(len(answers)):
        t1 = i % 5
        t2 = i % 8
        t3 = i % 10

        if a1[t1] == answers[i]:
            r1 += 1
        if a2[t2] == answers[i]:
            r2 += 1
        if a3[t3] == answers[i]:
            r3 += 1
    
    res = max(r1, r2, r3)
    if res == r1:
        answer.append(1)
    if res == r2:
        answer.append(2)
    if res == r3:
        answer.append(3)

    return answer


a = [1,2,3,4,5]
b = [1,3,2,4,2]

print(solution(a))
print(solution(b))