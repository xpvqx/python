antal_äpplen = int(input('Antal plockade äpplen: '))
äpplen_per_låda = int(input('Antal äpplen per låda: '))

resterande = antal_äpplen % äpplen_per_låda

if resterande == 0:
    kvar_att_plocka = 0
else:
    kvar_att_plocka = äpplen_per_låda - resterande
print(kvar_att_plocka)
