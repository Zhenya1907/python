def thesaurus(*names):

    letters = []
    temporary_lst = []
    main_dict = {}

    for name in names: # создание списка первых букв имен
        letters.append(name[0])
    lst_letters = sorted(set(letters))

    for letter in lst_letters: # создание словаря
        for name in names:
            if name[0] == letter:
                temporary_lst.append(name)
        main_dict.setdefault(letter, temporary_lst.copy())
        temporary_lst.clear()

    return main_dict


names = input('Введите имена: ').split()
print(thesaurus(*names))

            
