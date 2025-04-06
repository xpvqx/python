maxvikt = int(input("Ange maxvikt (kg): "))
bigboy = 0
mängdpacket = 0

while maxvikt != bigboy:
    paketvikt = int(input("Ange paket vikt (kg): "))
    if bigboy + paketvikt > maxvikt:
        break
    else:
        bigboy += paketvikt
        mängdpacket += 1

print(f"Du kan lasta {mängdpacket} paket. Totalvikten är {bigboy} kg.")