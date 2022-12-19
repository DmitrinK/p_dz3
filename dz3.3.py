"""Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""
num_1 = int(input("Введите первое число: "))
num_2 = int(input("Введите второе число: "))
num_3 = int(input("Введите третье число: "))


def my_func(var_1, var_2, var_3):
    if var_1 < var_2 and var_3:
        return var_2 + var_3
    elif var_2 < var_1 and var_3:
        return var_1 + var_3
    elif var_3 < var_1 and var_2:
        return var_1 + var_2
    else:
        return "Значения чисел равны"


print(my_func(num_1, num_2, num_3))
