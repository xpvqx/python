# Skriv ett program som läser in ett ord från användaren. Programmet ska skriva
# ut ordet men med den sista vokalen tredubblad. Vokaler är aouåeiyäö.

vokaler = 'aouåeiyäöAOUÅEIYÄÖ'
ett_ord = input('Skriv in ett ord: ')
nytt_ord = ''

# iterera över varje bokstav i ordet
sista_vokal_index = -1

for i in range(len(ett_ord)):
    if ett_ord[i] in vokaler:
        sista_vokal_index = i

for i in range(len(ett_ord)):
    if i == sista_vokal_index:
        nytt_ord += ett_ord[i] * 3
    else:
        nytt_ord += ett_ord[i]

print(nytt_ord)
