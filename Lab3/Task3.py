with open("Task3.txt", 'a') as f:
    new_str = '1'
    print("Введите название и количество занятий через пробел.")
    while True:
        new_str = input()
        if new_str == '':
            break
        f.write(new_str + '\n')

with open("Task3.txt", 'r') as f:
    lines = f.readlines()

lines = [i.split() for i in lines]
dictionary = {}
for i in lines:
    name = ''
    total_classes = 0
    for k in i:
        if k.isalpha():
            name = k
        else:
            total_classes += float(k)
    dictionary[name] = total_classes

for k, v in dictionary.items():
    print(k, v)