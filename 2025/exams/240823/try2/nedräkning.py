# tar en lista med nummer:

# Positiva tal ska minskas med ett
# Negativa tal eller noll ska lämnas oförändrade
# Returnera antalet tal som ändrats

def decrement(numbers):

    counter = 0

    for i in range(len(numbers)):
        if numbers[i] > 0:
            numbers[i] -= 1
            counter += 1
    return counter

tal = [9, 4, -8, -5, 0, 2]
nb = decrement(tal)
print(tal) # [8, 3, -8, -5, 0, 1]
print(nb) # 3
