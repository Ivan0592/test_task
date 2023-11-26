# x = input()
# print(x)
#
# i = float(x)
# print(i)

# def surname_initials(surname, name):
#     s = name[0] + '. ' + surname
#     print(s)
#     return "My name is " + s
#
#
# my_name = surname_initials("Dima", "Shutov")

# print(my_name)


# def surname_initials(surname: str, name: str | None = None) -> str:
#     """
#     Function return surname with initials
#     :param surname:
#     :param name:
#     :return: string like D. Shutov
#     """
#     if name:
#         s = name[0] + '. ' + surname
#     else:
#         s = surname
#     print(s)
#     return "My name is " + s
#
#
# my_name = surname_initials("Shutov")

# m = max(3, 5, 6, 80, )
# print(m)


# print("mather", "wash", "window", sep=" ", end="!")
# print("New string", "new line")
# print("Other string")

# import pprint

# pprint.pprint(input)
# print([12, 45, 56, [45, 67, 3], [34, 56, 12, 34]])


import random

random_list = []
n = int(input())
for _ in range(n):
    random_list.append(random.randint(n, 100))


print("Список чисел: ", random_list)
print("Сумма чисел в списке: ", sum(random_list))
print("Второе по убыванию число: ", random_list[-2])
