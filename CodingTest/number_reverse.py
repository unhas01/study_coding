def solution(n):
    temp = list(str(n))
    temp.reverse()

    return list(map(int, temp))