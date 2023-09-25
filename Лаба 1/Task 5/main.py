continue_work = True
the_dict = {
    "Дорого-богато": ["Серьги", "Золото", 150, 10], "Кольца власти": ["Кольцо", "Золото", 140, 20], "Кулон": ["Подвеска", "Серебро", 80, 22], "Серебрянка": ["Серьги", "Серебро", 60, 50], "Кольцо судьбы": ["Кольцо", "Серебро", 40, 80]}

def view_all(the_dict):
    for k, v in the_dict.items():
        print(f"{k}\nТип: {v[0]}\nМатериал: {v[1]}\nСтоимость: {v[2]}\nКоличество: {v[3]}\n")

def buyProduct(product_name, amount):

    if product_name in the_dict:

        price = the_dict[product_name][2]

        quantity = the_dict[product_name][3]

        if amount <= quantity:

            total_price = price * amount

            the_dict[product_name][2] -= amount

            print(f"Покупка успешно совершена. Вы купили {amount} шт. {product_name} за {total_price} руб.")

        else:
            print(f"Извините, в магазине нет столько {product_name}.")

    else:
        print("Извините, товар не найден.")

while (continue_work == True):
    choice = int(input("1. Просмотр описания: название – описание \n2. Просмотр цены: название – цена. \n3. Просмотр количества: название – количество. \n4. Всю информацию. \n5. Покупка \nЛюбое другое значение. Выход\n"))

    if (choice == 1):
        view_all(the_dict)

    elif (choice == 2):
        for k, v in the_dict.items():
            print(f"{k}\nСтоимость: {v[2]}\n")

    elif (choice == 3):
        for k, v in the_dict.items():
            print(f"{k}\nКоличество: {v[3]}\n")

    elif (choice == 4):
        view_all(the_dict)

    elif (choice == 5):
        name = input("Введите название: ")
        amount = int(input("Введите количество: "))
        buyProduct(name, amount)

    else:
        continue_work = False

print("Спасибо за использование")