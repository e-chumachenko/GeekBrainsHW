time_s = int(input('Введите, пожалуйста, время в секундах - '))
hours = time_s // 3600
minutes = (time_s - 3600 * hours) // 60
seconds = time_s % 60
print('{:02}:{:02}:{:02}'.format(hours, minutes, seconds))
