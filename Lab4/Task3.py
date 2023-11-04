class Shop:
    name = ''
    ___list_of_animals = []
    def add_animal_to_list(self):
        choice = input("Это птица? 1 - Да\n")

        if choice == '1':
            new_animal = Bird()

        else:
            new_animal = Fish()

        self.___list_of_animals.append(new_animal)

    def get_list_of_animals(self):
        return self.___list_of_animals


    def __init__(self):
        name = input("Введите название магазина: ")
        self.name = name

    def find_the_most_expensive(self):

        the_max = 0

        current = self.___list_of_animals[0]
        for i in self.___list_of_animals:
            if i.price > current.price:
                the_max = i
            current = i

        if the_max != 0:
            return the_max
        else:
            return self.___list_of_animals[0]


class Animal:
    price = 0
    breed = ''
    def __init__(self):
        self.breed = input("Введите породу: ")
        self.price = float(input("Введите цену: "))

    def type_of_movement(self):
        return


class Fish(Animal):
    def type_of_movement(self):
        return "Плывет"

class Bird(Animal):
    def type_of_movement(self):
        return "Летит"

shop = Shop()

while True:
    choice = input("\nВыберите действие:\n1)Добавить животное.\n2)Просмотреть список животных.\n3)Самая дорогая порода.\n4)Выход из программы.\n")
    if choice == '1':
        shop.add_animal_to_list()

    elif choice == '2':
        animals_list = shop.get_list_of_animals()
        for i in animals_list:
            print(f"Порода: {i.breed}\nЦена: {i.price}\nВид передвижения: {i.type_of_movement()}\n")

    elif choice == '3':
        animal = shop.find_the_most_expensive()
        print(animal.breed, animal.price)

    elif choice == '4':
        choice = input("Желаете сохранить данные текстовый файл? 1 - Да, 2 - Нет ")
        if choice == '1':
            with open("Lab3.txt", 'w') as f:
                f.write(f'Название магазина: {shop.name}\n')
                ls = shop.get_list_of_animals()
                f.write("Порода|Цена:\n")

                for i in ls:
                    zapis = ''
                    f.write(zapis.join(f"{i.breed}|{i.price} "))

            print("Данные записаны успешно!\n")

        print("Спасибо за использование!!")
        break

    else:
        print("Неверный ввод")