# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


def float_part(float_number):
    number = float_number % 1
    return number
    

def clear_list(some_list):
    new_list = []
    for i in range(len(my_list)):
        new_list.append(round(float_part(my_list[i]), 2))
        
    for i in range (len(new_list)):
        if new_list[i] == 0:
            new_list[i], new_list[len(new_list) - 1] = new_list[len(new_list) - 1], new_list[i]
            new_list.pop() 
            
    return new_list


   
my_list = [float(i) for i in input('Введите вещественные числа списка: ').split()]         
result = max(clear_list(my_list)) - min(clear_list(my_list))
print(result)

    