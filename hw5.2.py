my_file = open('poem.txt')
content = my_file.readlines()
print('Количество строк - ', len(content))
for count, line in enumerate(content, 1):
    print(f'Строка {count} - количество слов {len(line.split())}')
my_file.close()
