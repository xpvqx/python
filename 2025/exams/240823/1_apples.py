antal_plockade = int(input('Antal plockade äpplen: '))
per_låda = int(input('Antal äpplen per låda: '))

resterande = antal_plockade % per_låda

if resterande == 0:
    kvar_att_plocka = 0
else:
    kvar_att_plocka = per_låda - resterande
print(kvar_att_plocka)
