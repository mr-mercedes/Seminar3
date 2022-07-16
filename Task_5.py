# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


def neg_fibo(n):
    nfib1 = 1
    nfib2 = -1
    nfib_list = []
    nfib_list.append(nfib1)
    nfib_list.append(nfib2)
    for i in range(2, n):
        nfib1, nfib2 = nfib2, nfib1 - nfib2
        nfib_list.append(nfib2)

    return nfib_list
    

def fibo(n):
    fib1 = 1
    fib2 = 1
    fib_list = []
    fib_list.append(fib1)
    fib_list.append(fib2)
    for i in range(2,n):
        fib1, fib2 = fib2, fib1 + fib2
        fib_list.append(fib2)
        
    return fib_list


def summ_list(positive_list, negative_list):
    last_list = []
    for i in range(n):
        last_list.append(negative_list[len(negative_list) - 1 - i])
        
    last_list.append(0)

    for i in range(n):
        last_list.append(positive_list[i])
    
    return last_list   

   
n = int(input('Введите число Фибоначи: '))   
negative_list = neg_fibo(n)
fibonaci_list = fibo(n)  
print(summ_list(fibonaci_list, negative_list))