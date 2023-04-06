# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

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
        return 1
    return a * rec(a, b -1)

print(rec(a, b))