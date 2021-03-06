def solution(s):
    answer = -1

    stack = []
    
    for i in s:
        if not stack:
            stack.append(i)
        elif stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
            
    if not stack: 
        answer = 1
    else:
        answer = 0

    return answer