# Создай класс Calculator с методом add, который принимает 
# два числа и возвращает их сумму. Затем создай объект
# и вызови метод с разными параметрами.

# Доп. задача:

# 1. Написать еще 3 метода, вычитание, деление и умножение
# 2. Создать второй объект
# 3. Вызвать все методы для первого и второго объекта

class Calculator:
    def __init__(self, a, b):
        self.first = a
        self.second = b

    def add(self):
        self.s = self.first + self.second
        print("Сумма равна:", self.s)

    def umno(self):
        self.s = self.first * self.second
        print("Умножение:", self.s)

    def smth(self):
        self.s = self.first - self.second
        print("Вычитание:", self.s)

    def smth2(self):
        self.s = self.first / self.second
        print("Деление:", self.s)

obj1 = Calculator(10, 5)
obj1.add()
obj1.umno()
obj1.smth()
obj1.smth2()

obj2 = Calculator(20, 15)
obj2.add()
obj2.umno()
obj2.smth()
obj2.smth2()
