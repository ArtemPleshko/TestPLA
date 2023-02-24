"""
Задача 1

Создать массив (50 элементов) случайных натуральных чисел от -100 до 100

Вывести в цикле данные массива подписывая их "отрицательное/положительное/ноль это тоже число: x" в зависимости от значения икса
"""


import numpy as np
a = np.random.randint(-100, 100, size = (50))
print(a)
arr_odd = [j for j in a if j < 0]
arr_even = [j for j in a if j > 0]
arr_zero = [j for j in a if j == 0]

print(f'Не чётный:{arr_odd}\nЧётный:{arr_even}\nНоль:{arr_zero}')


