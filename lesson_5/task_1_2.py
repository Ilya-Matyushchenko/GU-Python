"""
* (вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield.
"""


n = int(input('Insert n: '))
num_gen = (num for num in range(1, n+1, 2))
counter = 0
while counter < n:
    print(next(num_gen))
    counter += 1