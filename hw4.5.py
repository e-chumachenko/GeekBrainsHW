from functools import reduce


def func_mlt(a, b):
    return a * b


num_list = [i for i in range(100, 1001) if i % 2 == 0]
print(reduce(func_mlt, num_list))