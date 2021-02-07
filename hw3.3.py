def my_func(a1, a2, a3):
    a_mn = min(a1, a2, a3)
    return a1 + a2 + a3 - a_mn


num1 = float(input('Введите, пожалуйста, первый аргумент - '))
num2 = float(input('Введите, пожалуйста, второй аргумент - '))
num3 = float(input('Введите, пожалуйста, третий аргумент - '))
print(my_func(num1, num2, num3))
