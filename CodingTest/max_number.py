def solution(numbers):
    numbers_str = [str(num) for num in numbers]               
    numbers_str.sort(key=lambda num: num*3, reverse=True)

    return str(int(''.join(numbers_str)))


num1 = [6, 10, 2]
num2 = [3, 30, 34, 5, 9]
print( solution(num1))
# permutations() 방식은 시간초과
