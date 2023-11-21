# x = 0
# s = 0
# d = 1
# # var1 = input
# # var2 = input()
# n = int(input())
#
#
# while x < n:
#     # s = s + x
#     # x = x + d
#     s += x
#     x += d


# дорешать
# while x < n:
#     print(x)
#     if n % 2 == 0:
#         x = x + 1
#         print(n)
# написать без условия if внутри цикла

# n = int(input())
# x = 0
# x = n % 2 == 0
# while x <= n:
#         print(x)
#         x += 1

n = int(input())
# num_list = 0  # start
# while num_list <= n:  # stop
#     print(num_list)
#     num_list += 2 # step

for num in range(0, n + 1, 2):
    print(num)



# s = s + x
# x = x + d
# s += x
# x += d

# def x(n: int) -> object:
#     return [x for x in range(0, n + 1, 2)]
#
#
# val = x(12)
#
# print(x(int(input())))
# print(type(x))

# arr = {0, 1, 2, 3, 6, 1, 3}
# print(arr, type(arr))