for i in range(0, 101):
    if i == 11 or i == 12 or i == 13 or i == 14:
        print(i, 'процентов')
    elif i % 10 == 1:
        print(i, 'процент')
    elif 2 <= (i % 10) <= 4:
        print(i, 'процента')
    elif 5 <= (i % 10) <= 9 or i % 10 == 0:
        print(i, 'процентов')