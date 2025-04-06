user_word = input('Ange ett ord med gammal stavning: ')  # qvinna
nystavat = ''
for bokstav in user_word:
    if bokstav == 'q':
        nystavat += 'k'
    elif bokstav == 'w':
        nystavat += 'v'
    else:
        nystavat += bokstav
print(nystavat)                                          # kvinna