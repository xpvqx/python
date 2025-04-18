# #Strängar är omuterbara, vilket innebär att deras innehåll inte kan ändras. Det
# visar sig att variabeln bokstav bara är en kopia av strängens bokstäver. När vi
# ändrar dess värde påverkar det inte strängen, utan bara den lokala kopian.
# Eftersom vi inte kan modifiera en sträng har vi inget annat val än att skapa en
# ny sträng.
#
# Modifiera koden från exemplet ovan så att strängens vokaler läggs till som
# stora bokstäver i den nya strängen och strängens konsonanter som små bokstäver.

word = input('Skriv ett ord: ')
word2 = ''

for c in word:
    if c in 'aouåeiyäö':
        c = c.upper()
        word2 += c
    else:
        c = c.lower()
        word2 += c
print(word2)
