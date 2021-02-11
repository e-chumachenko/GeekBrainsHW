# список задан в программе

my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list = [i for i in my_list if my_list.count(i) == 1]
print(new_list)

# список задает пользователь

my_str = input('Введите, пожалуйста, несколько чисел, разделенных пробелом - ')
my_list = [int(el) for el in my_str.split()]
print(my_list)
new_list = [i for i in my_list if my_list.count(i) == 1]
print(new_list)

