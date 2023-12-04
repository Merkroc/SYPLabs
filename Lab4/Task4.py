class Person:
    people_amount = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people_amount += 1

    def introduce(self):
        print(f"Ку, меня {self.name} звать, мне вот уже {self.age} стукнуло.")

    @staticmethod
    def get_people_amount():
        return Person.people_amount

    @classmethod
    def create_person(cls, name, age):
        return cls(name, age)

person1 = Person("Антоха", 25)
person2 = Person("Колян", 30)

person1.introduce()
person2.introduce()

people_amount = Person.get_people_amount()
print(f"Количество людей: {people_amount}")

person3 = Person.create_person("Пахан", 22)
person3.introduce()

people_amount = Person.get_people_amount()
print(f"Количество людей: {people_amount}")