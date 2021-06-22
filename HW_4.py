# Ирина Хромова ДЗ 4

import timeit
import cProfile

# задание 1


def hw3_1():
    result = {}
    for num in range(2, 10):
        result[num] = []
        for number in range(2, 100):
            if number % num == 0:
                result[num].append(number)
        print(
            f'{num} кратны - {len(result[num])} чис. Кратные: {result[num]}'
            )


hw3_1()
step = 1
while step <= 3:
    print(timeit.timeit(setup='from __main__ import hw3_1'))
    step += 1
cProfile.run('hw3_1()')

'''
Время:                    
0.012035900000000002
0.013966199999999998
0.015045799999999998

 198 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 HW_4.py:9(hw3_1)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        8    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        8    0.000    0.000    0.000    0.000 {built-in method builtins.print}
      178    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''

# задание 2


def without_eratosthenes(c):       # Функция поиска i-го простого числа,
    li = []                        # без использования алгоритма «Решето Эратосфена»
    for i in range(2, c + 1):      # асимптотика О(n^2)
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            li.append(i)
    return li


def eratosthenes(c):               # Функция поиска i-го простого числа,
    a = [0] * c                    # с использованием алгоритма «Решето Эратосфена»
    for i in range(c):             # асимптотика O(n log log n)
        a[i] = i
    a[1] = 0
    m = 2
    while m < n:
        if a[m] != 0:
            j = m * 2
            while j < n:
                a[j] = 0
                j = j + m
        m += 1
    b = []
    for i in a:
        if a[i] != 0:
            b.append(a[i])

    del a
    return b


def time_stat(s):
    f = 1
    while f <= s:
        print(
            f'{f} запуск без решета',
            timeit.timeit(setup='from __main__ import without_eratosthenes')
            )
        print(
            f'{f} запуск с решетом',
            timeit.timeit(setup='from __main__ import eratosthenes')
        )
        f += 1


n = int(input('Введите верхнюю границу для поиска простых чисел от 0 до n: '))
step = int(input('Введите количество запусков: '))
# print(without_eratosthenes(n))
# print(eratosthenes(n))
time_stat(step)

'''
Введите верхнюю границу для поиска простых чисел от 0 до n: 1000000000
Введите количество запусков: 6
1 запуск без решета 0.010032900000000566
1 запуск с решетом 0.007057500000000161
2 запуск без решета 0.006871499999999919
2 запуск с решетом 0.007456400000000585
3 запуск без решета 0.006869200000000575
3 запуск с решетом 0.008455600000000452
4 запуск без решета 0.007721000000000089
4 запуск с решетом 0.007548500000000402
5 запуск без решета 0.00689450000000047
5 запуск с решетом 0.007033199999999518
6 запуск без решета 0.006917599999999524
6 запуск с решетом 0.007194000000000145
'''
