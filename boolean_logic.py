# print(True and False)  # and - операция логического умножения  - коньюнкция
# print(True or False) # or - операция логического сложения - дизъюнкция
# print(True == False)  # операция проверки равенства - эквивалентность
# print(True <= False) # операция импликации - логическое следование
print(not True)

print(True & False)  # and - операция логического умножения  - коньюнкция
print(True | False) # or - операция логического сложения - дизъюнкция
print(True is False)  # операция проверки идентичности - эквивалентность
print(True ^ False) # операция строго или (xor)

print(~1)  # операция нахождения дополнения к числу 1 -- 001 , complement  -> 110 -- -2
print(1<<4) # 1 > 10000 == 16

print(bin(45))
print(45<<2)

print(45>>3)



#
# эквивалентность
bool_var = [True, False]
for i in bool_var:
    for j in bool_var:
        print(i, j, i ^ j, sep='\t')
