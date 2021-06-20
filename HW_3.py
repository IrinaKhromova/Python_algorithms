# Ирина Хромова ДЗ 3

import random

# задание 1

result = {}
for num in range(2, 10):
    result[num] = []
    for number in range(2, 100):
        if number % num == 0:
            result[num].append(number)
    print(
        f'{num} кратны - {len(result[num])} чис. Кратные: {result[num]}'
        )

# задание 2

orig_array = [random.randint(0, 99) for _ in range(10)]
print(f'Исходный массив {orig_array}')
even_index = []

for element in orig_array:
    if element % 2 == 0:
        even_index.append(orig_array.index(element))

print(f'Индексы чётных элементов исходного массива: {even_index}')

# задание 3

random_array = [random.randint(0, 99) for _ in range(10)]
print(f'Исходный массив: {random_array}')

max_element = random_array[0]
min_element = random_array[0]

for elem in random_array:
    if elem > max_element:
        max_element = elem
    elif elem < min_element:
        min_element = elem
min_index = random_array.index(min_element)
max_index = random_array.index(max_element)
random_array[min_index], random_array[max_index] = \
    random_array[max_index], random_array[min_index]
print(
    f'Массив после замены местами минимального {min_index}'
    f' и максимального {max_index} элементов: {random_array}'
    )

# задание 4

array_4 = [random.randint(0, 99) for _ in range(20)]
print(f'Массив: {array_4}')

max_index = 0
for el in array_4:
    if array_4.count(max_index) < array_4.count(el):
        max_index = array_4.index(el)

print(
    f'Число {array_4[max_index]}, встречается чаще всех,'
    f' {array_4.count(max_index)} раза'
    )

# задание 5

array_5 = [random.randint(-99, 99) for _ in range(10)]
print(f'Массив: {array_5}')

min_index = 0

for el in array_5:
    if array_5[min_index] > el:
        min_index = array_5.index(el)

if array_5[min_index] >= 0:
    print(f'В массиве нет отрицательных элементов')
else:
    print(
        f'Минимальный отрицательный элемент: {array_5[min_index]},'
        f' позиция {min_index}'
        )

# задание 6

array_6 = [random.randint(0, 99) for _ in range(10)]
print(f'Массив: {array_6}')

min_index = 0
max_index = 0
step = 1
el_sum = 0

for elem in array_6:
    if array_6[min_index] > elem:
        min_index = array_6.index(elem)
    elif array_6[max_index] < elem:
        max_index = array_6.index(elem)

if max_index - min_index < 0:
    step = -1

for elem in array_6[min_index + step:max_index:step]:
    el_sum += elem

print(
    f'Сумма элементов между минимальным ({array_6[min_index]})',
    f' и максимальным ({array_6[max_index]}) элементами: {el_sum}'
    )

# задание 7

array_7 = [random.randint(0, 99) for _ in range(10)]
print(f'Массив: {array_7}')

min_index_1 = 0
min_index_2 = 1

for el in array_7:
    if array_7[min_index_1] > el:
        min_index_2 = min_index_1
        min_index_1 = array_7.index(el)
    elif array_7[min_index_2] > el:
        min_index_2 = array_7.index(el)

print(f'Два наименьших элемента: {array_7[min_index_1]} и {array_7[min_index_2]}')

# задание 8

matrix_8 = []

for i in range(4):
    matrix_8.append([])
    row_sum = 0
    for j in range(4):
        user_number = int(input(f'Введите элемент {i+1} строки и {j+1} столбца (целое число): '))
        row_sum += user_number
        matrix_8[i].append(user_number)

    matrix_8[i].append(row_sum)

for col in matrix_8:
    print(('{:4d}' * 5).format(*col))

# задание 9

matrix_9 = []

for i in range(3):
    matrix_9.append([])
    matrix_9[i].extend([random.randint(0, 99) for _ in range(3)])

min_list = []
min_list.extend(matrix_9[0])
print('Исходная матрица: ')

for row in matrix_9:
    print(('{:4d} ' * len(row)).format(*row))
    i = 0
    for j in row:
        if j < min_list[i]:
            min_list[i] = j
        i += 1

print('Минимальные элементы каждого столбца')
print(('{:4d} ' * len(min_list)).format(*min_list))

min_list.sort(reverse=True)
print(
    'Максимальный элемент среди минимальных элементов'
    ' столбцов матрицы:', min_list[0]
    )

