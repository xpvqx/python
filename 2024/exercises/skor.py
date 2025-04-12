# Alla mina strumpor har samma färg, storlek och modell. Varje strumpa kan alltså paras ihop
# med vilken annan strumpa som helst. Skriv ett program som läser in antalet strumpor som
# användaren plockar ut ur tvättmaskinen. Programmet ska beräkna och skriva ut antalet hela
# par och antalet överblivna strumpor.

# Programmet ska skriva ut resultatet på följande format:
# "Det finns m par och n överbliven strumpa."
# med värden på m och n beroende på antalet strumpor som användaren angett.


# Läs in data från användaren och gör om till heltal  13
socks = int(input('Antalet strumpor '))

# Beräkna antalet kompletta par                       6
m = int(socks / 2)

# Beräkna antalet överblivna strumpor                 1
n = int(socks % 2)

# Skriv ut resultatet                                'Det finns 6 par och 1 överbliven strumpa.'
print(f'Det finns {m} par och {n} överblivna strumpor ')