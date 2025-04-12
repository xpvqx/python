# Fråga användaren om namn
namn = input('Skriv in ditt för och efternamn ')

# Hitta första mellanslaget
pos = namn.find(' ')

# Använd slicing för att plocka ut efternamnet
efternamn = namn[pos+1:]

# Skriv ut resultatet
print(f'The name is {efternamn}, {namn}. ')