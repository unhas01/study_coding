def solution(board, moves):
    answer = 0
    basket = []

    for i in range(len(moves)):
        # moves[i] = 꺼낼 곳
        # 꺼내는 반복문
        for j in range(len(board)):
            if board[j][moves[i] - 1] == 0:
                continue
            else:
                basket.append(board[j][moves[i] - 1])
                board[j][moves[i] - 1] = 0
                break

        if len(basket) >= 2 and basket[-1] == basket[-2]:
            basket.pop()
            basket.pop()
            answer+=2
                  
    return answer

a = [
[0,0,0,0,0],
[0,0,1,0,3],
[0,2,5,0,1],
[4,2,4,4,2],
[3,5,1,3,1]]
b = [1,5,3,5,1,2,1,4]
print(solution(a, b))

