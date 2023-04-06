# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# *Пример:*

# 2 2
#     4 

def input_int_number(message):
    while(True):
        n = input(message)
        if n.isdigit():
            return int(n)
        else:
            print("Вы ввели не число.")

a = input_int_number("Введите число А: ")
b = input_int_number("Введите число B: ")

def rec(a, b):
    if b == 0:
        return a
    return 1 + rec(a, b - 1)

print(rec(a, b))