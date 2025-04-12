# Läs in tal från användare
n = int(input('n: '))

# Skapa en variabel för att lagra resultatet
n_fakultet = 1

# Multiplicera heltalen från 1 till n
for i in range(1, n + 1):
    n_fakultet *= i

# Skriv ut resultatet
print('n!:', n_fakultet)