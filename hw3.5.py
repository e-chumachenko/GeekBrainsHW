def user_sum(user_str):
    user_l = user_str.split()
    user_num = []
    for i in user_l:
        user_num.append(int(i))
    return sum(user_num)


u_str = input('Введите, пожалуйста, строку чисел, разделенных пробелом, чтобы завершить нижмите "q" - ')
current_sum = 0
while True:
    if 'q' not in u_str:
        current_sum = current_sum + user_sum(u_str)
        print(current_sum)
        u_str = input('Введите, пожалуйста, строку чисел, разделенных пробелом, чтобы завершить нижмите "q" - ')
    elif u_str == 'q':
        break
    else:
        user_sl = u_str.split()
        user_snum = []
        for i in user_sl:
            if i != 'q':
                user_snum.append(int(i))
            else:
                print(current_sum + sum(user_snum))
        break
