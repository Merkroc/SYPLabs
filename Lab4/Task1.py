class Example:
    number1 = 1
    number2 = 9

    def __init__(self, dyn1, dyn2):
        self.dyn1 = dyn1
        self.din2 = dyn2
    def print_dynamic_var(self):
        print("Переменная:", self.dyn1)


    def sum_of_global(self):
        return self.number1 + self.number2

    def one_in_second(self):
        return pow(self.dyn1, self.dyn2)

obj = Example()
print(obj.sum_of_global())
print(obj.one_in_second(2, 3))
print(obj)