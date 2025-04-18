# Läs in cirkelns radie
# Beräkna och skriv ut cirkelns omkrets och area och skriv ut resultaten med  3 decimaler

# c (omrkets) = 2 * pi * r
# a (area) = pi * (r ** 2)

# Kontrollera om radien är större än 0, om inte skriv ut felmeddelande

import math 

r = float(input('Hur stor är radien? '))
if r > 0:
    a = float(math.pi * (r ** 2))
    c = float(math.pi * 2 * r)
    print(f'Om radien är {r} cm, är arean {a:.3f} cm^2 och omkretsen är {c:.3f} cm.')
else:
    print(f'Ej tillåten inmatning.')
