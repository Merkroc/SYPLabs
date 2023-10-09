stroka = input("Введите строку: ")
words = stroka.split(' ')

count = len([i for i in words if len(i) % 2 == 0])

l = list(map(lambda x: len(x), words))

print("Количество слов, имеющих четную длину: ",count)

print("Самое длинное слово: ", words[l.index(max(l))])

