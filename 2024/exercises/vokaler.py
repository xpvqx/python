# Läs in ett ord från användaren
word = input('Say something: ')
# Definera en sträng som innehåller alla vokaler
vokaler = 'aouåeiyäö'
# Itereraöver alla bokstäver i ordet
for bokstav in word:
    # Om den aktuella bokstaven finns i strängen vokaler..
    if bokstav in vokaler:
        # Skriv ut en asterisk
        print('*', end='')
    # Annars: den aktuella bokstaven är konstant
    else:
        print(bokstav, end='')
print()