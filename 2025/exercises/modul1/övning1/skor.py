# Alla mina skor har samma färg, storlek och modell. Varje högersko kan alltså
# paras ihop med vilken vänstersko som helst och vice versa. Skriv ett program
# som läser in antalet vänsterskor och antalet högerskor från användaren.

# Programmet ska skriva ut resultatet på följande format:
# "Det finns m par och n överblivna skor."
# med värden på m och n beroende på antalet höger- och vänsterskor som
# användaren angett.


# Läs in antal vänsterskor och gör om till heltal         13
vänster_skor = int(input('Skriv in antalet vänster skor '))

# Läs in antal högerskor och gör om till heltal           9
höger_skor = int(input('Skriv in antalet höger skor '))

# Beräkna antal kompletta par                             9
m = min(vänster_skor, höger_skor)

# Beräkna antal överblivna skor                           4
n = abs(vänster_skor - höger_skor)

# Skriv ut resultatet                                     'Det finns 9 par och 4 överblivna skor.'
print(f'Det finns {m} par och {n} överblivna skor.')