words = ['в', '"', '5', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+5', '"', 'градусов']
new_words = []

for i in range(len(words)):

    if words[i] != '"' and words[i].isdigit() == False and words[i][1:].isdigit() == False:
        new_words.append(words[i])
   
    elif words[i].isdigit():
        new_words.append(f'"{int(words[i]):02}"')

    elif (words[i][0] == '+' or words[i][0] == '-') and words[i][1].isdigit() == True:
        new_words.append(f'"{words[i][0]}{int(words[i][1:]):02}"')

print(' '.join(new_words)) 
       
