price = [58.9, 34.25, 20.8, 43.2, 22.15, 52.1,
         68.3, 56.4, 45.88, 10.5, 70.34, 67.30, 80.2]

for i in price:
    print(f'{int(i)} руб. {int(i * 100 % 100):02} коп.', end=', ')
price.sort()
print('\n'f'Список цен:{price} id: {id(price)}')

new_price = sorted(price, reverse=True)
print('\n' f'Новый список по убыванию: {new_price} id списка: {id(new_price)}')

print('\n', price[-5:])
