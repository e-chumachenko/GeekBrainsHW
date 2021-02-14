with open('salary.txt', encoding='utf-8') as salary_f:
    staff = {}
    for employee in salary_f.readlines():
        employee_l = employee.split()
        l_name = employee_l[0]
        staff[l_name] = float(employee_l[1])
    for last_name, salary in staff.items():
        if salary < 20000:
            print('Зарплата менее 20000 руб. - ', last_name, salary, 'руб.')
    print('Средняя зарплата сотрудников - ', sum(staff.values())/len(staff.values()), 'руб./чел.')
