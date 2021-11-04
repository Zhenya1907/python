list_cube = [] # создание списка кубов
for i in range(1, 1000, 2):
    list_cube.append(i**3)

list_sum_digits = [] # создание списка с суммой цифр каждого куба
for cube in list_cube:
    sum_digits = 0
    while cube > 0:
        sum_digits += cube % 10
        cube = cube // 10
    list_sum_digits.append(sum_digits)

main_sum = 0 # проверка деления на 7 и вывод суммы кубов
for indx in range(len(list_sum_digits)):
    if list_sum_digits[indx] % 7 == 0:
        main_sum += list_cube[indx]
print(main_sum)

for indx in range(len(list_cube)): # прибавление 17 к эллементам списка кубов
    list_cube[indx] += 17

new_main_sum = 0 # снова поиск суммы цифр, проверка деления на 7 и вывод суммы без создания нового списка
for indx in range(len(list_cube)):
    sum_digits = 0
    temporally_num = list_cube[indx]
    while temporally_num > 0:
        sum_digits += temporally_num % 10
        temporally_num = temporally_num // 10
    if sum_digits % 7 == 0:
        new_main_sum += list_cube[indx]
print(new_main_sum)