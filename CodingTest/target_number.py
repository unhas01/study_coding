from collections import deque

def solution(numbers, target):
    answer = 0

    q = deque()
    n = len(numbers)
    q.append((numbers[0], 0))
    q.append((-numbers[0], 0))

    while q:
        x, idx = q.popleft()
        idx += 1

        if idx < n:
            q.append((x + numbers[idx], idx))
            q.append((x - numbers[idx], idx))
        else:
            if x == target:
                answer += 1
        
    return answer

n1 = [1, 1, 1, 1, 1]
n2 = [4, 1, 2, 1]

print(solution(n1, 3))
print(solution(n2, 4))