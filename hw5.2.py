my_file = open('poem.txt')
content = my_file.readlines()
print('���������� ����� - ', len(content))
for count, line in enumerate(content, 1):
    print(f'������ {count} - ���������� ���� {len(line.split())}')
my_file.close()
