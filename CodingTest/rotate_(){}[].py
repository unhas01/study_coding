def solution(s):
    answer = 0
    
    for i in range(len(s)):
        t = s[i:] + s[:i]       # 회전
        
        stack = []
        dic = {"]": "[", ")": "(", "}": "{"}
        b = True

        for i in t:
            if i in ('(', '{', '['):
                stack.append(i)
            else:
                if len(stack) == 0:
                    b = False
                    break
                if dic[i] == stack[-1]:
                    stack.pop()
                else:
                    b = False
                    break
        
        if stack:
            b = False
        
        if b == True:
            answer += 1

    return answer

s1 = "[](){}"
s2 = "}]()[{"
s3 = "[)(]"
s4 = "}}}"

print(solution(s1))
print(solution(s2))
print(solution(s3))
print(solution(s4))