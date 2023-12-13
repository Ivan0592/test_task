import random


# choices = [str(), int(), list(), float()]
choices = [str()]
var = random.choice(choices)
# if type(var) == str:
# if isinstance(var, str):
#     print(True)
# else:
#     print(False)
# if isinstance(var, str)  == True:
#     print(True)
#
# print(var, type(var), isinstance(var, str))
#
#
# x = 30
#
# if 45 > x > 15:
#     print("Cool")


# colors = ['красный', 'зеленый', 'синий', 'желтый']
#
# for i in colors:
# #     for j in colors:
# #         for k in colors:
# #             for l in colors:
# #                 print(i, j, k, l)
#
# import itertools
#
# colors = ['красный', 'зеленый', 'синий', 'желтый']
#
# ctr = 0
# for combination in itertools.product(colors, repeat=5):
#     print(*combination, sep='\t')
#     ctr += 1
# print(ctr)

surname = input("Введите свою фамилию: ")
name = input("Введите свое имя: ")
midname = input("Введите свое отчество: ")


def format_name(name, midname, surname):
    # if name and midname and surname:
    #     return f"{surname} {name[0]}. {midname[0]}."
    # elif name and surname:
    #     return f"{name} {surname}"
    # elif name and midname:
    #     return f"{name} {midname}"
    # elif name:
    #     return name
    # elif surname:
    #     return surname
    #
    # else:
    #     return "Недостаточно информации"

    # return f"{midname} {name} {surname}" if (name and surname) or (surname and not midname) \
    #     else "Недостаточно информации"


# print(format_name(name, midname, surname))

names :list = input().split()
last_name, first_name, father_name = names[0], names[1], names[2]
s = ''
if len(names) > 0:
    s += "Afvbkbz" + names[0]
print(f"Фамилия: {last_name}, Имя: {first_name}, Отчество: {father_name}")


adress = input().split(", ")
street, house = adress[0], adress[1]
print(f"Улица: {street}, Дом: {house}")


s1 = "Дорогой{user}, ..."
s2 = "Ivan"
letter = s1.replace("{user}", s2)
print(letter)





