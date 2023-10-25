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
        pass

    if isinstance(element,tuple):
        min_val = min(element)
        max_val = max(element)
        print(f'минимальный/максимальный эллемент кортежа = {min_val}/{max_val}')


    if isinstance(element,int):
        arr_off_numbers = list(str(int(element)))
        result = 0
        for i in arr_off_numbers:
            num = int(i)
            if num % 2 == 0:
                result += num
        if result == 0:
             return "Сумма четных цифр равна = " + 0
        return result

    if isinstance(element,str):
        print(" ".join([str(ord(i)) for i in str(element)]))