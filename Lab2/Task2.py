# def convert_to_tuple(value):
#     if value[0] != '(' and value[-1] != ')':
#         print('value in not tuple')
#         return
#     try:
#         t = tuple(value[1:-1].replace(" ", "").split(","))
#         min_val = min(t)
#         max_val = max(t)
#
#         print(f'min/max val of t => {min_val}/{max_val}')
#         print(f'value is a tuple, result => {t}')
#     except:
#         print('invalid input tuple')
#
#
# def convert_to_array(value):
#     if value[0] != '[' and value[-1] != ']':
#         print("value is not array")
#         return
#     try:
#         a = eval(value)
#         print(f'value is a array, result => {a}')
#
#     except:
#         print('invalid input array')
#
#
# def convert_to_int(value):
#     try:
#         arr_off_numbers = list(str(int(value)))
#         result = 0
#         for i in arr_off_numbers:
#             num = int(i)
#             if num % 2 == 0:
#                 result += num
#         if result == 0:
#             return '0'
#         return result
#
#     except:
#         print('value in not int')
#         return None
#
#
# if __name__ == '__main__':
#     val = input()
#     convert_to_tuple(val)
#     convert_to_array(val)
#     is_int = convert_to_int(val)
#     if is_int:
#         print(f'value is a number, result => {is_int}')
#
def make_for_type(element):
    if isinstance(element,list):
        if 0 in element:
            index_of_first_null = element.index(0)
            index_of_second_null = 0
            amount = 0
            sum = 0
            for i, e in enumerate(element):
                if e == 0:
                    amount += 1

                if amount == 2:
                    index_of_second_null = i
                    break

            if amount == 1:
                print("Ноль только один")
                return

            for i in element[index_of_first_null:index_of_second_null]:
                sum += i
            print(f'Сумма элементов между первым и вторым нулем = {sum}')

        else:
            print("Нулей нет")


    if isinstance(element,tuple):
        min_val = min(element)
        max_val = max(element)
        print(f'Старый кортеж: {element}')
        print(f'минимальный/максимальный эллемент кортежа = {min_val}/{max_val}')

        element_list = list(element)
        element_list[element.index(min_val)] = max_val
        element_list[element.index(max_val)] = min_val
        element = tuple(element_list)
        print(f'Новый кортеж: {element}')

    if isinstance(element,int):
        arr_off_numbers = list(str(int(element)))
        result = 0
        for i in arr_off_numbers:
            num = int(i)
            if num % 2 == 0:
                result += num
        if result == 0:
            print("Сумма четных цифр равна = 0")
            return
        print(result)

    if isinstance(element,str):
        print(f'Ваша строка: {element}')
        print(" ".join([str(ord(i)) for i in str(element)]))


choice = int(input("Выберите тип данных, с которым хотите работать:\n1.Список.\n2.Кортеж.\n3.Число.\n4.Строка.\n"))
match choice:
    case 1:
        make_for_type([1, 0, 4, 3, 0, 7])
    case 2:
        make_for_type((21, 10, -5, 12, 51))
    case 3:
        make_for_type(int(5132566))
    case 4:
        make_for_type("Love is")