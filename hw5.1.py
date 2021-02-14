my_file = open('my_text.txt', 'a')
while True:
    user_content = input('¬ведите, пожалуйста, данные - ')
    if user_content != '':
        print(user_content, file=my_file)
    else:
        my_file.write('\n')  # при каждом последующем запуске программы новый блок данных будет отделен пустой строкой
        break
my_file.close()
