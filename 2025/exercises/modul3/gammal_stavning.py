# q byttes ut mot k
# w byttes ut mot v

user_word = input('Ange ett ord med gammal stavning: ')  # qvinna
new_word = ''

for c in user_word:         # for varje bokstav i ordet
    if c == 'q':            # om bokstaven i ordet är 'q'
        new_word += 'k'     # byt ut till 'k' i nytt ord
    elif c == 'w':          # eller om bokstaven är 'w'
        new_word += 'v'     # byt ut till v i nytt ord
    else:                   # annars...
        new_word += c       # lägg till varje bokstav i nya ordet
print(new_word)             # printa nya ordet
