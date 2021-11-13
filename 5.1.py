import random 

def get_jokes(num):

    """Функция для создания шуточек без повтора слов"""

    random.shuffle(nouns)
    random.shuffle(adverbs)
    random.shuffle(adjectives)
    for i in range(num):
        jokes_lst.append(f'{nouns[i]} {adverbs[i]} {adjectives[i]}')
    return jokes_lst


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
jokes_lst = []

num = int(input('Сколько хотите шуточек? '))

print(get_jokes(num))