def decrement(numbers):
    count = 0
    for i in range(len(numbers)):
        if numbers[i] > 0:
            numbers[i] -= 1  # ändra på plats
            count += 1
    return count

tal = [9, 4, -8, -5, 0, 2]
nb = decrement(tal)

print(tal)
print(nb)
