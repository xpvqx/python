# på gymmet kan man antigen köpa ett årskort eller köpa biljett vid varje besök
# läs in pris för årskort, priset för en biljett och antal planerade besök under ett år
# beräkna om det lönar sig att köpa årskort eller inte

årskort = int(input('Hur mycket kostar ett årskort? '))
biljett = int(input('Hur mycket kostar en biljett? '))
besök = int(input('Hur många gånger tänker du gå till gymmet? '))

if årskort <= besök * biljett:
    print(f'Du borde skaffa årskort ')
else:
    print(f'Fortsätt köpa biljett ')
