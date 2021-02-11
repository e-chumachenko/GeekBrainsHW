from sys import argv

script_name, hours, hourly_rate, bonus = argv


def func_salary(h, h_r, b):
    return (h * h_r) + b


print('Salary - ', func_salary(int(hours), int(hourly_rate), int(bonus)))
