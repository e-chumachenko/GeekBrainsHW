class Warehouse:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height


class OfficeEquipment:
    def __init__(self, e_type, model, price):
        self.e_type = e_type
        self.model = model
        self.price = price


class Printer(OfficeEquipment):

    def __init__(self, e_type, model, price, black_ink_cartridge, clr_ink_cartridge):
        OfficeEquipment.__init__(self, e_type, model, price)
        self.black_ink_cartridge = black_ink_cartridge
        self.clr_ink_cartridge = clr_ink_cartridge


class Scanner(OfficeEquipment):

    def __init__(self, e_type, model, price, formats, automation):
        OfficeEquipment.__init__(self, e_type, model, price)
        self.formats = formats
        self.automation = automation


class Copier(OfficeEquipment):

    def __init__(self, e_type, model, price, black_ink_cartridge, clr_ink_cartridge, automation):
        OfficeEquipment.__init__(self, e_type, model, price)
        self.black_ink_cartridge = black_ink_cartridge
        self.clr_ink_cartridge = clr_ink_cartridge
        self.automation = automation
