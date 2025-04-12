# Läs in ord från användaren
ord = input('Skriv in ett ord: ')
baklänges_ord = ord[::-1]

for bokstav in baklänges_ord:
    print(bokstav)