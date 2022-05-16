"""
Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield
"""


def num_gen(n):
    for i in range(1, n + 1, 2):
        yield i


num = int(input('Insert n: '))
ord_num = num_gen(num)
counter = 0
while counter < num:
    print(next(ord_num))
    counter += 1
