ord = input('Skriv ett ord ')
vokaler = 'aouåeiyäöAOUÅEIY'

for c in ord:
    if c in vokaler:
        print(c, end='')
