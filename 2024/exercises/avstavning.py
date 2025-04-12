# Läs in ett ord från användaren
word = input('Say something... ')
# Skapa en tom sträng som ska innehålle det nya ordet
new_word = ''
# Iterera över alla positioner i ordet, utom det sista
for i in range(len(word) -1):
    # Lägg till bokstaven på den givna positionen och ett bindestreck
    new_word += word[i] + '-'
# Lägg till den sista bokstaven
new_word += word[-1]
# Skriv ut resultatet
print(new_word)