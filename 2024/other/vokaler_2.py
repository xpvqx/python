ord = input('Skriv ett ord: ')
nytt_ord = ''

for bokstav in ord:
  if bokstav in 'aouåeiyäö':
    bokstav = bokstav.upper()
  else:
    bokstav = bokstav.lower()
  nytt_ord += bokstav

print(nytt_ord)