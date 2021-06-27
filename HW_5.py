# Ирина Хромова ДЗ 5

from collections import namedtuple, deque

# задание 1

Company = namedtuple('Company', [
    'quarter1', 'quarter2', 'quarter3', 'quarter4'
])

list_company = {}

n = int(input('Введите количество предприятий: '))

for i in range(n):
    name = input(str(i + 1) + '-е предприятие, введите название: ')
    income_q1 = float(input('Прибыль за 1-й квартал: '))
    income_q2 = float(input('Прибыль за 2-й квартал: '))
    income_q3 = float(input('Прибыль за 3-й квартал: '))
    income_q4 = float(input('Прибыль за 4-й квартал: '))
    list_company[name] = Company(
        quarter1=income_q1,
        quarter2=income_q2,
        quarter3=income_q3,
        quarter4=income_q4
    )

total_income = ()

for name, income in list_company.items():
    print(f'Предприятие: {name} прибыль за год - {sum(income)}')
    total_income += income

average_total_income = sum(total_income) / len(list_company)
print(f'Средняя прибыль за год среди всех предприятий {average_total_income}')

print('Предприятия, у которых прибыль выше среднего:')

for name, income in list_company.items():
    if sum(income) > average_total_income:
        print(f'{name} - {sum(income)}')

print('Предприятия, у которых прибыль ниже среднего:')

for name, income in list_company.items():
    if sum(income) < average_total_income:
        print(f'{name} - {sum(income)}')


# задание 2


def translate_hex():
    hex_number = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                  'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
                  0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
                  10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

    return hex_number


def sum_hex(x, y):
    hex_num = translate_hex()
    result = deque()
    transfer = 0

    if len(y) > len(x):
        x, y = deque(y), deque(x)
    else:
        x, y = deque(x), deque(y)

    while x:
        if y:
            res = hex_num[x.pop()] + hex_num[y.pop()] + transfer
        else:
            res = hex_num[x.pop()] + transfer

        transfer = 0

        if res < 16:
            result.appendleft(hex_num[res])
        else:
            result.appendleft(hex_num[res - 16])
            transfer = 1

    if transfer:
        result.appendleft('1')

    return list(result)


def multi_hex(x, y):
    hex_num = translate_hex()
    result = deque()
    interim = deque([deque() for _ in range(len(y))])

    x, y = x.copy(), deque(y)

    for i in range(len(y)):
        m = hex_num[y.pop()]
        for j in range(len(x) - 1, -1, -1):
            interim[i].appendleft(m * hex_num[x[j]])
        for _ in range(i):
            interim[i].append(0)

    transfer = 0

    for _ in range(len(interim[-1])):
        res = transfer
        for i in range(len(interim)):
            if interim[i]:
                res += interim[i].pop()
        if res < 16:
            result.appendleft(hex_num[res])
        else:
            result.appendleft(hex_num[res % 16])
            transfer = res // 16

    if transfer:
        result.appendleft(hex_num[transfer])

    return list(result)


a = list(input('Введите 1-е шестнадцатиричное число: ').upper())
b = list(input('Введите 2-е шестнадцатиричное число: ').upper())

print(f'{a} + {b} = {sum_hex(a, b)}')
print(f'{a} * {b} = {multi_hex(a, b)}')

# рекурсия ДЗ 2

# Задание 7
'''
Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число
'''


def left(c):
    if c == 1:
        return c
    elif c > 0:
        return c + left(c - 1)


def right(c):
    return c * (c + 1) // 2


n = int(input('Введите натуральное число n для прверки утверждения 1+2+...+n = n(n+1)/2: '))

if left(n) == right(n):
    print(f'Для n = {n} - True')
else:
    print(f'Для n = {n} - False')

print(f'левая часть = {left(n)}, правая часть = {right(n)}')
