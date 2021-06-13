# Ирина Хромова ДЗ 1

from random import random

# задание 1

number = input('Введите трехзначное число: ')

num_sum = 0
multiplication = 1

for f in number:
    num_sum += int(f)
    multiplication *= int(f)

print(f'Сумма цифр числа {number}: {num_sum}')
print(f'Произведение цифр {number}: {multiplication}')

# задание 2

n = 5
m = 6

bit_and = n & m
bit_or = n | m
bit_xor = n ^ m
bit_not_n = ~n
bit_not_m = ~m
bit_shift_right = n >> 2
bit_shift_left = n << 2

print(f'Побитовое «И» (AND) для {bin(n)} и {bin(m)}: \
{bin(bit_and)} ({bit_and})')

print(f'Побитовое «ИЛИ» (OR) для {bin(n)} и {bin(m)}: \
{bin(bit_or)} ({bit_or})')

print(f'Исключающее «ИЛИ» (XOR) для {bin(n)} и {bin(m)}: \
{bin(bit_xor)} ({bit_xor})')

print(f'Побитовое отрицание (NOT) для {bin(n)}: \
{bin(bit_not_n)} ({bit_not_n}) и для {bin(m)}: \
{bin(bit_not_m)} ({bit_not_m})')

print(f'Битовый сдвиг вправо для {bin(n)}: \
{bin(bit_shift_right)} ({bit_shift_right})')

print(f'Битовый сдвиг влево для {bin(n)}: \
{bin(bit_shift_left)} ({bit_shift_left})')

# задание 3

x1, y1, x2, y2 = [
    int(x) for x in input('Введите кординаты двух точек через пробел x1 y1 x2 y2: ').split()
]

k = (y2 - y1)/(x2 - x1)
b = y1 - k * x1

print(f'Уравнение прямой: y = {k}x + {b}')

# задание 4

num_1 = int(input('Введите первое целое число: '))
num_2 = int(input('Введите второе целое число: '))
n_int = int(random() * (num_2 - num_1 + 1)) + num_1
print(f'Случайное целое число в вашем диапазоне: {n_int}')

num_3 = float(input('Введите первое вещественное число: '))
num_4 = float(input('Введите второе вещественное число: '))
n_float = random() * (num_4 - num_3) + num_3
print(f'Случайное вещественное число в вашем диапазоне: {round(n_float, 3)}')

let_1 = ord(input('Введите начальную букву диапазона: '))
let_2 = ord(input('Введите конечную букву диапазона: '))
n_let = int(random() * (let_2 - let_1 + 1)) + let_1
print(f'Случайная буква в вашем диапазоне: {chr(n_let)}')

# задание 5

letter_1, letter_2 = [
  x.upper() for x in input('Введите две буквы через пробел в диапазоне от A до Z: ').split()
]

abc_list = [chr(i) for i in range(ord('A'), ord('Z') + 1)]

index_letter_1 = abc_list.index(letter_1) + 1
index_letter_2 = abc_list.index(letter_2) + 1

if index_letter_1 < index_letter_2:
    step = 1
else:
    step = -1

print(f'Первая буква {letter_1}, находится на позиции: {index_letter_1}')
print(f'Вторая буква {letter_2}, находится на позиции: {index_letter_2}')

print(
    f'Между ними находятся буквы \
{abc_list[abc_list.index(letter_1) + step:abc_list.index(letter_2):step]} \
({abs(index_letter_1 - index_letter_2) - 1})'
        )

# задание 6

abc_number = int(input('Введите номер буквы в алфавите: '))

abc_list = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
print(abc_list)
if abc_number <= len(abc_list):
    print(f'Буква под номером {abc_number}: {abc_list[abc_number - 1]}')
else:
    print(
      f'Введено число превышающее количество букв в алфавите ({len(abc_list)})'
    )

# задание 7

a, b, c = [
      float(x) for x in input('Введите длины отрезков для треугольника через пробел: ').split()
        ]

if a < b + c and b < a + c and c < a + b:
    if a == b and b == c:
        print(f'Треугольник со сторонами {a} {b} {c} - равносторонний')
    elif a == b or b == c or c == a:
        print(f'Треугольник со сторонами {a} {b} {c} - равнобедренный')
    else:
        print(f'Треугольник со сторонами {a} {b} {c} - разносторонний')
else:
    print(f'Треугольника со сторонами {a} {b} {c} не существует')

# задание 8

year = int(input('Введите год: '))

if year % 400 == 0:
    print(f'Год {year} високосный')
elif year % 100 == 0 and year % 400 != 0:
    print(f'Год {year} невисокосный')
elif year % 4 == 0:
    print(f'Год {year} високосный')
else:
    print(f'Год {year} невисокосный')

# задание 9

number_1 = int(input('Введите первое целое число: '))
number_2 = int(input('Введите второе целое число: '))
number_3 = int(input('Введите третье целое число: '))

if number_2 < number_1 < number_3 or number_3 < number_1 < number_2:
    print('Среднее:', number_1)
elif number_1 < number_2 < number_3 or number_3 < number_2 < number_1:
    print('Среднее:', number_2)
else:
    print('Среднее:', number_3)
