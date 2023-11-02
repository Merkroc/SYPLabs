with open("Task2.txt", 'a') as f:
    new_str = '1'
    print("Введите фамилию и оклад сотрудника через пробел.")
    while True:
        new_str = input()
        if new_str == '':
            break
        f.write(new_str+'\n')

f = open("Task2.txt")
lines = f.readlines()
lines = [i.split() for i in lines]

print("Сотрудники с окладом более 2 тысяч:")
for k in lines:
    if float(k[1]) >= 2:
        print(f'{str(k[0])} {str(k[1])}')

print("\nСотрудники с окладом менее 2 тысяч:")
for k in lines:
    if float(k[1]) < 2:
        print(f'{str(k[0])} {str(k[1])}')

        