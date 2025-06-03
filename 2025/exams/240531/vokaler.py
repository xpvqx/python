vokaler = 'aouåeiyäöAOUÅEIYÄÖ'
ett_ord = input('Skriv in ett ord: ').lower()
nytt_ord = ''

for bokstav in ett_ord:
    if bokstav in vokaler:
        nytt_ord += bokstav.lower() + bokstav.upper() + bokstav.lower()
    else:
        nytt_ord += bokstav
print(nytt_ord)
