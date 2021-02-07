def division(dividend, divisor):
    return dividend / divisor


try:
    user_dividend = float(input('Введите, пожалуйста, делимое - '))
    user_divisor = float(input('Введите, пожалуйста, делитель - '))
    if user_divisor == 0:
        result = 'Ошибка - деление на 0'
    else:
        result = division(user_dividend, user_divisor)
except ValueError:
    result = 'Введенные данные не являются числом'
print('Результат - ', result)
