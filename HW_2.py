# Ирина Хромова ДЗ 2

from os import urandom

# задание 1

while True:
    try:
        number1, operation, number2 = [
                i for i in
                input(
                    'Введите математическое выражение через пробел (число арифм. операцию число) '
                    'чтобы закончить введите 0 вместо операции: '
                    ).split()
                ]
    except ValueError:
        print('Неправильный ввод, введите арифм. операцию')
        continue
    number1 = int(number1)
    number2 = int(number2)

    if operation == '0':
        break
    elif operation == '+':
        print(f'{number1} {operation} {number2} = {number1 + number2}')
    elif operation == '-':
        print(f'{number1} {operation} {number2} = {number1 - number2}')
    elif operation == '*':
        print(f'{number1} {operation} {number2} = {number1 * number2}')
    elif operation == '/':
        try:
            print(f'{number1} {operation} {number2} = {number1 / number2}')
        except ZeroDivisionError:
            print('Ошибка. Деление на ноль')

# задание 2

number = input('Введите число больлше двухзначного: ')
even = 0
odd = 0
for f in number:
    i = int(f)
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print(f'У вашего числа {number}: четных цифр - {even}, нечетных - {odd} ')

# задание 3

number = input('Введите число, не менее двухзначного: ')

print(f'Чило {number} в обратном порядке: {number[::-1]}')

# задание 4

n = int(input('Введите количество элементов для вычисления суммы ряда чисел a /= -2: '))
i = 0
a = 1
sum_series = 0
while i < n:
    sum_series += a
    a /= -2
    i += 1

print(f'Сумма {sum_series}')

# задание 5

i = 1
for symbol in range(32, 128):
    if i % 10 == 0:
        print(f'{symbol:5}: {chr(symbol)}')
    else:
        print(f'{symbol:5}: {chr(symbol)}', end=' ')
    i += 1

# задание 6


def random_number():
    random = int(int.from_bytes(urandom(7), 'big')) >> 5
    li = [n for n in range(0, 101)]
    return li[random % 100]


right_number = random_number()
attempt = 1
while attempt <= 10:
    print(f'Попытка №{attempt:2} из 10')
    user_number = int(input('Введите число от 1 до 100: '))
    if user_number == right_number:
        print('Загаданное число угадано')
        break
    elif user_number > right_number:
        print(f'Ваше число {user_number} больше загаданного')
    else:
        print(f'Ваше число {user_number} меньше загаданного')
    attempt += 1
if attempt > 10:
    print(f'Не угадано! Загаданное число {right_number}')

# задание 7

m = int(input('Введите натуральное число n для прверки утверждения 1+2+...+n = n(n+1)/2: '))
right = 0
for i in range(1, m+1):
    right += i
left = m * (m + 1) // 2
print(right)
print(left)

# задание 8

user_range = input('Введите последовательность чисел без пробела: ')
search_digit = input('Введите цифру для поиска: ')
count = 0

for i in user_range:
    if i == search_digit:
        count += 1

print(
    f'Цифра встречается {search_digit} в последовательности {user_range}: \
{count} раз(а)'
        )

# задание 9


def digit_sum(numbers):
    s = 0
    for num in numbers:
        s += int(num)
    return s


li_numbers = [i for i in input('Введите натуральные числа через пробел и нажмите Enter: ').split()]

max_num = 0
max_sum = 0
for i in li_numbers:
    if digit_sum(i) > max_sum:
        max_num = i
        max_sum = digit_sum(i)

print(f'У числа {max_num} была наибольшая сумма цифр - {max_sum}')

