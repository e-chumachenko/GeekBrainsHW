my_file = open('my_text.txt', 'a')
while True:
    user_content = input('�������, ����������, ������ - ')
    if user_content != '':
        print(user_content, file=my_file)
    else:
        my_file.write('\n')  # ��� ������ ����������� ������� ��������� ����� ���� ������ ����� ������� ������ �������
        break
my_file.close()
