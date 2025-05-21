# En hobbyodlare plockar äpplen i trädgården och lägger i lådor. För att kunna
# ställa undan lådorna måste alla lådor vara fyllda. Skriv ett program som
# läser in hur många äpplen som plockats, samt hur många äpplen som får plats i
# varje låda. Programmet ska sedan skriva ut hur många äpplen till som behöver
# plockas för att alla påbörjade lådor ska bli fyllda. Utskriften ska se ut som
# i de givna exemplena.

antal_äpplen = int(input('Antal plockade äpplen: '))
äpplen_per_låda = int(input('Antal äpplen per låda: '))

resterande = antal_äpplen % äpplen_per_låda

if resterande == 0:
    kvar_att_plocka = 0
else:
    kvar_att_plocka = äpplen_per_låda

print(f"Antal äpplen kvar att plocka: {kvar_att_plocka}")
