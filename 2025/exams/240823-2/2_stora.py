ett_ord = input('Skriv in ett ord: ')
stora = input('Bokstäver att göra stora: ').lower()
nytt_ord = ''

for bokstav in ett_ord:
    if bokstav.lower() in stora:
        nytt_ord += bokstav.upper()
    else:
        nytt_ord += bokstav.lower()
print(nytt_ord)
