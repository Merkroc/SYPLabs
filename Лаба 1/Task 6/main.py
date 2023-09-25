stroka = input("Введите последовательность чисел, разделённых запятой: ")
numbers = stroka.split(',')
num = tuple(numbers)
print("Список ",numbers,"\nКортеж ", num)