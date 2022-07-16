# ; Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# ; Пример:

# ; - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


def summ_numbers(some_list):
    summ = 0
    for i in range(1, len(some_list), 2):
        summ += some_list[i]
    
    return summ


my_list = [int(i) for i in input('Введите элементы списка: ').split()]
print(summ_numbers(my_list))
