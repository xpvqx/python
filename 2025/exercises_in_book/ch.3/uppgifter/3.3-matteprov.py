# Man kan få högst 50p.
# E = 25p, D = 30p, C = 35p, B = 40p, A = 45p.

poäng = int(input('Hur många poäng? '))

if poäng >= 45:
    betyg = 'A'
elif poäng >= 40:
    betyg = 'B'
elif poäng >= 35:
    betyg = 'C'
elif poäng >= 30:
    betyg = 'D'
elif poäng >= 25:
    betyg = 'E'
else:
    betyg = 'F'

print(f'{poäng} poäng. Betyg: {betyg}.')
