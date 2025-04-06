# sista_vokalen
vokaler = 'aouåeiyäöAOUÅEIYÄÖ'
word = input("Skriv in ett ord: ")
sista = ''

for i in range(len(word) -1, -1, -1):
    if word[i] in vokaler:
        print(word)