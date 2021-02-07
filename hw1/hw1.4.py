num = int(input('Введите, пожалуйста, целое положительное число - '))
mx_num = 0
while num > 0:
    remainder = num % 10
    num = num // 10
    if remainder > mx_num:
        mx_num = remainder
    print(remainder, num, mx_num)
print('Самая большая цифра в числе - ', mx_num)
