with open('1234.txt') as my_file, open('1234_rus.txt', 'w', encoding='utf-8') as rus_file:
    for line in my_file.readlines():
        if line.split()[0] == 'One':
            print(f'Один {line.split()[1]} {line.split()[2]}', file=rus_file)
        elif line.split()[0] == 'Two':
            print(f'Два {line.split()[1]} {line.split()[2]}', file=rus_file)
        elif line.split()[0] == 'Three':
            print(f'Три {line.split()[1]} {line.split()[2]}', file=rus_file)
        else:
            print(f'Четыре {line.split()[1]} {line.split()[2]}', file=rus_file)
