my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

i = 0
while i < len(my_list):
    sign = None
    if my_list[i][0] in '+ -':
        sign = my_list[i][0]
    if my_list[i].isdigit() or (sign and my_list[i][1:].isdigit()):
        if sign:
            my_list[i] = sign + my_list[i][1:].zfill(2)
        else:
            my_list[i] = my_list[i].zfill(2)

        my_list.insert(i, '"')
        my_list.insert(i + 2, '"')
        i += 2
    i += 1
print(my_list)
new_my_list = " ".join(my_list)
print(new_my_list)