# tre olika abonnemang; kontant normal och plus

# kontant är billigast om man ringer högst 33 min per månad
# normal lönar sig om man ringer mellan 33 och 66 minuter per månad
# plus är mest lönsamt om man ringer ännu mer

# läs in antal minuter man uppskattar att man kommer ringa per månad
# beräklna vilket abonnemang man bör välja

t = int(input('Hur många minuter ringer du per månad? '))

if t <= 33:
    print(f'Kontant är billigast')
elif t > 33 and t <= 66:
    print(f'Normal är billigast')
else:
    print(f'Plus är billigast')
