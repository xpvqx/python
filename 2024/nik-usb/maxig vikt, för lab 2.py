maxigvikt = int(input("Ange maxvikt (kg): "))
packetvikt = int(input("Paketets vikt (kg): "))
mängdpacket = 0
if maxigvikt < packetvikt:
    print("Du kan lasta 0 paket. Totalvikten är 0 kg.")
else:
    mängdpacket += 1
    if maxigvikt == packetvikt:
        reee = 1
    else:      
     while maxigvikt > packetvikt:
        extrapacketvikt = int(input("Paketets vikt (kg): "))
        checkpacket = packetvikt
        checkpacket += extrapacketvikt
        if maxigvikt >= checkpacket:
            packetvikt += extrapacketvikt
            mängdpacket += 1
        elif maxigvikt < checkpacket:
            break
print(f"Du kan lasta {mängdpacket} paket. Totalvikten är {packetvikt} kg.")