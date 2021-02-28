class OnlyNumbers(Exception):
    def __init__(self, txt):
        self.txt = txt


user_list = []

while True:
    user_data = input('Введите, пожалуйста, число - ')
    if user_data != 'stop':
        try:
            if user_data.isdigit():
                user_list.append(int(user_data))
                print(user_list)
            elif user_data.startswith('-') and '.' not in user_data and user_data[1:].isdigit():
                user_list.append(int(user_data))
                print(user_list)
            elif '.' in user_data and len(user_data.split('.')) == 2 and user_data.split('.')[0].isdigit() and \
                    user_data.split('.')[1].isdigit():
                user_list.append(float(user_data))
                print(user_list)
            elif '.' in user_data and len(user_data.split('.')) == 2 and user_data.split('.')[0].startswith('-') \
                    and user_data.split('.')[0][1:].isdigit() and user_data.split('.')[1].isdigit():
                user_list.append(float(user_data))
                print(user_list)
            else:
                raise OnlyNumbers('Можно вводить только числа')
        except OnlyNumbers as msg:
            print(msg)
    else:
        print(user_list)
        break
