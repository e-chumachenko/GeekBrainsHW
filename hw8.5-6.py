class Department:

    def __init__(self, title, length, width, height, employee):
        self.title = title
        self.length = length
        self.width = width
        self.height = height
        self.employee = employee


class Warehouse(Department):
    wh_equipment = {'printer': 0, 'scanner': 0, 'copier': 0}

    def new_item(self):
        while True:
            # например, 'printer 4', один вид оборудования для каждой итерации
            user_data = input('Введите тип оборудования, поступившего на склад (printer или scanner или copier) и '
                              'количество через пробел, для остановки ввода данных '' - ')
            if user_data != '':
                try:
                    check = int(user_data.split()[1])
                except ValueError:
                    print('Введено некорректное значение для количества оборудования')
                    continue
                if user_data.split()[0] == 'printer':
                    self.wh_equipment['printer'] = self.wh_equipment['printer'] + int(user_data.split()[1])
                elif user_data.split()[0] == 'scanner':
                    self.wh_equipment['scanner'] = self.wh_equipment['scanner'] + int(user_data.split()[1])
                elif user_data.split()[0] == 'copier':
                    self.wh_equipment['copier'] = self.wh_equipment['copier'] + int(user_data.split()[1])
                else:
                    print('Введены некорректные данные')
            else:
                print(self.title, self.wh_equipment)
                break


class OtherDepartment(Department):
    od_equipment = {'printer': 0, 'scanner': 0, 'copier': 0}

    def transfer(self):
        user_choice = input('Введите тип (printer или scanner или copier) и количество передаваемого '
                            'со склада оборудования через пробел - ')
        if Warehouse.wh_equipment[user_choice.split()[0]] < int(user_choice.split()[1]):
            print('На складе нет такого количества оборудования')
        else:
            Warehouse.wh_equipment[user_choice.split()[0]] = Warehouse.wh_equipment[user_choice.split()[0]] - int(user_choice.split()[1])
            self.od_equipment[user_choice.split()[0]] = self.od_equipment[user_choice.split()[0]] + int(user_choice.split()[1])


warehouse = Warehouse('склад', 10, 10, 5, 3)
p_department = OtherDepartment('производство', 8, 8, 3, 7)

warehouse.new_item()
p_department.transfer()
print(warehouse.title, warehouse.wh_equipment)
print(p_department.title, p_department.od_equipment)
