"""
Реализовать функцию, принимающую несколько параметров, описывающих данные
пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы. Реализовать
вывод данных о пользователе одной строкой.
"""


def user_data():
    user_name = input("Введите имя: ")
    user_surname = input("Введите фамилию: ")
    user_birth_year = input("Введите год рождения: ")
    user_city = input("Введите город проживания: ")
    user_email = input("Введите email: ")
    user_telephone = input("ведите телефон: ")
    return user_name, user_surname, user_birth_year, user_city, user_email, \
           user_telephone


print(user_data())
