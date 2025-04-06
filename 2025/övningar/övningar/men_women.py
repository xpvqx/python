antal_kvinnor = int(input('Antal kvinnor: '))
antal_män = int(input('Antal män: '))
andel_kvinnor = float(antal_kvinnor / antal_män)
procent_kvinnor = (andel_kvinnor * 100)

print(f'I gruppen är det {procent_kvinnor:.2f} % kvinnor.')