stroka = input("Введите строку: ")

if(len(stroka) > 0):
    stroka = stroka.split(' ')

    odd = [i for i in stroka if int(i) % 2 == 0]

    if(len(odd)>0):
        print("Максимальное четное число ", max(odd))

    else:
        print("Первый элемент ", stroka[0])

    stroka.sort(reverse=True)

    print(stroka)
else:
    print("Вы ничего не вве")
#l.sort(reverse=True)