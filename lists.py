# x = [1, 2, 'ab']
# print(x, id(x))
# x = x[:-1]
# x.append(4)
# append(x, 4)
# try:
#     try:
#
#         x.pop(10)
#         1 / 0
#     except IndexError as err:
#         x.pop()
#         print(str(err))
# except Exception:
#     print("error")
# finally:
#
#     print("We done")
# print(x, id(x))



# ДЗ:
# 1) Создать список из 100 рандомных элементов (если не получится то просто захардкодить
# руками список из 10 элементов) и отсортировать по остатку от деления на 3. Т.е.
# чначала идут числа чей очтаток от деления равен 0, потом 1, и далее 2
# 1.1) Сделать так чтоб программа не вылетала по ошибке при любом вводимом списке


import random
# num = []
# for i in range((10), 5):
#     num.append(randint(0, 100))
# print(num)


# num = list(map(int, input().split()))


num = [random.randint(1, 100) for i in range(100)]
num_sort = sorted(num)
sort = sorted(num_sort, key=lambda x: x % 3)
print(num)
print(num_sort)
print(sort)
