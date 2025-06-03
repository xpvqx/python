# Skriv en funktion som tar en lista med heltal.
#
# Funktionen ska ändra listans element enligt följande regler:
#     - Positiva tal ska minskas med ett
#     - Negativa tal eller noll ska lämnas oförändrade

# funktion som tar en lista med heltal
def decrement(numbers):
    new_lst = []
    for i in range(len(numbers)):
        if numbers[i] > 0:
            new_lst.append(numbers[i] - 1)
        else:
            new_lst.append(numbers[i])
    return new_lst

tal = [9, 4, -8, -5, 0, 2]
nb = decrement(tal)

print(tal)
print(nb)

# funkar inte, man ska ändra i listan ej skapa ny
