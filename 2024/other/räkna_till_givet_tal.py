# Läs in ett positivt heltal från användaren.
tal = int(input('Ange ett positivt heltal'))

# Skriv ut alla tal från 1 till och med det givna talet. Talen ska skrivas på varsin rad.
if tal > 0:
    for i in range(1, tal + 1):
        print(i)