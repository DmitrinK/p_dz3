"""
Программа принимает действительное положительное число x и целое отрицательное
число y. Необходимо выполнить возведение числа x в степень y. Задание
необходимо реализовать в виде функции my_func(x, y). При решении задания
необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в
степень с помощью оператора *. Второй — более сложная реализация без
оператора *, предусматривающая использование цикла.
"""
user_x = int(input("Введите Х: "))
user_y = int(input("Введите Y: "))


def my_func(var_1, var_2):
    answer = var_1
    while var_2 > 1:
        answer = answer * var_1
        var_2 = var_2 - 1
    return 1 / answer


print(my_func(user_x, user_y))


def my_func2(var_1, var_2):
    answer = var_1
    while var_2 > 1:
        answer = answer + answer
        var_2 = var_2 - 1
    return 1 / answer


print(my_func2(user_x, user_y))
