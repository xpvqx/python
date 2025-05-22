ett_ord = input('Skriv in ett ord: ')
stora = input('Bokstäver att göra stora: ')
nytt_ord = ''

# Gör alla jämförelser på små bokstäver
stora_små = stora.lower()

for c in ett_ord:
    if c.lower() in stora_små:
        nytt_ord += c.upper()
    else:
        nytt_ord += c.lower()

print(nytt_ord)
