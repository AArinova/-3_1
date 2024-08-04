def print_params(a=1, b='строка', c=True):
    print(a, b, c)


values_list = [11, 'Джонни', False]

values_dict = {'a' : 12, 'b' : 'Donald', 'c' : True}

values_list_2 = ['first_element', 0]

print_params(*values_list)
print_params(**values_dict)
#Функция корректно отрабатывает следующие вызовы
print_params(b = 25)
#Работает print_params(*values_list_2, 42)
print_params(*values_list_2, 42)
print_params(b = 25)
print_params(c = [1, 2, 3])
