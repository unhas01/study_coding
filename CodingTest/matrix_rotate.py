def solution(rows, columns, queries):
    answer = []

    x = columns
    y = rows

    # 2차원 행렬 초기화
    matrix = []            
    num = 0     
    for i in range(y):
        t = []
        for j in range(x):
            num += 1
            t.append(num)
        matrix.append(t)
    
    # 회전
    for j in queries:
        x1, y1, x2, y2 = j[0]-1, j[1]-1, j[2]-1, j[3]-1

        temp = matrix[x1][y1]
        min_num = temp

        for i in range(x1, x2): # 왼쪽
            a = matrix[i+1][y1]
            matrix[i][y1] = a
            min_num = min(min_num, a)
        
        for i in range(y1, y2): # 아래쪽
            a = matrix[x2][i+1]
            matrix[x2][i] = a
            min_num = min(min_num, a)

        for i in range(x2, x1, -1): # 오른쪽
            a = matrix[i-1][y2]
            matrix[i][y2] = a
            min_num = min(min_num, a)
        
        for i in range(y2, y1, -1): # 위쪽
            a = matrix[x1][i-1]
            matrix[x1][i] = a
            min_num = min(min_num, a)
        
        matrix[x1][y1+1] = temp

        answer.append(min_num)

    return answer

q1 = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
q2 = [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]
q3 = [[1,1,100,97]]

print(solution(6,6,q1))
print(solution(3,3,q2))
print(solution(100,97,q3))
