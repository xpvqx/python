# Läs in tal från användaren
user_input = input('Ange en serie heltal, åtskilda av mellanslag: ')

# Omvandla strängen till en lista
user_list = user_input.split()

# Omvandla varje element i listan till ett heltal
numbers = [int(tal) for tal in user_list]

# Läs in ett målvärde från användaren och gör om till heltal
goal = int(input('Ange ett målvärde: '))



# Skriv ut resultatet: Definiera först closest
print('Närmast:', closest)
