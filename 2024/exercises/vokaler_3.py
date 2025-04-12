vokaler = 'aouåeiyäö'
empty = ''

# user input
word = input('Skriv in ett ord: ')

for bokstav in word:
    if bokstav.lower() in vokaler:
        empty += bokstav

print(empty)