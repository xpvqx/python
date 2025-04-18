# Använd medlemskapsoperatorn för att komplettera följande kod så att texten "Det finns inget x i ordet"
# skrivs ut om användaren anger ett ord utan x i.

# medlemsskapoperatorn = 'in'

ord = input('Skriv ett ord som innehåller bokstaven x: ')
x ='x'

if x not in ord:                            # om bokstaven inte finns i ordet
    print('Det finns inget x i ordet')      # skriv ut felmeddelande
else:                                       # annars printa ord
    print(ord)
