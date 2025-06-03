import math

antal_barn = int(input('Antal barn: '))
kakor_per_burk = int(input('Antal kakor per burk: '))

kak_behov = math.ceil(antal_barn / kakor_per_burk)

print(kak_behov)
