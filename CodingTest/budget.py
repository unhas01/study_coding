def solution(d, budget):
    answer = 0
    t = budget
    arr = d
    arr.sort()
    for i in range(len(arr)):
        t -= arr[i]
        if t < 0:
            break
        answer += 1
    return answer