class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'оклад': wage, 'премия': bonus}


class Position(Worker):
    def get_full_name(self):
        print(f'Сотрудницу/сотрудника зовут - {self.name} {self.surname}')

    def get_total_income(self):
        total_income = self._income['оклад'] + self._income['премия']
        print(f'Доход с учетом премии - {total_income}')


employee_1 = Position('Ольга', 'Трофимова', 'учительница', 45000, 20000)
print(employee_1.name, employee_1.surname, employee_1.position, employee_1._income)
employee_1.get_full_name()
employee_1.get_total_income()

employee_2 = Position('Дмитрий', 'Грачев', 'врач', 55000, 10000)
print(employee_2.name, employee_2.surname, employee_2.position, employee_2._income)
employee_2.get_full_name()
employee_2.get_total_income()

user_str = input('Введите, пожалуйста, имя, фамилию, должность, оклад и премию сотрудника через пробел - ')
user_data = user_str.split()

employee_3 = Position(user_data[0], user_data[1], user_data[2], int(user_data[3]), int(user_data[4]))
print(employee_3.name, employee_3.surname, employee_3.position, employee_3._income)
employee_3.get_full_name()
employee_3.get_total_income()
