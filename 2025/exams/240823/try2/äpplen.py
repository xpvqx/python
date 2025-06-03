antal_plockade = int(input('Antal plockade äpplen: '))
per_låda = int(input('Antal äpplen per låda: '))

# skriv ut hur många som behöver plockas för att alla påbörjade lådor ska fyllas
resterande = antal_plockade % per_låda

if resterande == 0:
    kvar_att_plocka = 0
else:
    kvar_att_plocka = per_låda - resterande
print(f'Antal äpplen kvar att plocka: {kvar_att_plocka}')
