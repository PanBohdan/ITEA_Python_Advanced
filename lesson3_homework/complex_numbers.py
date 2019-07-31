class Complex:
    def __init__(self, real, imaginary):
        self._real = real
        self._imag = imaginary

    def get_real(self):
        return self._real

    def get_imag(self):
        return self._imag

    def __add__(self, other):
        try:
            a = self._real + other.get_real()
            b = self._imag + other.get_imag()
            return Complex(a, b)
        except AttributeError:
            raise Exception('cannot add a number to a complex number')

    def __sub__(self, other):
        try:
            a = self._real - other.get_real()
            b = self._imag - other.get_imag()
            return Complex(a, b)
        except AttributeError:
            raise Exception('cannot subtract a number from a complex number')

    def __mul__(self, other):
        try:
            a = self._real*other.get_real()-self._imag*other.get_imag()
            b = self._real*other.get_imag()+self._imag*other.get_real()
            return Complex(a, b)
        except AttributeError:
            raise Exception('cannot multiply a number by an complex number')

    def __truediv__(self, other):
        try:
            first_part = self._real * other.get_real() + self._imag * other.get_imag()
            second_part = self._imag * other.get_real() - self._real * other.get_imag()
            sum_of_other_squared = other.get_real()**2 + other.get_imag()**2
            real = first_part / sum_of_other_squared
            imag = second_part / sum_of_other_squared
            return Complex(real, imag)
        except AttributeError:
            raise Exception('cannot divide a number by an complex number')

    def get_num(self):
        if self._imag >= 0:
            operator = '+'
        else:
            operator = ''
        return f"{self._real}{operator}{self._imag}i"


comp_a = Complex(1, 2)
comp_b = Complex(3, 4)

print((comp_a+comp_b).get_num())
print((comp_a-comp_b).get_num())
print((comp_a*comp_b).get_num())
print((comp_a/comp_b).get_num())
