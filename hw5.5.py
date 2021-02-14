#  дл€ однократного ввода данных

with open('sum_file_1.txt', 'w+') as s_file:
    user_str = input('¬ведите, пожалуйста, числа, разделенные пробелами - ')
    print(user_str, file=s_file)
    s_file.seek(0)
    data = s_file.read()
    data_num = [float(num) for num in data.split()]
    print(sum(data_num))

# дл€ многократного ввода данных

with open('sum_file_m.txt', 'a+') as s_file:
    user_str = input('¬ведите, пожалуйста, числа, разделенные пробелами, чтобы завершить - пустую строку "" ')
    while True:
        if user_str != '':
            print(user_str, file=s_file)
            s_file.seek(0)
            sum_num = 0
            for line in s_file.readlines():
                num_l = [float(num) for num in line.split()]
                print(num_l)
                sum_num = sum_num + sum(num_l)
            print(sum_num)
            user_str = input('¬ведите, пожалуйста, числа, разделенные пробелами, чтобы завершить - пустую строку "" ')
        else:
            break
