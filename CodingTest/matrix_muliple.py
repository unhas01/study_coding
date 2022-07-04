def solution(arr1, arr2):
    answer = [[] for _ in range(len(arr1))]
    
    for i in range(len(arr1)):                  # arr1의 행
        tmp = [0] * len(arr2[0])
        for j in range(len(arr1[0])):           # arr1의  열, arr2의 행
            for k in range(len(arr2[0])):       # arr2의 열
                tmp[k] += arr1[i][j] * arr2[j][k]
        answer[i] = tmp
                
    return answer


a = [[1, 4], [3, 2], [4, 1]]
b = [[3, 3], [3, 3]]
c = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
d = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]
print(solution(a, b))
print(solution(c, d))