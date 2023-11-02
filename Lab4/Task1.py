class Example:
    number1 = 1
    number2 = 9

    def add_atribute(self):
        self.x = "Новая переменная"
        print(self.x)

    def sum_of_global(self):
        return self.number1 + self.number2

    def one_in_second(self, din1, din2):
        self.din1 = din1
        self.din2 = din2
        return pow(self.din1, self.din2)

obj = Example()
print(obj.sum_of_global())
print(obj.one_in_second(2, 3))
print(obj)