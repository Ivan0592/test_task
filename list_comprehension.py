# num_list = list(range(1, 12, 2))
#
# for num in num_list:
#     print(num)
# del num  # переменная для итерации в списке остается пока ее не удалишь
#
# print(num_list)
# num_list.insert(3, 99)
# print(num_list)
# for i in range(len(num_list)):
#     print(num_list[i], i)

# other_list = [1, 4, 8]
# num_list.append(other_list)
# print(num_list, hex(id(num_list)))
# del other_list
# print(num_list)


# 1) Я ввожу с консоли число в формате (X.X, .X или XXX). Ты выводишь мне целую часть от этого числа в целочисленном виде
# 2) с консоли я задаю число N. Программа создаёт список длины N из целочисленных значений по модулю не превосходящих 100.
# И выводит сумму этого списка.
# 3) В том же списке необходимо найти второе по убыванию значения число.



N = float(input("Введите число N: "))
i = int(N)
list_numbers = list(range(i, 101, 1))
print("Список чисел: ", list_numbers)
print("Сумма чисел в списке: ", sum(list_numbers))
print(max(list_numbers) - 1)

