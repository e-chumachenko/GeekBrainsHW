class Matrix:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        # поиск числа, состоящего из наибольшего количества символов, для определения отступа столбцов матрицы
        len_num = len(str(self.data[0][0]))
        for row in self.data:
            for el in row:
                if len(str(el)) > len_num:
                    len_num = len(str(el))
        step = '{:' + str(len_num + 3) + 'd}'
        for row in self.data:
            for el in row:
                print(step.format(el), end='')
            print()
        return ''

    def __add__(self, other):
        new_data = []
        for i in range(len(self.data)):
            new_data.append([x + y for x, y in zip(self.data[i], other.data[i])])
        return Matrix(new_data)


a = Matrix([[1, 1, 1], [-2, -2, -2], [5, 5, 5]])
b = Matrix([[3, 3, 3], [4, 4, 4], [6, 6, 6]])

print(a)
print(b)
print(a + b)

# # Вариант с вводом матриц пользователем
#
#
# def str_to_matrix(user_data):
#     user_data_rows = user_data.split('_')
#     user_matrix = []
#     for data_row in user_data_rows:
#         user_matrix.append([int(j) for j in data_row.split()])
#     return user_matrix
#
#
# user_data_1 = input('Введите, пожалуйста, данные для матрицы 1 - числа в строке через пробел, строки через "_" - ')
# # Например, 1 1 1_2 2 2_3 3 3
# user_data_2 = input('Введите, пожалуйста, данные для матрицы 2 - числа в строке через пробел, строки через "_" - ')
#
# c = Matrix(str_to_matrix(user_data_1))
# d = Matrix(str_to_matrix(user_data_2))
# print(c)
# print(d)
# print(c + d)
