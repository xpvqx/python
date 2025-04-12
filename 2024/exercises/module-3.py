# Definera vokaler
vokaler = 'aouåeiyäöAOUÊIYÄÖ'
# Be användaren om ett ord
ord = input('Skriv in ett ord: ')
# En tom variabel
nytt_ord = ''

for bokstav in ord:
    if bokstav in vokaler:
        bokstav = bokstav
        nytt_ord += bokstav
        sista_vokal = (ord + nytt_ord[-1] * 3)
print(sista_vokal)