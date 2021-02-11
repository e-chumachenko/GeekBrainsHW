from math import factorial


def fact(param):
    for i in range(1, param+1):
        result_f = factorial(i)
        yield result_f


n = int(input('Веведите, пожалуйста, для какого количества чисел, начиная от 1, рассчитать факториал - '))
for el in fact(n):
    print(el)
