# Läs in ett par ord från användaren
user_data = input('Skriv in dina ord: ')
# Gör om till en lista
user_list = user_data.split()

# Skriv din kod här...
# Loopa genom varje ord i listan
for word in user_list:
    # Kontrollera om ordet består enbart av versaler
    if word.isupper():
        # Skriv ut ordet om det uppfyller kraven
        print(word)