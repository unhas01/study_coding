def solution(sizes):
    answer = 0
    big = []
    small = []

    for i in sizes:
        big.append(max(i[0], i[1]))
        small.append(min(i[0], i[1]))

    answer = max(big) * max(small)

    return answer
