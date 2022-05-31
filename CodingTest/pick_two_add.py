from itertools import combinations

def solution(numbers):
    answer = []
    temp = list(combinations(numbers, 2))

    for i in temp:
        answer.append(sum(i))

    t = set(answer)
    res = list(t)
    res.sort()

    return res
