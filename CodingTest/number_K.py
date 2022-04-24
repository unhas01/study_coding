def solution(array, commands):
    answer = []

    for li in commands:
        temp = array[li[0]-1:li[1]]
        temp.sort()
        answer.append(temp[li[2]-1])
    return answer

# a = [1, 5, 2, 6, 3, 7, 4]

# li = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

# print(solution(a,li))
