price_list= [99.9, 11, 88.8, 21.21, 77, 13.13, 39.39, 74.74, 45.45, 68.68]

for price in price_list:
    rub = int(price)
    coin = int((price - rub) * 100)
    print(f'{rub} руб {coin:02d} коп')

print('Основной список + ID:', price_list, id(price_list))


price_list.sort()
print('Основной список, отсортированный по возрастанию + ID:', price_list, id(price_list))

price_list_new = price_list.copy()
price_list_new.reverse()
print('Новый список, отсортированный по убыванию + ID:', price_list_new, id(price_list_new))

print('Цены пяти самых дорогих товаров по возрастанию:', *price_list_new[4::-1])