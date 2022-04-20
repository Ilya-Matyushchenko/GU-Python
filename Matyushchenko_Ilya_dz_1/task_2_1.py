my_list = []
check_list = 0
number_list = []
number_sum = 0

for i in range(1, 1000, 2):
    i = i ** 3
    my_list.append(i)

for number in my_list:
    i = number
    while i > 0:
        number_sum = i % 10
        i = i // 10
        check_list += number_sum
    if check_list % 7 == 0:
        check_list = 0
        number_list.append(number)
    else:
        check_list = 0

answer = 0
for i in number_list:
    answer += i
print(answer)