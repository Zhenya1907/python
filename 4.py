main_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for string in main_list:
    words_list = string.split(' ')
    name = words_list[len(words_list) - 1].title()
    print(f'Привет, {name}!')
    