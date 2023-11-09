def calculation(arg):
    numbers = []
    for i in range(1, arg+1):
        if arg % i == 0:
            numbers.append(i)
    return numbers


print("Введите число:")
arg = int(input())
print(f"{arg} делится без остатка на:")
print(calculation(arg))
