x = input()

t = type(x)

if t is list:
    pass

if t is tuple:
    pass

elif t is int:
    x = [int(x) for i in x]
    for i in x:
        if i % 2 == 0:
            print(i)


elif t is str:
    print(" ".join([str(ord(i)) for i in str(x)]))