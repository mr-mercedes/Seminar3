# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import math

def complex_numbers(some_list):
    complex = []
    for i in range(math.ceil(len(some_list) / 2)):
        complex.append(some_list[i] * some_list[len(some_list) - i - 1])
    
    return complex


my_list = [int(i) for i in input('Введите элементы списка: ').split()]
print(complex_numbers(my_list))
            