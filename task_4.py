my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
           'токарь высшего разряда нИКОЛАй', 'директор аэлита']
i = 0
while i < len(my_list):
    new_list = "".join(my_list[i].title().split()[-1:])
    print('Привет, ', "".join(my_list[i].title().split()[-1:]), '!')
    i += 1
