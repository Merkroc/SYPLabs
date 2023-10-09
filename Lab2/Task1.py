def calculation(arg):
    numbers = []
    for i in range(0, 1001):
        if (i%arg==0):
            numbers.append(i)
    return numbers

print("Введите число:")
arg = int(input())
print("Числа, которые делятся на", arg)
print(calculation(arg))
