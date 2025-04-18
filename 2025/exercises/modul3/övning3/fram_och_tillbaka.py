# Skriv ett program som läser in ett ord från användaren. Programmet ska skriva ut det
# givna ordet framlänges och baklänges, vertikalt och sida vid sida. De två bokstäverna
# på varje rad ska skiljas åt av mellanslag och av ett bindestreck.

word = input('Ange ett ord: ')
backwards = word[::-1]

for i in range(len(word)):
    print(word[i], "-", backwards[i])
