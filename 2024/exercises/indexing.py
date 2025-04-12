word = input("Skriv in ett ord: ")  # Läs in user-input
vowels = "aouåeiyäöAOUÅEIYÄÖ"       # Definera vokalerna
new_word = ""                       # Skapa en tom sträng för att lagra det modifierade ordet

last_vowel = -1     # index för den sista vokalen = -1

# Hitta den sista vokalen och dess position
for i in range(len(word) - 1, -1, -1):
    if word[i] in vowels:       # Om bokstaven är en vokal..
        last_vowel = i          # ..spara index för sista vokalen
        break                   # Avsluta loopen när sista vokalen har hittats

# Modifiera ordet om det finns minst en vokal
if last_vowel != -1:
    for i in range(len(word)):
        if i == last_vowel:         # Om indexet matchar den sista vokalen..
            new_word += word[i] * 3 # ..multiplicera den sista vokalen och lägg till i den modifierade strängen
        else:
            new_word += word[i]     # Annars lägg till bokstaven till ordet utan att multiplicera
else:
    new_word = word                 # Om det inte finns någon vokal använd originalordet

# Skriv ut det nya ordet
print(new_word)