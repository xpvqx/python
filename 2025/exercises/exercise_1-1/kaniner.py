R = 2000
months = int(0)
while R < 20000:
    R += 0.1 * R * (1 - R / 25000)
    months += 1
print(f'{months}')