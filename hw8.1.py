class Date:
    def __init__(self, str_date):
        self.str_date = str_date

    @classmethod
    def to_int(cls, str_date):
        dd = int(str_date.split('-')[0])
        mm = int(str_date.split('-')[1])
        yyyy = int(str_date.split('-')[2])
        return dd, mm, yyyy

    @staticmethod
    def validation(str_date):
        d, m, y = Date.to_int(str_date)
        if m in [1, 3, 5, 7, 8, 10, 12]:
            if d < 1 or d > 31:
                print('Число должно быть в интервале от 1 до 31\nМесяц введен корректно')
            else:
                print('Число введено корректно\nМесяц введен корректно')
        elif m in [4, 6, 9, 11]:
            if d < 1 or d > 30:
                print('Число должно быть в интервале от 1 до 30\nМесяц введен корректно')
            else:
                print('Число введено корректно\nМесяц введен корректно')
        elif m == 2:
            if d < 1 or d > 29:
                print('Число должно быть в интервале от 1 до 29\nМесяц введен корректно')
            else:
                print('Число введено корректно\nМесяц введен корректно')
        else:
            print('Месяц должен быть в интервале от 1 до 12')
        if y < 1970 or y > 2021:
            print('Год должен быть в интервале от 1970 до 2021')
        else:
            print('Год введен корректно')


Date.validation('15-01-2019')
