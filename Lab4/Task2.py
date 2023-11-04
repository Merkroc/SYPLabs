class Employee:
    full_name = ''
    experience = 0.0
    salary_per_hour = 0.0
    total_hours = 0
    salary = 0.0
    extra_payment = 0.0
    def __init__(self):
        self.full_name = input("Введите ФИО сотрудника: ")
        self.experience = float(input("Введите стаж сотрудника: "))
        self.salary_per_hour = float(input("Введите ставку за час: "))
        self.total_hours = int(input("Введите количество часов, которое отработал сотрудник: "))

    def calculate_salary(self):
        self.salary = self.salary_per_hour * self.total_hours
        return self.salary

    def calculate_extra_payment(self):
        exp = self.experience
        if exp < 1:
            self.extra_payment = self.salary * 0.01
        elif exp < 3:
            self.extra_payment = self.salary * 0.05
        elif exp < 5:
            self.extra_payment = self.salary * 0.08
        else:
            self.extra_payment = self.salary * 0.15
        return self.extra_payment


    def show_information(self):
        print(f'ФИО: {self.full_name} \nОпыт работы: {self.experience} \nЧасовая ставка: {self.salary_per_hour} \nКоличество часов: {self.total_hours} \nОклад: {self.calculate_salary()} \nПремия: {self.calculate_extra_payment()}\n')

list_of_Emploees = []

amount = int(input("Введите количество рабочих, которых хотите добавить"))
for i in range(amount):
    a = Employee()
    list_of_Emploees.append(a)

for i in list_of_Emploees:
    i.show_information()
    print('\n')

