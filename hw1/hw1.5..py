revenue = float(input('Введите, пожалуйста, выручку фирмы - '))
costs = float(input('Введите, пожалуйста, издержки фирмы - '))
if revenue > costs:
    profitability = (revenue - costs) / revenue
    staff = int(input('Введите, пожалуйста, численность сотрудников фирмы - '))
    profit_staff = (revenue - costs) / staff
    print('Фирма получила прибыль - ', revenue - costs, 'руб.')
    print('Рентабельность выручки - ', profitability)
    print('Численность сотрудников - ', staff, 'человек/а')
    print('Прибыль фирмы в расчёте на одного сотрудника', profit_staff, 'руб./чел.')
elif revenue < costs:
    print('Фирма получила убыток - ', costs - revenue, 'руб.')
else:
    print('Доходы фирмы равны расходам')
