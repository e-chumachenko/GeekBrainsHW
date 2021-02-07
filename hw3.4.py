# первыйы способ


def my_func(x, y):
    return x ** y


num1 = float(input('Введите, пожалуйста, действительное положительное число - '))
num2 = int(input('Введите, пожалуйста, целое отрицательное число - '))
if num1 > 0 and num2 < 0:
    print(my_func(num1, num2))
else:
    print('Введены неверные исходные данные')

# второй способ


def my_func(x, y):
    current = x
    for i in range(y, -1):
        current = current * x
    return 1 / current


num1 = float(input('Введите, пожалуйста, действительное положительное число - '))
num2 = int(input('Введите, пожалуйста, целое отрицательное число - '))
if num1 > 0 and num2 < 0:
    print(my_func(num1, num2))
else:
    print('Введены неверные исходные данные')
