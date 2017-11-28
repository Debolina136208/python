def fibonacci(val):
    num1 = 0
    num2 = 1
    count = 0
    while (count < val):
        print(num1, end=',')
        sum = num1 + num2
        num1 = num2
        num2 = sum
        count += 1


fibonacci(20)

