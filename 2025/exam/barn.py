import math

antal_barn = int(input('Antal barn: '))
kakor_per_burk = int(input('Antal kakor per burk: '))

burkar = float(antal_barn / kakor_per_burk)


print(math.ceil(burkar))
