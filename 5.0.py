import random 

def get_jokes(num):

    """Функция для создания шуточек"""

    for i in range(num):
        word_1 = random.choice(nouns)
        word_2 = random.choice(adverbs)
        word_3 = random.choice(adjectives)
        joke = f'{word_1} {word_2} {word_3}' 
        jokes_lst.append(joke)
    return jokes_lst


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
jokes_lst = []

num = int(input('Сколько хотите шуточек? '))

print(get_jokes(num))