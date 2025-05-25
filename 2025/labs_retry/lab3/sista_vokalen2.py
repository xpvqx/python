vokaler = 'aouåeiyäö'

ett_ord = input('Skriv in ett ord: ')
nytt_ord = ''

sista_vokalen_index = -1

# hitta sista vokalens index
for i in range(len(ett_ord)):
    if ett_ord[i] in vokaler:
        sista_vokalen_index = i

# bygg nytt ord
for i in range(len(ett_ord)):
    if i == sista_vokalen_index:
        nytt_ord += ett_ord[i] * 3
    else:
        nytt_ord += ett_ord[i]
print(nytt_ord)
