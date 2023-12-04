with open("F1.txt", 'w') as f1:
    new_str = '1'
    while new_str != '':
        new_str = input()
        f1.write(new_str+'\n')

with open("F2.txt", 'w') as f2:
    f1 = open("F1.txt")
    str_f1 = f1.readlines()
    f1.close()
    for i in str_f1:
        alpha = True
        for k in i:
            if k.isdigit():
                alpha = False
                break
        if alpha:
            f2.write(i)