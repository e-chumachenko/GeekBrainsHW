class ZDError(Exception):
    def __init__(self, txt):
        self.txt = txt


user_data = input('Введите, пожалуйста, делимое и делитель через пробел - ')

try:
    a = float(user_data.split()[0])
    b = float(user_data.split()[1])
    if b == 0:
        raise ZDError('Делитель не должен быть равен 0')
except ValueError:
    print('Вы ввели не число')
except ZDError as error:
    print(error)
else:
    print(a / b)
