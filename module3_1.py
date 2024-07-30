from random import randint

calls = 0 #Создать переменную calls = 0 вне функций.
def count_calls(): #Функция count_calls подсчитывающая вызовы остальных функций.
    global calls
    calls += 1
    return calls
def string_info(string):
    count_calls()
    result = (len(string), string.upper(), string.lower())
    #print(result)
    return result
def is_contains(string, list_to_search):
    count_calls()
    string = string.lower()
    for each in list_to_search:
        each = each.lower()
    if string in list_to_search:
        return True
    else:
        return False

str_list = ['Buka', 'Baka', 'Byaka', 'kukushka']
stroka = 'Kukushka'

num_func_calls1 = randint(1, 100) #сколько раз вызвать string_info
num_func_calls2 = randint(1, 100) #сколько раз вызвать is_contains

print(f'string_info будет вызвана {num_func_calls1} раз(-а),'
      f'is_contains будет вызвана {num_func_calls2} раз(-а)')

for i1 in range(num_func_calls1):
    string_info(stroka)
for i2 in range(num_func_calls2):
    is_contains(stroka, str_list)

print(f'Функции проработали {calls} раз')


