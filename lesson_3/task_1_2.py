def num_translate_adv(a):
    my_dict = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре',
               'five': 'пять', 'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
    if a.istitle() and a.lower() in my_dict:
        a = a.lower()
        print(my_dict.get(a).title())
    else:
        print(my_dict.get(a))


while True:
    numeric = input()
    if numeric == 'end':
        break
    else:
        num_translate_adv(numeric)
