def solution(n, arr1, arr2):
    answer = [] 

    for i in range(n):
        temp = bin(arr1[i] | arr2[i])    # bit 연산 (or)
        temp = temp[2:].zfill(n)
        temp = temp.replace('1', '#').replace('0', ' ')
        answer.append(temp)

    return answer

n = 6
ar1 = [46, 33, 33 ,22, 31, 50]
ar2 = [27 ,56, 19, 14, 14, 10]
print(solution(n, ar1, ar2))
