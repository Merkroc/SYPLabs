x = input()

try:
    x = int(x)
    x = x/2
    print(x)

except ValueError:
    print(x, "не является числом")

finally:
    print("Досвидос")