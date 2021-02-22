class Cell:
    def __init__(self, unit):
        self.unit = int(unit)

    def __add__(self, other):
        return Cell(self.unit + other.unit)

    def __sub__(self, other):
        if (self.unit - other.unit) != 0:
            return Cell(abs(self.unit - other.unit))
        else:
            return 'В клетках одинаковое количество ячеек'

    def __mul__(self, other):
        return Cell(self.unit * other.unit)

    def __truediv__(self, other):
        return Cell(self.unit // other.unit)

    def make_order(self, units_in_row):
        row = self.unit // units_in_row
        remainder = self.unit % units_in_row
        list_rows = []
        for r in range(row):
            list_rows.append(units_in_row * '*' + '/n')
        if remainder != 0:
            list_rows.append(remainder * '*')
        else:
            last_element = list_rows.pop()
            list_rows.append(last_element[0:units_in_row])
        print(''.join(list_rows))


c1 = Cell(15)
c2 = Cell(7)

(c1 + c2).make_order(5)
(c1 - c2).make_order(3)
(c1 * c2).make_order(20)
(c1 / c2).make_order(1)
