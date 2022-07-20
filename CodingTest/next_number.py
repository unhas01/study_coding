def solution(n):
    answer = 0

    one_count = bin(n).count("1")

    for num in range(n+1, 1000001):
        num_one_count = bin(num).count("1")

        if one_count == num_one_count:
            answer = num
            break

    return answer