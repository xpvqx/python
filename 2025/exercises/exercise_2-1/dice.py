import random

antal_kast = 0      # räkna antal för kast

while True:
    kast_resultat = random.randint(1, 6) 
    print(kast_resultat)
    antal_kast += 1
    if antal_kast == 6:
        break
print(f'Det tog {antal_kast} kast att få en 6:a')
