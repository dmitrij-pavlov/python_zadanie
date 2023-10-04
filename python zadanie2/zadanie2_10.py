num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
operation = input("Введите операцию (+, -,  или /): ")
if operation in ['+', '-', '', '/']:
    if operation == '/' and num2 == 0:
        result = "888888"
    else:
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            result = num1 / num2
else:
    result = "888888"
    
print(result)
