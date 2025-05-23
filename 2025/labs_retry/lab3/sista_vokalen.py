# Skriv ett program som läser in ett ord från användaren. 
# Programmet ska skriva ut ordet men med den sista vokalen tredubblad.
# Vokaler är aouåeiyäö.

vokaler = 'aouåeiyäö'
ett_ord = input('Skriv in ett ord: ')
nytt_ord = ''

# hitta index för sista vokalen
sista_vokal_index = -1
for i in range(len(ett_ord)):
    if ett_ord[i] in vokaler:
        sista_vokal_index = i

# bygg nytt ord med tredubblad sista vokal
for i in range(len(ett_ord)):
    if i == sista_vokal_index:
        nytt_ord += ett_ord[i] * 3
    else:
        nytt_ord += ett_ord[i]

# skriv ut nytt ord
print(nytt_ord)
