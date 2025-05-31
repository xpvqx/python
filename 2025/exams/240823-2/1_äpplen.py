# läs in hur många äpplen som har plocakts
# samt hur många som för plats i varje låda
# skriv ut: hur många äpplen till som behöver plockas
# för att alla påbörjade lådor ska bli fyllda.

antal_plockade = int(input('Antal plockade äpplen: '))
per_låda = int(input('Antal äpplen per låda: '))

# % = resten efter division

resterande = antal_plockade % per_låda

if resterande == 0:
    kvar_att_plocka = 0
    print(f'Kvar att plocka: {kvar_att_plocka}')
else:
    kvar_att_plocka = per_låda - resterande
    print(f'Kvar att plocka: {kvar_att_plocka}')
