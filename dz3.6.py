"""
Реализовать функцию int_func(), принимающую слово из маленьких латинских букв
и возвращающую его же, но с прописной первой буквой. Например,
print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов,
разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной
буквы. Необходимо использовать написанную ранее функцию int_func().
"""
user_str = input("Введите слово: ")
print(user_str.capitalize())


def int_func(var_1):
    return str.capitalize(var_1)


def ext_func(var_1):
    str_transformation = var_1.split(' ')
    count = 0
    while count < len(str_transformation):
        str_transformation[count] = int_func(str_transformation[count])
        count += 1
    return str_transformation


print(int_func(user_str))
print(ext_func(user_str))
