class ComplexNumber:
    def __init__(self, num_real, num_img):
        self.num_real = num_real
        self.num_img = num_img

    def __add__(self, other):
        return complex(self.num_real, self.num_img) + complex(other.num_real, other.num_img)

    def __mul__(self, other):
        return complex(self.num_real, self.num_img) * complex(other.num_real, other.num_img)


a = ComplexNumber(1, 3)
b = ComplexNumber(2, 5)

print(a + b)
print(a * b)
