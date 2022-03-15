class DivisionByZero:
    def __init__(self, devidend, divisor):
        self.devidend = devidend
        self.divisor = divisor

    @staticmethod
    def division(devidend, divisor):
        try:
            return (devidend / divisor)
        except:
            return (f"Деление на ноль недопустимо")

ex = DivisionByZero(3, 0)
print(ex.division(3, 0))
