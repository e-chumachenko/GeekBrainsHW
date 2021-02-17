class Stationery:
    title = 'Канцелярская принадлежность'

    def __init__(self, color):
        self.color = color

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    item_title = 'Ручка'

    def draw(self):
        print(f'Я пишу, мой цевт {self.color}')


class Pencil(Stationery):
    item_title = 'Карандаш'

    def draw(self):
        print(f'Я черчу, мой цевт {self.color}')


class Handle(Stationery):
    item_title = 'Маркер'

    def draw(self):
        print(f'Я подчёркиваю, мой цевт {self.color}')


blue_pen = Pen('синий')
print(blue_pen.title, ' - ', blue_pen.item_title)
blue_pen.draw()

green_pencil = Pencil('зелёный')
print(green_pencil.title, ' - ', green_pencil.item_title)
green_pencil.draw()

yellow_handle = Handle('жёлтый')
print(yellow_handle.title, ' - ', yellow_handle.item_title)
yellow_handle.draw()
