def solution(n, h):
    answer = [[0] * n for _ in range(n)] 

    answer[0][0] = 1
    for i in range(1, n):
        answer[i][i] = answer[i-1][i-1] + i*2

    for i in range(1, n):
        up, left = answer[i][i], answer[i][i]

        if h:
            for j in range(1, n):
                if i % 2 == 0:
                    answer[i-j][i] = up + 1
                    answer[i][i-j] = left - 1
                else:
                    answer[i-j][i] = up - 1
                    answer[i][i-j] = left + 1
            
                up = answer[i-j][i]
                left = answer[i][i-j]
        else:
            for j in range(1, n):
                if i % 2 == 0:
                    answer[i-j][i] = up - 1
                    answer[i][i-j] = left + 1
                else:
                    answer[i-j][i] = up + 1
                    answer[i][i-j] = left - 1
                    
                up = answer[i-j][i]
                left = answer[i][i-j]

    return answer

print(solution(4, True))
print(solution(4, False))

# True
# 0     1   2   3   4  (i)  

# 1     2   9   10  25
# 4     3   8   11  24  
# 5     6   7   12  23
# 16    15  14  13  22  
# 17    18  19  20  21  

# False
# 1     4   5   16  17
# 2     3   6   15  18
# 9     8   7   14  19
# 10    11  12  13  20
# 25    24  23  22  21

# [1, 0, 0, 0],  00 01 02 03
# [0, 3, 0, 0],  10 11 12 13
# [0, 0, 7, 0],  20 21 22 23
# [0, 0, 0, 13]  30 31 32 33
