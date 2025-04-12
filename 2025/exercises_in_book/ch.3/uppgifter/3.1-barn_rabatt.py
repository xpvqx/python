# vuxna = 10% rabatt av grundpris, barn 50% av grundpris

p = int(input('Grundpris?: '))
a = int(input('Ålder?: '))

if a < 12:
    p = p * 0.5
elif a > 65:
    p = p * 0.75
else:
    p = p * 0.9

print(f'Pris: {p:.2f} kr ')
