# Skriv ett program som läser in först ett ord från användaren, sedan ett par bokstäver. Programmet ska sedan skriva ut ordet på följande sätt: I utskriften ska alla förekomster av de angivna bokstäverna vara stora, medan övriga bokstäver ska vara små.

# Om ordet från användaren innehåller stora bokstäver, som inte finns med bland de bokstäver som ska göras stora, ska de alltså göras om till små. Andra tecken än bokstäver ska lämnas oförändrade.

ett_ord = input('Skriv ett ord: ')
stora = input('Bokstäver att göra stora: ').lower()
nytt_ord = ''

for bokstav in ett_ord:
    lilla = bokstav.lower()
    if lilla in stora:
        # Bokstav finns i "stora"-listan, kolla originalens skiftläge
        if bokstav.isupper():
            # Ursprungligen stor → gör liten
            nytt_ord += lilla
        else:
            # Ursprungligen liten → gör stor
            nytt_ord += lilla.upper()
    else:
        # Bokstaven finns ej i listan → alltid liten (om bokstav)
        if bokstav.isalpha():
            nytt_ord += lilla
        else:
            # Tecken som inte är bokstav lämnas som de är
            nytt_ord += bokstav

print(nytt_ord)
