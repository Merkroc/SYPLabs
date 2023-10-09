number = int(input("Введите число:"))
print("Делители числа ",number)
for i in range(1,number):
    if(number%i==0):
        print(i)