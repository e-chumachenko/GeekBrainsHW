# список задан в программе

my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
generator_list = (el for el in my_list)
new_list = [i for i in my_list[1:] if i > next(generator_list)]
print(new_list)

# список задает пользователь

my_str = input('Введите, пожалуйста, несколько чисел, разделенных пробелом - ')
my_list = [int(el) for el in my_str.split()]
generator_list = (el for el in my_list)
new_list = [i for i in my_list[1:] if i > next(generator_list)]
print(my_list)
print(new_list)