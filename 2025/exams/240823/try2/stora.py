ett_ord = input('Skriv in ett ord: ')
stora = input('Bokstäver att göra stora: ')
nytt_ord = ''

stora_små = stora.lower()

for bokstav in ett_ord:
    if bokstav in stora_små:
        nytt_ord += bokstav.upper()
    else:
        nytt_ord += bokstav.lower()
print(nytt_ord)
