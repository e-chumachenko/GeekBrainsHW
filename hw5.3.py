with open('salary.txt', encoding='utf-8') as salary_f:
    staff = {}
    for employee in salary_f.readlines():
        employee_l = employee.split()
        l_name = employee_l[0]
        staff[l_name] = float(employee_l[1])
    for last_name, salary in staff.items():
        if salary < 20000:
            print('�������� ����� 20000 ���. - ', last_name, salary, '���.')
    print('������� �������� ����������� - ', sum(staff.values())/len(staff.values()), '���./���.')
