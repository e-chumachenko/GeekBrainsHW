class Car:
    car_count = 0

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        Car.car_count += 1

    def go(self):
        print('Машина поехала\n')

    def stop(self):
        print('Машина остановилась\n')

    def turn(self, direction):
        print(f'Машина повернула {direction}\n')

    def show_speed(self, current_speed):
        print(f'Скорость в данный момент - {current_speed} км/ч')


class TownCar(Car):
    def show_speed(self, current_speed):
        print(f'Скорость в данный момент - {current_speed} км/ч')
        if current_speed > 60:
            print('Превышение скорости!')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police, price):
        super().__init__(speed, color, name, is_police)
        self.price = price


class WorkCar(Car):
    def show_speed(self, current_speed):
        print(f'Скорость в данный момент - {current_speed} км/ч')
        if current_speed > 40:
            print('Превышение скорости!')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police, policemen, is_siren_on):
        super().__init__(speed, color, name, is_police)
        self.policemen = policemen
        self.is_siren_on = is_siren_on


hyundai = TownCar(180, 'красный', 'Hyundai Solaris', False)
print(f'{hyundai.name} - цвет {hyundai.color}, максимальная скорость {hyundai.speed} км/ч')
hyundai.show_speed(70)
hyundai.go()

lamborghini = SportCar(325, 'жёлтый', 'Lamborghini Huracan', False, 270000)
print(f'{lamborghini.name} - цвет {lamborghini.color}, максимальная скорость {lamborghini.speed} км/ч, '
      f'цена {lamborghini.price}$')
lamborghini.show_speed(110)
lamborghini.turn('налево')

volkswagen = WorkCar(145, 'зелёный', 'Volkswagen Transporter', False)
print(f'{volkswagen.name} - цвет {volkswagen.color}, максимальная скорость {volkswagen.speed} км/ч')
volkswagen.show_speed(35)
volkswagen.stop()

ford_police = PoliceCar(185, 'синий', 'Ford Focus', True, 2, True)
print(f'{ford_police.name} - цвет {ford_police.color}, максимальная скорость {ford_police.speed} км/ч')
if ford_police.is_police:
    print('Это полицейская машина')
print(f'Количество полицейских в машине - {ford_police.policemen}')
if ford_police.is_siren_on:
    print('Сирена включена!')
ford_police.show_speed(130)
ford_police.turn('направо')

print(f'Создано машин - {Car.car_count}')
