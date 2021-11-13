def num_translate(key):
    if str(key).istitle():
        new_key = str(key).lower()
        return dictionary.get(new_key).title()
    else:
        return dictionary.get(key)

dictionary = {

    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять',
}

value = input('Введите значение на английском: ')

print(num_translate(value))
