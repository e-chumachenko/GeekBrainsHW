a = float(input('Результат в первый день в км - '))
b = float(input('Желаемый резултат в км - '))
days = 1
while a < b:
    a = 1.1 * a
    days = days + 1
print('Номер дня -', days)
